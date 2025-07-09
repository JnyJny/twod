# twod - A Two-Dimensional Geometry Library for Humans™

[![Test & Publish](https://github.com/JnyJny/twod/actions/workflows/release.yaml/badge.svg)](https://github.com/JnyJny/twod/actions/workflows/release.yaml)
![Version](https://img.shields.io/pypi/v/twod)
![Python Version](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FJnyJny%2Ftwod%2Fmaster%2Fpyproject.toml)
![License](https://img.shields.io/pypi/l/twod)
![Monthly Downloads](https://img.shields.io/pypi/dm/twod)

**twod** (pronounced "two dee") is a Python library that provides simple, intuitive two-dimensional geometric primitives designed for humans. It offers both traditional float-based and complex number-based implementations of fundamental geometric objects.

## Features

- **Multiple Implementations**: Choose between traditional float-based (`Point`, `Rect`) and complex number-based (`CPoint`, `CRect`) implementations
- **Comprehensive Geometry**: Points, rectangles, lines, and ellipses with full geometric operations
- **Intuitive API**: Human-friendly method names and comprehensive docstrings
- **Performance Options**: Complex number implementations leverage Python's optimized complex type
- **Rich Operations**: Full arithmetic operator support, geometric calculations, and spatial relationships

## Core Classes

### Point Classes
- **`Point`**: Traditional float-based 2D point with comprehensive geometric operations
- **`CPoint`**: Complex number-based point implementation with similar API but leveraging Python's complex type

### Rectangle Classes  
- **`Rect`**: Traditional rectangle using Point internally
- **`CRect`**: Complex number-based rectangle using CPoint and mixins

### Additional Primitives
- **`Line`**: Line segment with geometric operations like intersections, distances, and relationships
- **`Ellipse`**: Ellipse with properties like area, perimeter, and eccentricity

## Quick Example

```python
from twod import Point, Rect, Line

# Create points
origin = Point(0, 0)
corner = Point(10, 10)

# Calculate distance
distance = origin.distance(corner)  # 14.142135623730951

# Create a rectangle
rect = Rect(origin, corner)
print(f"Area: {rect.area}")  # Area: 100.0

# Create a line
line = Line(origin, corner)
print(f"Length: {line.length}")  # Length: 14.142135623730951
print(f"Angle: {line.angle_degrees}")  # Angle: 45.0

# Check if point is inside rectangle
test_point = Point(5, 5)
print(f"Inside: {test_point.inside(rect.bottom_left, rect.top_right)}")  # Inside: True
```

## Why twod?

- **Human-Friendly**: Intuitive method names and clear documentation
- **Flexible**: Choose the implementation that best fits your needs
- **Comprehensive**: Full suite of geometric operations and relationships
- **Well-Tested**: Extensive test suite ensuring reliability
- **Modern Python**: Uses Python 3.10+ features like structural pattern matching

## Getting Started

Ready to dive in? Check out the [installation guide](installation.md) and [quickstart tutorial](quickstart.md) to begin using twod in your projects.

## API Reference

Explore the complete API documentation:

- [API Reference](api/index.md) - Complete API documentation for all classes and modules

## Contributing

twod is open source and welcomes contributions! Visit the [GitHub repository](https://github.com/JnyJny/twod) to report issues, suggest features, or contribute code.