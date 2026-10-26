# Examples

This page contains practical examples showing how to use twod for common geometric tasks.

## Basic Point Operations

### Creating and Manipulating Points

```python
from twod import Point

# Different ways to create points
origin = Point()  # Point(0, 0)
p1 = Point(3, 4)  # Point(3, 4)
p2 = Point(x=10, y=20)  # Point(10, 20)
p3 = Point.from_any((5, 6))  # From tuple
p4 = Point.from_any([7, 8])  # From list

# Point arithmetic
result = p1 + p2  # Point(13, 24)
difference = p2 - p1  # Point(7, 16)
scaled = p1 * 2  # Point(6, 8)
halved = p1 / 2  # Point(1.5, 2.0)
```

### Distance and Angle Calculations

```python
from twod import Point
import math

p1 = Point(0, 0)
p2 = Point(3, 4)

# Distance calculations
distance = p1.distance(p2)  # 5.0
dist_squared = p1.distance_squared(p2)  # 25.0 (faster)

# Polar coordinates
radius = p2.radius  # 5.0
angle_rad = p2.radians  # 0.9272952180016122
angle_deg = p2.degrees  # 53.13010235415598

# Create point from polar coordinates
polar_point = Point.from_polar(5, math.pi / 4)  # Point(3.535..., 3.535...)
```

## Working with Rectangles

### Rectangle Creation and Properties

```python
from twod import Rect

# Origin (x, y) and dimensions (w, h)
rect = Rect(10, 10, 40, 20)

# Rectangle properties
print(f"Width: {rect.w}")  # Width: 40
print(f"Height: {rect.h}")  # Height: 20
print(f"Area: {rect.area}")  # Area: 800
print(f"Center: {rect.center}")  # Center: Point(x=30.0, y=20.0)

# Corner access: A is (x, y), then B, C and D around the rectangle
print(f"A: {rect.A}")  # A: Point(x=10, y=10)
print(f"B: {rect.B}")  # B: Point(x=50, y=10)
print(f"C: {rect.C}")  # C: Point(x=50, y=30)
print(f"D: {rect.D}")  # D: Point(x=10, y=30)
```

### Rectangle Operations

```python
from twod import Point, Rect

rect = Rect(0, 0, 10, 10)

# Move rectangle
moved = rect + Point(5, 5)  # Rect(x=5, y=5, w=10, h=10)

# Check if point is inside
test_point = Point(5, 5)
inside = test_point in rect  # True

# Check if rectangles overlap
rect2 = Rect(5, 5, 10, 10)
overlap = rect.intersects(rect2)  # True

# Check if one rectangle is entirely inside another
contained = Rect(2, 2, 3, 3) in rect  # True
```

## Line Geometry

### Line Creation and Properties

```python
from twod import Point, Line

# Create line from two points
start = Point(0, 0)
end = Point(6, 8)
line = Line(start, end)

# Line properties
print(f"Length: {line.length}")  # Length: 10.0
print(f"Angle: {line.angle_degrees}")  # Angle: 53.13010235415598
print(f"Slope: {line.slope}")  # Slope: 1.3333333333333333
print(f"Midpoint: {line.midpoint}")  # Midpoint: Point(3, 4)

# Direction and vector
print(f"Direction: {line.direction}")  # Unit vector
print(f"Vector: {line.vector}")  # Vector from start to end
```

### Line Intersections

```python
from twod import Point, Line

# Create two intersecting lines
line1 = Line(Point(0, 0), Point(4, 4))  # Diagonal line
line2 = Line(Point(0, 4), Point(4, 0))  # Opposite diagonal

# Find intersection
intersection = line1.intersection_point(line2)
print(f"Intersection: {intersection}")  # Point(2, 2)

# Check if lines intersect
intersects = line1.intersects_line(line2)  # True

# Parallel lines don't intersect
line3 = Line(Point(0, 1), Point(4, 5))  # Parallel to line1
no_intersection = line1.intersection_point(line3)  # None
```

### Distance from Point to Line

```python
from twod import Point, Line

# Horizontal line
line = Line(Point(0, 0), Point(10, 0))

# Points at various positions
point_on_line = Point(5, 0)
point_above = Point(5, 3)
point_below = Point(5, -2)

# Calculate distances
dist1 = line.distance_to_point(point_on_line)  # 0.0
dist2 = line.distance_to_point(point_above)  # 3.0
dist3 = line.distance_to_point(point_below)  # 2.0

# Find closest point on line
closest = line.closest_point_on_line(point_above)  # Point(5, 0)
```

## Flexible Input

### Tuples and Lists

