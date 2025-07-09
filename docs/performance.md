# Performance Guide

This guide explains when to use different twod implementations and how to optimize performance for your specific use case.

## Implementation Comparison

twod provides two main implementation approaches:

### Traditional Float-Based Classes
- **Classes**: `Point`, `Rect`
- **Storage**: Separate x, y float attributes
- **Best for**: General use, educational purposes, direct coordinate access
- **Memory**: Slightly more memory per object due to separate attributes

### Complex Number-Based Classes  
- **Classes**: `CPoint`, `CRect`
- **Storage**: Single complex number (x + yj)
- **Best for**: Performance-critical applications, rotations, polar operations
- **Memory**: More compact storage, single complex number

## Performance Benchmarks

### Basic Operations

```python
import time
from twod import Point, CPoint

# Test data
n = 100000
points_data = [(i, i+1) for i in range(n)]

# Point creation
start = time.time()
points = [Point(x, y) for x, y in points_data]
point_time = time.time() - start

start = time.time()
cpoints = [CPoint(x + y*1j) for x, y in points_data]
cpoint_time = time.time() - start

print(f"Point creation: {point_time:.3f}s")
print(f"CPoint creation: {cpoint_time:.3f}s")
```

### Distance Calculations

```python
import time
from twod import Point, CPoint

# Create test points
p1 = Point(0, 0)
p2 = Point(3, 4)
cp1 = CPoint(0+0j)
cp2 = CPoint(3+4j)

# Distance calculation benchmark
n = 1000000

start = time.time()
for _ in range(n):
    dist = p1.distance(p2)
point_dist_time = time.time() - start

start = time.time()
for _ in range(n):
    dist = cp1.distance(cp2)
cpoint_dist_time = time.time() - start

print(f"Point distance: {point_dist_time:.3f}s")
print(f"CPoint distance: {cpoint_dist_time:.3f}s")
```

### Rotations

This is where complex numbers really shine:

```python
import time
import math
from twod import Point, CPoint

def rotate_point_traditional(point, angle):
    """Traditional rotation using trigonometry."""
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    return Point(
        point.x * cos_a - point.y * sin_a,
        point.x * sin_a + point.y * cos_a
    )

def rotate_cpoint_complex(cpoint, angle):
    """Rotation using complex number multiplication."""
    import cmath
    rotation = cmath.exp(1j * angle)
    return cpoint * CPoint(rotation)

# Benchmark rotations
point = Point(3, 4)
cpoint = CPoint(3+4j)
angle = math.pi / 4  # 45 degrees
n = 100000

start = time.time()
for _ in range(n):
    rotated = rotate_point_traditional(point, angle)
traditional_time = time.time() - start

start = time.time()
for _ in range(n):
    rotated = rotate_cpoint_complex(cpoint, angle)
complex_time = time.time() - start

print(f"Traditional rotation: {traditional_time:.3f}s")
print(f"Complex rotation: {complex_time:.3f}s")
print(f"Speedup: {traditional_time/complex_time:.1f}x")
```

## When to Use Each Implementation

### Use Point/Rect When:

1. **Direct coordinate access is important**
   ```python
   from twod import Point
   
   p = Point(3, 4)
   # Direct access to coordinates
   x_coord = p.x
   y_coord = p.y
   ```

2. **Educational or learning contexts**
   ```python
   # Clear, intuitive representation
   point = Point(3, 4)
   print(f"Point at ({point.x}, {point.y})")
   ```

3. **Integration with existing float-based code**
   ```python
   # Works naturally with existing functions expecting x, y
   def process_coordinates(x, y):
       return x * 2 + y
   
   point = Point(3, 4)
   result = process_coordinates(point.x, point.y)
   ```

4. **Simple geometric calculations**
   ```python
   from twod import Point
   
   # Simple distance calculation
   p1 = Point(0, 0)
   p2 = Point(3, 4)
   distance = p1.distance(p2)  # Clear and straightforward
   ```

### Use CPoint/CRect When:

1. **Performance is critical**
   ```python
   from twod import CPoint
   
   # Faster operations, especially for large datasets
   points = [CPoint(x+y*1j) for x, y in large_dataset]
   ```

