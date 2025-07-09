# Geometry Concepts

This page explains the mathematical concepts and geometric principles underlying twod's design and functionality.

## Coordinate Systems

### Cartesian Coordinates

twod uses the standard Cartesian coordinate system where:
- **x-axis**: Horizontal axis (positive goes right)
- **y-axis**: Vertical axis (positive goes up)
- **Origin**: Point (0, 0) where axes intersect

```python
from twod import Point

origin = Point(0, 0)
right = Point(1, 0)    # 1 unit right
up = Point(0, 1)       # 1 unit up
diagonal = Point(1, 1) # 1 unit right and up
```

### Polar Coordinates

Points can also be represented in polar form using:
- **Radius (r)**: Distance from origin
- **Angle (θ)**: Angle from positive x-axis (counter-clockwise)

```python
from twod import Point
import math

# Create point from polar coordinates
radius = 5
angle = math.pi / 4  # 45 degrees
point = Point.from_polar(radius, angle)
print(f"Point: {point}")  # Point(3.535..., 3.535...)

# Convert Cartesian to polar
p = Point(3, 4)
print(f"Radius: {p.radius}")  # 5.0
print(f"Angle: {p.radians}")  # 0.9272952180016122
```

## Distance Calculations

### Euclidean Distance

The distance between two points \\((x_1, y_1)\\) and \\((x_2, y_2)\\) is:

\\[d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}\\]

```python
from twod import Point

p1 = Point(0, 0)
p2 = Point(3, 4)
distance = p1.distance(p2)  # 5.0
```

### Distance Squared

For performance, when you only need relative distances, use squared distance:

\\[d^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2\\]

```python
from twod import Point

p1 = Point(0, 0)
p2 = Point(3, 4)
dist_squared = p1.distance_squared(p2)  # 25.0 (faster than distance)
```

## Vector Operations

### Dot Product

The dot product of two vectors **a** = (a₁, a₂) and **b** = (b₁, b₂) is:

\\[\mathbf{a} \cdot \mathbf{b} = a_1 b_1 + a_2 b_2\\]

The dot product has important geometric properties:
- **Perpendicular vectors**: dot product = 0
- **Parallel vectors**: dot product = ±|a||b|
- **Angle between vectors**: \\(\cos \theta = \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}||\mathbf{b}|}\\)

```python
from twod import Point

a = Point(3, 4)
b = Point(1, 2)
dot_product = a.dot(b)  # 3*1 + 4*2 = 11

# Check if vectors are perpendicular
perpendicular = Point(1, 0)
vertical = Point(0, 1)
print(perpendicular.dot(vertical))  # 0 (perpendicular)
```

### Cross Product (2D)

In 2D, the cross product gives a scalar representing the z-component of the 3D cross product:

\\[\mathbf{a} \times \mathbf{b} = a_1 b_2 - a_2 b_1\\]

This is useful for:
- **Orientation**: positive = counter-clockwise, negative = clockwise, zero = collinear
- **Area calculation**: |cross product| = 2 × area of triangle

```python
from twod import Point

a = Point(1, 0)
b = Point(0, 1)
cross = a.cross(b)  # 1*1 - 0*0 = 1 (counter-clockwise)

# Check orientation
p1 = Point(0, 0)
p2 = Point(1, 0)
p3 = Point(1, 1)
orientation = p1.ccw(p2, p3)  # > 0 (counter-clockwise)
```

## Line Geometry

### Line Representation

Lines in twod are represented as line segments with start and end points. Key properties:

- **Length**: Distance between endpoints
- **Direction**: Unit vector from start to end
- **Slope**: Rise over run (dy/dx)
- **Angle**: Angle from positive x-axis

```python
from twod import Point, Line

line = Line(Point(0, 0), Point(3, 4))
print(f"Length: {line.length}")         # 5.0
print(f"Direction: {line.direction}")   # Unit vector (0.6, 0.8)
print(f"Slope: {line.slope}")           # 4/3 ≈ 1.333
print(f"Angle: {line.angle_degrees}")   # ~53.13°
```

### Line Intersection

Two lines intersect if their direction vectors are not parallel. The intersection point can be found using parametric equations:

- **Line 1**: P₁ + t₁(P₂ - P₁)
- **Line 2**: P₃ + t₂(P₄ - P₃)

```python
from twod import Point, Line

line1 = Line(Point(0, 0), Point(2, 2))
line2 = Line(Point(0, 2), Point(2, 0))
intersection = line1.intersection_point(line2)  # Point(1, 1)
```

### Distance from Point to Line

The shortest distance from a point to a line segment involves:
1. Project the point onto the infinite line
2. Clamp the projection to the line segment
3. Calculate distance to the clamped point

```python
from twod import Point, Line

line = Line(Point(0, 0), Point(10, 0))  # Horizontal line
point = Point(5, 3)
distance = line.distance_to_point(point)  # 3.0
closest = line.closest_point_on_line(point)  # Point(5, 0)
```

## Angle Calculations

### Angle Between Vectors

The angle between two vectors is found using the dot product:

\\[\theta = \arccos\left(\frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}||\mathbf{b}|}\right)\\]