```python
from twod import Point

p = Point(3, 4)

# Geometry methods accept (x, y) sequences
p.distance((0, 0))  # 5.0
p.midpoint([5, 6])  # Point(x=4.0, y=5.0)
p.between((0, 0), (10, 10))  # True
```

### Building Points with from_any

```python
from twod import Point

p1 = Point.from_any(3 + 4j)  # From complex
p2 = Point.from_any((3, 4))  # From tuple
p3 = Point.from_any([3, 4])  # From list
p4 = Point.from_any({"x": 3, "y": 4})  # From dict
p5 = Point.from_any("3+4j")  # From string
p6 = Point.from_any(5)  # From scalar: Point(5, 5)

assert p1 == p2 == p3 == p4 == p5
```

### Rotation and Scaling

```python
from twod import Point

p = Point(1, 0)
p.rotate(90, is_degrees=True)  # about the origin, in place
q = p.rotate(180, origin=(1, 1), is_degrees=True, inplace=False)  # new Point
p.scale(2)  # in place
```

## Geometric Relationships

### Collinearity and Orientation

```python
from twod import Point, ColinearPoints

# Check if three points are collinear
p1 = Point(0, 0)
p2 = Point(1, 1)
p3 = Point(2, 2)

collinear = p1.is_colinear(p2, p3)  # True

# Check counter-clockwise orientation
p4 = Point(1, 2)
try:
    ccw = p1.is_ccw(p2, p4)  # True
except ColinearPoints:
    print("Points are collinear")
```

### Line Relationships

```python
from twod import Point, Line

# Create various lines
horizontal = Line(Point(0, 0), Point(5, 0))
vertical = Line(Point(0, 0), Point(0, 5))
diagonal = Line(Point(0, 0), Point(3, 4))

# Check relationships
perpendicular = horizontal.perpendicular_to(vertical)  # True
parallel = horizontal.parallel_to(Line(Point(0, 1), Point(5, 1)))  # True

# Calculate angles between lines
angle = horizontal.angle_between(diagonal)  # In radians
```

## Practical Applications

### Bounding Box Calculation

```python
from twod import Point, Rect

# Set of points
points = [Point(10, 5), Point(20, 15), Point(5, 10), Point(15, 8), Point(12, 20)]

# Find bounding box
min_x = min(p.x for p in points)  # 5
max_x = max(p.x for p in points)  # 20
min_y = min(p.y for p in points)  # 5
max_y = max(p.y for p in points)  # 20

bounding_box = Rect(min_x, min_y, max_x - min_x, max_y - min_y)
print(f"Bounding box: {bounding_box}")
```

### Polygon Perimeter

```python
from twod import Point

# Simple polygon (triangle)
vertices = [
    Point(0, 0),
    Point(3, 0),
    Point(1.5, 2.6),
    Point(0, 0),  # Close the polygon
]

# Calculate perimeter
perimeter = sum(vertices[i].distance(vertices[i + 1]) for i in range(len(vertices) - 1))
print(f"Perimeter: {perimeter}")
```

### Collision Detection

```python
from twod import Point, Line


def lines_intersect(line1, line2):
    """Check if two line segments intersect."""
    return line1.intersects_line(line2)


def point_in_circle(point, center, radius):
    """Check if point is inside circle."""
    return point.distance(center) <= radius


# Example usage
line1 = Line(Point(0, 0), Point(10, 10))
line2 = Line(Point(0, 10), Point(10, 0))

if lines_intersect(line1, line2):
    intersection = line1.intersection_point(line2)
    print(f"Lines intersect at: {intersection}")

# Point in circle
center = Point(5, 5)
test_point = Point(3, 4)
if point_in_circle(test_point, center, 3):
    print("Point is inside circle")
```

## Performance Considerations

### Rotating Many Points

```python
import math
from twod import Point

# Compute cos and sin once for repeated rotations by the same angle
angle = math.pi / 4
cos, sin = math.cos(angle), math.sin(angle)
points = [Point(i, i) for i in range(100)]
rotated = [Point(p.x * cos - p.y * sin, p.x * sin + p.y * cos) for p in points]
```

### Memory and Speed Tips

```python
from twod import Point

# Use distance_squared when you only need relative distances
points = [Point(i, i) for i in range(100)]
origin = Point(0, 0)

# Faster: compare squared distances
closest = min(points, key=lambda p: origin.distance_squared(p))

# Slower: compare actual distances
# closest = min(points, key=lambda p: origin.distance(p))
```

These examples demonstrate the core capabilities of twod. The library's consistent API makes it easy to work with geometric objects in an intuitive way.