2. **Frequent rotations or polar operations**
   ```python
   from twod import CPoint
   import cmath
   
   # Efficient rotation
   point = CPoint(3+4j)
   rotated = point * CPoint(cmath.exp(1j * angle))
   ```

3. **Working with complex mathematical operations**
   ```python
   from twod import CPoint
   
   # Natural complex number operations
   z1 = CPoint(3+4j)
   z2 = CPoint(1+2j)
   product = z1 * z2  # Natural complex multiplication
   ```

4. **Memory optimization**
   ```python
   # More compact storage for large point collections
   points = [CPoint(x+y*1j) for x, y in range(1000000)]
   ```

## Optimization Strategies

### 1. Use Squared Distance When Possible

```python
from twod import Point

# When you only need relative distances
points = [Point(i, i) for i in range(100)]
origin = Point(0, 0)

# Efficient: compare squared distances (no sqrt)
closest = min(points, key=lambda p: origin.distance_squared(p))

# Less efficient: compare actual distances
# closest = min(points, key=lambda p: origin.distance(p))
```

### 2. Batch Operations

```python
from twod import Point

# Process multiple points efficiently
points = [Point(i, i) for i in range(1000)]
translation = Point(10, 10)

# Efficient batch translation
translated = [p + translation for p in points]
```

### 3. Pre-calculate Expensive Operations

```python
from twod import Point
import math

# Pre-calculate trigonometric values for repeated rotations
angle = math.pi / 4
cos_angle = math.cos(angle)
sin_angle = math.sin(angle)

def rotate_point_optimized(point, cos_a, sin_a):
    return Point(
        point.x * cos_a - point.y * sin_a,
        point.x * sin_a + point.y * cos_a
    )

# Use pre-calculated values
points = [Point(i, i) for i in range(100)]
rotated = [rotate_point_optimized(p, cos_angle, sin_angle) for p in points]
```

### 4. Choose Appropriate Data Structures

```python
from twod import Point

# For spatial queries, consider using spatial data structures
# This is a simple example - real applications might use KD-trees or R-trees

def find_nearby_points(target, points, radius):
    """Find points within radius of target."""
    radius_squared = radius * radius
    return [p for p in points if target.distance_squared(p) <= radius_squared]

# Use squared distance for efficiency
target = Point(0, 0)
points = [Point(i, j) for i in range(10) for j in range(10)]
nearby = find_nearby_points(target, points, 5)
```

### 5. Vectorize Operations When Possible

```python
from twod import Point
import numpy as np

# For very large datasets, consider NumPy for vectorized operations
def vectorized_distance(points1, points2):
    """Calculate distances between corresponding points using NumPy."""
    p1_array = np.array([(p.x, p.y) for p in points1])
    p2_array = np.array([(p.x, p.y) for p in points2])
    diff = p1_array - p2_array
    return np.sqrt(np.sum(diff * diff, axis=1))

# For very large datasets, this can be much faster
points1 = [Point(i, i) for i in range(10000)]
points2 = [Point(i+1, i+1) for i in range(10000)]
distances = vectorized_distance(points1, points2)
```

## Memory Usage

### Memory Footprint Comparison

```python
import sys
from twod import Point, CPoint

# Memory usage per object
point = Point(3, 4)
cpoint = CPoint(3+4j)

print(f"Point size: {sys.getsizeof(point)} bytes")
print(f"CPoint size: {sys.getsizeof(cpoint)} bytes")

# For large collections, this difference matters
n = 100000
points = [Point(i, i) for i in range(n)]
cpoints = [CPoint(i+i*1j) for i in range(n)]

# Measure total memory usage
import tracemalloc
tracemalloc.start()

# Create point collection
point_collection = [Point(i, i) for i in range(n)]
current, peak = tracemalloc.get_traced_memory()
point_memory = current

tracemalloc.clear_traces()

# Create cpoint collection
cpoint_collection = [CPoint(i+i*1j) for i in range(n)]
current, peak = tracemalloc.get_traced_memory()
cpoint_memory = current

print(f"Memory for {n} Points: {point_memory / 1024 / 1024:.2f} MB")
print(f"Memory for {n} CPoints: {cpoint_memory / 1024 / 1024:.2f} MB")
```