```python
from twod import Point, Line
import math

line1 = Line(Point(0, 0), Point(1, 0))  # Horizontal
line2 = Line(Point(0, 0), Point(1, 1))  # 45° diagonal

angle_rad = line1.angle_between(line2)  # π/4 radians
angle_deg = angle_rad * 180 / math.pi   # 45 degrees
```

### Angle Normalization

Angles in twod are typically normalized to:
- **Radians**: [0, 2π) or [-π, π)
- **Degrees**: [0, 360°) or [-180°, 180°)

## Complex Number Geometry

### Complex Numbers as Points

Complex numbers provide an elegant way to represent 2D points:
- **Real part**: x-coordinate
- **Imaginary part**: y-coordinate
- **Magnitude**: Distance from origin
- **Argument**: Angle from positive x-axis

```python
from twod import CPoint

# Complex number 3+4j represents point (3, 4)
cp = CPoint(3+4j)
print(f"X: {cp.x}")        # 3.0
print(f"Y: {cp.y}")        # 4.0
print(f"Radius: {cp.radius}")  # 5.0
print(f"Angle: {cp.radians}")  # 0.9272952180016122
```

### Complex Arithmetic

Complex number arithmetic naturally represents geometric operations:
- **Addition**: Translation
- **Multiplication by real**: Scaling
- **Multiplication by complex**: Rotation and scaling

```python
from twod import CPoint
import cmath

# Translation
cp1 = CPoint(1+2j)
cp2 = CPoint(3+4j)
translated = cp1 + cp2  # CPoint(4+6j)

# Rotation by 90° (multiply by i)
rotated = cp1 * CPoint(1j)  # CPoint(-2+1j)

# Rotation by arbitrary angle
angle = 0.5  # radians
rotation = cmath.exp(1j * angle)
rotated = cp1 * CPoint(rotation)
```

## Geometric Relationships

### Collinearity

Three points are collinear if they lie on the same line. This can be tested using the cross product:

```python
from twod import Point

p1 = Point(0, 0)
p2 = Point(1, 1)
p3 = Point(2, 2)

# Points are collinear if cross product is zero
collinear = p1.is_colinear(p2, p3)  # True
```

### Orientation

The orientation of three points can be:
- **Counter-clockwise**: Cross product > 0
- **Clockwise**: Cross product < 0
- **Collinear**: Cross product = 0

```python
from twod import Point

p1 = Point(0, 0)
p2 = Point(1, 0)
p3 = Point(1, 1)

ccw_test = p1.ccw(p2, p3)  # > 0 (counter-clockwise)
is_ccw = p1.is_ccw(p2, p3)  # True
```

### Point in Rectangle

A point is inside a rectangle if:
- x-coordinate is between left and right bounds
- y-coordinate is between bottom and top bounds

```python
from twod import Point, Rect

rect = Rect(Point(0, 0), Point(10, 10))
test_point = Point(5, 5)

# Check if point is inside
inside = test_point.inside(rect.bottom_left, rect.top_right)  # True
```

## Performance Considerations

### Squared Distance vs Distance

When comparing distances, use squared distance to avoid expensive square root calculation:

```python
from twod import Point

points = [Point(1, 1), Point(2, 2), Point(3, 3)]
origin = Point(0, 0)

# Efficient: compare squared distances
closest = min(points, key=lambda p: origin.distance_squared(p))

# Less efficient: compare actual distances
# closest = min(points, key=lambda p: origin.distance(p))
```

### Complex vs Float Operations

Complex number operations can be more efficient for:
- Rotations
- Polar coordinate conversions
- Repeated geometric transformations

```python
from twod import Point, CPoint

# Traditional rotation (slower)
def rotate_point(point, angle):
    import math
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    return Point(
        point.x * cos_a - point.y * sin_a,
        point.x * sin_a + point.y * cos_a
    )

# Complex rotation (faster)
def rotate_cpoint(cpoint, angle):
    import cmath
    return cpoint * CPoint(cmath.exp(1j * angle))
```

## Numerical Precision

### Floating Point Considerations

When working with floating-point numbers, be aware of:
- **Precision limits**: Not all decimal numbers can be represented exactly
- **Comparison tolerance**: Use tolerance for equality checks
- **Accumulated errors**: Errors can accumulate in long calculations

```python
from twod import Point

# Floating point precision issues
p1 = Point(0.1, 0.2)
p2 = Point(0.3, 0.0)
sum_point = p1 + p2  # May not be exactly Point(0.4, 0.2)

# Use tolerance for comparisons
def points_equal(p1, p2, tolerance=1e-10):
    return p1.distance(p2) <= tolerance
```

### Tolerance in Geometric Operations

Many geometric operations in twod use tolerance for robust comparisons:

```python
from twod import Point, Line

line = Line(Point(0, 0), Point(10, 0))
point = Point(5, 1e-12)  # Very close to line

# Contains point uses tolerance
contains = line.contains_point(point)  # True (within default tolerance)
contains_strict = line.contains_point(point, tolerance=1e-15)  # False
```

Understanding these concepts will help you use twod effectively and write robust geometric code.