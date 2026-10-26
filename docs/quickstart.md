# Quickstart Guide

This guide will get you up and running with twod in minutes. We'll cover the basic classes and operations you need to know.

## Basic Point Operations

### Creating Points

```python
from twod import Point

# Create points
origin = Point()  # Defaults to (0, 0)
p1 = Point(3, 4)
p2 = Point(x=10, y=20)

# From tuple or list
p3 = Point((5, 6))
p4 = Point([7, 8])

print(f"Origin: {origin}")  # Origin: Point(0, 0)
print(f"P1: {p1}")  # P1: Point(3, 4)
```

### Point Arithmetic

```python
from twod import Point

a = Point(1, 2)
b = Point(3, 4)

# Addition and subtraction
c = a + b  # Point(4, 6)
d = b - a  # Point(2, 2)

# Multiplication and division
e = a * 2  # Point(2, 4)
f = b / 2  # Point(1.5, 2.0)

# Dot product and cross product
dot = a.dot(b)  # 11 (1*3 + 2*4)
cross = a.cross(b)  # -2 (1*4 - 2*3)
```

### Distance and Geometry

```python
from twod import Point

p1 = Point(0, 0)
p2 = Point(3, 4)

# Distance calculations
distance = p1.distance(p2)  # 5.0
dist_sq = p1.distance_squared(p2)  # 25.0

# Midpoint
mid = p1.midpoint(p2)  # Point(1.5, 2.0)

# Polar coordinates
radius = p2.radius  # 5.0
angle = p2.degrees  # 53.13010235415598
```

## Flexible Input

Geometry methods accept `(x, y)` tuples and lists as well as `Point`s, and
`Point.from_any` builds a `Point` from several kinds of value:

```python
from twod import Point

p = Point(3, 4)

# Methods accept tuples
distance = p.distance((5, 6))
midpoint = p.midpoint((5, 6))

# Build a Point from other values
Point.from_any((5, 6))  # from a tuple or list
Point.from_any({"x": 1, "y": 2})  # from a dict
Point.from_any(1 + 2j)  # from a complex number
Point.from_any("1+2j")  # from a string
Point.from_polar(5, 0.927)  # radius=5, angle=0.927 radians

# Rotate about the origin or another point
p.rotate(90, is_degrees=True)  # in place
q = p.rotate(90, origin=(1, 1), is_degrees=True, inplace=False)  # new Point
```

## Rectangles

### Creating Rectangles

```python
from twod import Point, Rect

# From two points
bottom_left = Point(0, 0)
top_right = Point(10, 20)
rect = Rect(bottom_left, top_right)

# Properties
print(f"Width: {rect.width}")  # Width: 10
print(f"Height: {rect.height}")  # Height: 20
print(f"Area: {rect.area}")  # Area: 200
print(f"Center: {rect.center}")  # Center: Point(5, 10)
```

### Rectangle Operations

```python
from twod import Point, Rect

rect = Rect(Point(0, 0), Point(10, 10))

# Check if point is inside
test_point = Point(5, 5)
inside = test_point.inside(rect.bottom_left, rect.top_right)  # True

# Rectangle arithmetic
moved_rect = rect + Point(5, 5)  # Moves rectangle by (5, 5)
scaled_rect = rect * 2  # Scales rectangle by 2
```

## Lines

### Creating and Using Lines

```python
from twod import Point, Line

# Create a line
start = Point(0, 0)
end = Point(3, 4)
line = Line(start, end)

# Properties
print(f"Length: {line.length}")  # Length: 5.0
print(f"Angle: {line.angle_degrees}")  # Angle: 53.13010235415598
print(f"Midpoint: {line.midpoint}")  # Midpoint: Point(1.5, 2.0)
print(f"Slope: {line.slope}")  # Slope: 1.3333333333333333
```

### Line Operations

```python
from twod import Point, Line

line1 = Line(Point(0, 0), Point(2, 2))
line2 = Line(Point(0, 2), Point(2, 0))

# Intersection
intersection = line1.intersection_point(line2)  # Point(1, 1)
intersects = line1.intersects_line(line2)  # True

# Distance from point to line
test_point = Point(1, 0)
distance = line1.distance_to_point(test_point)  # 0.7071067811865476

# Line relationships
horizontal = Line(Point(0, 0), Point(5, 0))
vertical = Line(Point(0, 0), Point(0, 5))
perpendicular = horizontal.perpendicular_to(vertical)  # True
```

## Ellipses

```python
from twod import Ellipse

# An ellipse is a Point (its center) with semi-axes along x and y
ellipse = Ellipse(x=0, y=0, major_axis=5, minor_axis=3)

print(ellipse.e)  # 0.8
print(ellipse.focus1, ellipse.focus2)  # Point(x=4.0, y=0) Point(x=-4.0, y=0)
print(ellipse.vertices)  # [Point(x=5, y=0), Point(x=-5, y=0)]
print(ellipse.co_vertices)  # [Point(x=0, y=3), Point(x=0, y=-3)]
```

## Common Patterns

### Finding Closest Point
```python
from twod import Point, Line

line = Line(Point(0, 0), Point(10, 0))
test_point = Point(5, 3)
closest = line.closest_point_on_line(test_point)  # Point(5, 0)
```

### Checking Geometric Relationships
```python
from twod import Point

# Check if three points are collinear
p1, p2, p3 = Point(0, 0), Point(1, 1), Point(2, 2)
collinear = p1.is_colinear(p2, p3)  # True

# Check counter-clockwise orientation
ccw = p1.is_ccw(p2, Point(1, 2))  # True
```

### Working with Angles
```python
from twod import Point, Line

line1 = Line(Point(0, 0), Point(1, 0))  # Horizontal
line2 = Line(Point(0, 0), Point(1, 1))  # 45 degrees

angle_rad = line1.angle_between(line2)  # π/4 radians
angle_deg = angle_rad * 180 / 3.14159  # ~45 degrees
```

## Next Steps

Now that you understand the basics, explore:

- [Examples](examples.md) - More detailed usage examples
- [API Reference](api/index.md) - Complete method documentation
- [Performance Guide](performance.md) - When to use different implementations
- [Geometry Concepts](geometry-concepts.md) - Mathematical background