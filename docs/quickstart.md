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
print(f"P1: {p1}")         # P1: Point(3, 4)
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
e = a * 2    # Point(2, 4)
f = b / 2    # Point(1.5, 2.0)

# Dot product and cross product
dot = a.dot(b)    # 11 (1*3 + 2*4)
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

## Complex Number Points

For performance-critical applications, use `CPoint` which leverages Python's complex number type:

```python
from twod import CPoint

# Create from complex number
cp1 = CPoint(3+4j)
cp2 = CPoint.from_any((5, 6))  # Flexible constructor

# Same operations as Point
distance = cp1.distance(cp2)
midpoint = cp1.midpoint(cp2)

# Polar operations (efficient with complex numbers)
polar_point = CPoint.from_polar(5, 0.927)  # radius=5, angle=0.927 radians
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
print(f"Width: {rect.width}")    # Width: 10
print(f"Height: {rect.height}")  # Height: 20
print(f"Area: {rect.area}")      # Area: 200
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
scaled_rect = rect * 2           # Scales rectangle by 2
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
print(f"Length: {line.length}")           # Length: 5.0
print(f"Angle: {line.angle_degrees}")     # Angle: 53.13010235415598
print(f"Midpoint: {line.midpoint}")       # Midpoint: Point(1.5, 2.0)
print(f"Slope: {line.slope}")             # Slope: 1.3333333333333333
```

### Line Operations

```python
from twod import Point, Line

line1 = Line(Point(0, 0), Point(2, 2))
line2 = Line(Point(0, 2), Point(2, 0))

# Intersection
intersection = line1.intersection_point(line2)  # Point(1, 1)
intersects = line1.intersects_line(line2)       # True

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
from twod import Point, Ellipse

# Create ellipse
center = Point(0, 0)
ellipse = Ellipse(center, semi_major_axis=5, semi_minor_axis=3)

# Properties
print(f"Area: {ellipse.area}")           # Area: 47.12388980384689
print(f"Perimeter: {ellipse.perimeter}") # Approximate perimeter
print(f"Eccentricity: {ellipse.eccentricity}")  # 0.8
```

## Choosing Between Implementations

### Traditional Float-Based Classes
- **Use when**: You need familiar x, y coordinate access
- **Classes**: `Point`, `Rect`
- **Best for**: General geometric calculations, educational purposes

```python
from twod import Point, Rect

point = Point(3, 4)
print(f"X: {point.x}, Y: {point.y}")  # Direct coordinate access
```

### Complex Number-Based Classes
- **Use when**: You need performance or work with rotations/polar coordinates
- **Classes**: `CPoint`, `CRect`
- **Best for**: Performance-critical applications, complex geometric transformations

```python
from twod import CPoint

point = CPoint(3+4j)
print(f"Radius: {point.radius}")       # Efficient polar coordinates
rotated = point * (1+1j)               # Efficient rotation
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
angle_deg = angle_rad * 180 / 3.14159   # ~45 degrees
```

## Next Steps

Now that you understand the basics, explore:

- [Examples](examples.md) - More detailed usage examples
- [API Reference](api/index.md) - Complete method documentation
- [Performance Guide](performance.md) - When to use different implementations
- [Geometry Concepts](geometry-concepts.md) - Mathematical background