### Memory-Efficient Patterns

```python
from twod import CPoint

# Use generators for large datasets
def generate_points(n):
    """Generate points on demand."""
    for i in range(n):
        yield CPoint(i + i*1j)

# Process points without storing all in memory
total_distance = 0
origin = CPoint(0)
for point in generate_points(1000000):
    total_distance += origin.distance(point)
    # Point is garbage collected after use
```

## Profiling and Measurement

### Basic Timing

```python
import time
from twod import Point, CPoint

def time_operation(operation, n=100000):
    """Time an operation n times."""
    start = time.time()
    for _ in range(n):
        operation()
    return time.time() - start

# Compare point creation
point_time = time_operation(lambda: Point(3, 4))
cpoint_time = time_operation(lambda: CPoint(3+4j))

print(f"Point creation: {point_time:.3f}s")
print(f"CPoint creation: {cpoint_time:.3f}s")
```

### Using timeit for Accurate Measurements

```python
import timeit
from twod import Point, CPoint

# More accurate timing with timeit
setup = """
from twod import Point, CPoint
p1 = Point(0, 0)
p2 = Point(3, 4)
cp1 = CPoint(0)
cp2 = CPoint(3+4j)
"""

point_time = timeit.timeit('p1.distance(p2)', setup=setup, number=100000)
cpoint_time = timeit.timeit('cp1.distance(cp2)', setup=setup, number=100000)

print(f"Point distance: {point_time:.3f}s")
print(f"CPoint distance: {cpoint_time:.3f}s")
```

## Best Practices

### 1. Choose the Right Implementation

- **Point/Rect**: For general use, learning, direct coordinate access
- **CPoint/CRect**: For performance-critical applications, rotations, large datasets

### 2. Measure Performance

- Profile your specific use case
- Use appropriate timing tools
- Consider memory usage for large datasets

### 3. Optimize Appropriately

- Use squared distance when possible
- Pre-calculate expensive operations
- Consider vectorized operations for very large datasets
- Use generators for memory efficiency

### 4. Consider Trade-offs

- **Readability vs Performance**: Sometimes Point is clearer even if CPoint is faster
- **Memory vs Speed**: CPoint uses less memory but may be less intuitive
- **Complexity vs Optimization**: Don't optimize prematurely - measure first

### 5. Real-world Example

```python
from twod import Point, CPoint
import time

class ParticleSystem:
    """Example showing when to choose different implementations."""
    
    def __init__(self, use_complex=False):
        self.use_complex = use_complex
        self.particles = []
        
    def add_particle(self, x, y):
        if self.use_complex:
            self.particles.append(CPoint(x + y*1j))
        else:
            self.particles.append(Point(x, y))
    
    def update(self, dt):
        """Update particle positions - this is called frequently."""
        if self.use_complex:
            # Complex number operations are faster for rotations
            import cmath
            rotation = cmath.exp(1j * dt)
            self.particles = [p * CPoint(rotation) for p in self.particles]
        else:
            # Traditional approach
            import math
            cos_dt = math.cos(dt)
            sin_dt = math.sin(dt)
            new_particles = []
            for p in self.particles:
                new_x = p.x * cos_dt - p.y * sin_dt
                new_y = p.x * sin_dt + p.y * cos_dt
                new_particles.append(Point(new_x, new_y))
            self.particles = new_particles

# Benchmark particle systems
traditional = ParticleSystem(use_complex=False)
complex_system = ParticleSystem(use_complex=True)

# Add particles
for i in range(1000):
    traditional.add_particle(i, i)
    complex_system.add_particle(i, i)

# Time updates
start = time.time()
for _ in range(100):
    traditional.update(0.1)
traditional_time = time.time() - start

start = time.time()
for _ in range(100):
    complex_system.update(0.1)
complex_time = time.time() - start

print(f"Traditional system: {traditional_time:.3f}s")
print(f"Complex system: {complex_time:.3f}s")
print(f"Speedup: {traditional_time/complex_time:.1f}x")
```

This example shows how complex number-based operations can significantly improve performance for applications involving rotations and transformations.

By understanding these performance characteristics, you can make informed decisions about which twod implementation to use for your specific needs.