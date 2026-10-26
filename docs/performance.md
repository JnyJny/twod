# Performance Guide

twod is plain Python, so each operation costs on the order of 50 to 500
nanoseconds. That is fine for a game loop with hundreds of points. For
thousands of points per frame or more, use NumPy instead.

## Measured Costs

Best of five `timeit` runs on Python 3.13, Apple silicon. Treat the numbers
as relative, not absolute: they vary by machine and Python version.

| Operation                        | Time   |
|----------------------------------|--------|
| `Point(3, 4)`                    | 53 ns  |
| `p.x` read or write              | 5 ns   |
| `p + q`                          | 119 ns |
| `p += q`                         | 72 ns  |
| `p * 2`                          | 198 ns |
| `p.distance(q)`                  | 97 ns  |
| `p.dot(q)`                       | 66 ns  |
| `p.rotate(0.5)` (in place)       | 161 ns |
| `p.rotate(0.5, inplace=False)`   | 222 ns |
| `Rect(0, 0, 10, 10)`             | 161 ns |
| `Point(5, 5) in rect`            | 290 ns |
| `rect.center`                    | 103 ns |

To measure on your machine:

```python
import timeit
from twod import Point

p, q = Point(3, 4), Point(1, 2)
n = 200_000
print(timeit.timeit("p.distance(q)", globals={"p": p, "q": q}, number=n) / n)
```

## Mutable Points Avoid Allocations

`Point` is mutable. In-place operators update the point instead of creating
a new one, which is about 40 percent faster than the allocating form:

```python
from twod import Point

position = Point(0, 0)
velocity = Point(2, 1)

position += velocity  # 72 ns, no new Point
position = position + velocity  # 119 ns, allocates a Point
```

`rotate` and `scale` also work in place by default.

## Compare Squared Distances

`distance_squared` skips the square root, which is all you need to compare
or sort by distance:

```python
from twod import Point

origin = Point(0, 0)
points = [Point(i, i) for i in range(100)]
radius = 25

closest = min(points, key=lambda p: origin.distance_squared(p))
nearby = [p for p in points if origin.distance_squared(p) <= radius * radius]
```

## Reuse Trigonometry

Rotating many points by the same angle recomputes `cos` and `sin` each
time. Compute them once instead:

```python
import math
from twod import Point

points = [Point(i, i) for i in range(100)]
angle = math.pi / 4

cos, sin = math.cos(angle), math.sin(angle)
rotated = [Point(p.x * cos - p.y * sin, p.x * sin + p.y * cos) for p in points]
```

## Use NumPy for Bulk Work

For large collections, convert once and let NumPy do the arithmetic:

```python
import numpy as np
from twod import Point

origin = Point(0, 0)
points = [Point(i, i) for i in range(100)]

coords = np.array([p.xy for p in points])
distances = np.hypot(*(coords - origin.xy).T)
```

NumPy is tuned for this and will beat any pure Python approach, including
this library.

## Complex Number Classes

`CPoint` and `CRect` stored a point as one complex number. They were slower
than `Point` and `Rect` for nearly everything measured (construction, `x`
and `y` access, arithmetic and rotation, by roughly 2 to 16 times), and they
are deprecated. Use `Point` and `Rect`.
