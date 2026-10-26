# twod - A Two-Dimensional Geometry Library for Humans™

[![Test & Publish](https://github.com/JnyJny/twod/actions/workflows/release.yaml/badge.svg)](https://github.com/JnyJny/twod/actions/workflows/release.yaml)
![Version](https://img.shields.io/pypi/v/twod)
![Python Version](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FJnyJny%2Ftwod%2Fmaster%2Fpyproject.toml)
![License](https://img.shields.io/pypi/l/twod)
![Monthly Downloads](https://img.shields.io/pypi/dm/twod)

**twod** (pronounced "two dee") is a Python library that provides simple, intuitive two-dimensional geometric primitives designed for humans. It offers points, rectangles, lines, and ellipses with arithmetic operators and common geometric calculations.

## Features

- **Comprehensive Geometry**: Points, rectangles, lines, and ellipses with full geometric operations
- **Intuitive API**: Human-friendly method names and comprehensive docstrings
- **Flexible Input**: Geometry methods accept `Point`s or `(x, y)` tuples and lists
- **Rich Operations**: Full arithmetic operator support, geometric calculations, and spatial relationships

## Core Classes

### Point Classes
- **`Point`**: Mutable 2D point with arithmetic operators, polar coordinates, rotation, and geometric calculations

### Rectangle Classes  
- **`Rect`**: Rectangle with an origin and dimensions, containment, and overlap tests

### Additional Primitives
- **`Line`**: Line segment with geometric operations like intersections, distances, and relationships
- **`Ellipse`**: Ellipse with eccentricity, foci, vertices, co-vertices, and containment
- **`Circle`**: Circle with containment

### Deprecated
- `CPoint` and `CRect`, the complex number implementations, are deprecated and will be removed in 0.5.0. They were slower than `Point` and `Rect` and duplicated their API. `Point.from_any`, `Point.rotate` and `Point.scale` replace the useful parts.

## Quick Example

```python
from twod import Point, Rect, Line

# Create points
origin = Point(0, 0)
corner = Point(10, 10)

# Calculate distance
distance = origin.distance(corner)  # 14.142135623730951

# Create a rectangle from its origin (x, y) and dimensions (w, h)
rect = Rect(0, 0, 10, 10)
print(f"Area: {rect.area}")  # Area: 100

# Create a line
line = Line(origin, corner)
print(f"Length: {line.length}")  # Length: 14.142135623730951
print(f"Angle: {line.angle_degrees}")  # Angle: 45.0

# Check if point is inside rectangle
test_point = Point(5, 5)
print(f"Inside: {test_point in rect}")  # Inside: True
```

## Why twod?

- **Human-Friendly**: Intuitive method names and clear documentation
- **Flexible**: Choose the implementation that best fits your needs
- **Comprehensive**: Full suite of geometric operations and relationships
- **Well-Tested**: Extensive test suite ensuring reliability
- **Modern Python**: Requires Python 3.11+ and uses structural pattern matching

## Getting Started

Ready to dive in? Check out the [installation guide](installation.md) and [quickstart tutorial](quickstart.md) to begin using twod in your projects.

## API Reference

Explore the complete API documentation:

- [API Reference](api/index.md) - Complete API documentation for all classes and modules

## Contributing

twod is open source and welcomes contributions! Visit the [GitHub repository](https://github.com/JnyJny/twod) to report issues, suggest features, or contribute code.