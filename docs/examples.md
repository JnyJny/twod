# Examples

This page contains practical examples showing how to use twod for common geometric tasks.

## Basic Point Operations

### Creating and Manipulating Points

```python
from twod import Point

# Different ways to create points
origin = Point()                    # Point(0, 0)
p1 = Point(3, 4)                   # Point(3, 4)
p2 = Point(x=10, y=20)             # Point(10, 20)
p3 = Point((5, 6))                 # From tuple
p4 = Point([7, 8])                 # From list

# Point arithmetic
result = p1 + p2                   # Point(13, 24)
difference = p2 - p1               # Point(7, 16)
scaled = p1 * 2                    # Point(6, 8)
halved = p1 / 2                    # Point(1.5, 2.0)
```

### Distance and Angle Calculations

```python
from twod import Point
import math

p1 = Point(0, 0)
p2 = Point(3, 4)

# Distance calculations
distance = p1.distance(p2)         # 5.0
dist_squared = p1.distance_squared(p2)  # 25.0 (faster)

# Polar coordinates
radius = p2.radius                 # 5.0
angle_rad = p2.radians             # 0.9272952180016122
angle_deg = p2.degrees             # 53.13010235415598

# Create point from polar coordinates
polar_point = Point.from_polar(5, math.pi/4)  # Point(3.535..., 3.535...)
```

## Working with Rectangles

### Rectangle Creation and Properties

```python
from twod import Point, Rect

# Create rectangle from corners
bottom_left = Point(10, 10)
top_right = Point(50, 30)
rect = Rect(bottom_left, top_right)

# Rectangle properties
print(f"Width: {rect.width}")         # Width: 40
print(f"Height: {rect.height}")       # Height: 20
print(f"Area: {rect.area}")           # Area: 800
print(f"Center: {rect.center}")       # Center: Point(30, 20)

# Corner access
print(f"Bottom-left: {rect.bottom_left}")
print(f"Top-right: {rect.top_right}")
print(f"Top-left: {rect.top_left}")
print(f"Bottom-right: {rect.bottom_right}")
```

### Rectangle Operations

```python
from twod import Point, Rect

rect = Rect(Point(0, 0), Point(10, 10))

# Move rectangle
moved = rect + Point(5, 5)         # Moves to (5,5)-(15,15)

# Scale rectangle
scaled = rect * 2                  # Scales to (0,0)-(20,20)

# Check if point is inside
test_point = Point(5, 5)
inside = test_point.inside(rect.bottom_left, rect.top_right)  # True

# Check if rectangles overlap
rect2 = Rect(Point(5, 5), Point(15, 15))
# Would need to implement overlap check manually or use spatial relationships
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
print(f"Length: {line.length}")           # Length: 10.0
print(f"Angle: {line.angle_degrees}")     # Angle: 53.13010235415598
print(f"Slope: {line.slope}")             # Slope: 1.3333333333333333
print(f"Midpoint: {line.midpoint}")       # Midpoint: Point(3, 4)

# Direction and vector
print(f"Direction: {line.direction}")     # Unit vector
print(f"Vector: {line.vector}")           # Vector from start to end
```

### Line Intersections

```python
from twod import Point, Line

# Create two intersecting lines
line1 = Line(Point(0, 0), Point(4, 4))    # Diagonal line
line2 = Line(Point(0, 4), Point(4, 0))    # Opposite diagonal

# Find intersection
intersection = line1.intersection_point(line2)
print(f"Intersection: {intersection}")     # Point(2, 2)

# Check if lines intersect
intersects = line1.intersects_line(line2)  # True

# Parallel lines don't intersect
line3 = Line(Point(0, 1), Point(4, 5))    # Parallel to line1
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
dist2 = line.distance_to_point(point_above)    # 3.0
dist3 = line.distance_to_point(point_below)    # 2.0

# Find closest point on line
closest = line.closest_point_on_line(point_above)  # Point(5, 0)
```

## Complex Number Points

### Using CPoint for Performance

```python
from twod import CPoint

# Create from complex number
cp1 = CPoint(3+4j)
cp2 = CPoint(1+2j)

# Arithmetic operations (leverages complex number efficiency)
sum_cp = cp1 + cp2                 # CPoint(4+6j)
diff_cp = cp1 - cp2                # CPoint(2+2j)
product = cp1 * cp2                # Complex multiplication

# Polar operations are very efficient
radius = cp1.radius                # 5.0
angle = cp1.radians                # 0.9272952180016122

# Create from polar coordinates
polar_cp = CPoint.from_polar(5, 1.57)  # Approximately 5j
```

### Flexible CPoint Construction

```python
from twod import CPoint

# Various ways to create CPoint
cp1 = CPoint.from_any(3+4j)           # From complex
cp2 = CPoint.from_any((3, 4))         # From tuple
cp3 = CPoint.from_any([3, 4])         # From list
cp4 = CPoint.from_any({"x": 3, "y": 4})  # From dict
cp5 = CPoint.from_any("3+4j")         # From string
cp6 = CPoint.from_any(5)              # From scalar (5+0j)

# All create equivalent points
assert cp1 == cp2 == cp3 == cp4 == cp5
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
    ccw = p1.is_ccw(p2, p4)         # True
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
points = [
    Point(10, 5),
    Point(20, 15),
    Point(5, 10),
    Point(15, 8),
    Point(12, 20)
]

# Find bounding box
min_x = min(p.x for p in points)  # 5
max_x = max(p.x for p in points)  # 20
min_y = min(p.y for p in points)  # 5
max_y = max(p.y for p in points)  # 20

bounding_box = Rect(Point(min_x, min_y), Point(max_x, max_y))
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
    Point(0, 0)  # Close the polygon
]

# Calculate perimeter
perimeter = sum(
    vertices[i].distance(vertices[i+1]) 
    for i in range(len(vertices)-1)
)
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

### When to Use CPoint vs Point

```python
from twod import Point, CPoint
import time

# For simple operations, both are similar
p1 = Point(3, 4)
cp1 = CPoint(3+4j)

# For complex rotations, CPoint is more efficient
def rotate_point_traditional(point, angle):
    """Rotate using traditional trigonometry."""
    import math
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    return Point(
        point.x * cos_a - point.y * sin_a,
        point.x * sin_a + point.y * cos_a
    )

def rotate_cpoint(cpoint, angle):
    """Rotate using complex number multiplication."""
    import cmath
    rotation = cmath.exp(1j * angle)
    return cpoint * CPoint(rotation)

# CPoint rotation is typically faster for repeated operations
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