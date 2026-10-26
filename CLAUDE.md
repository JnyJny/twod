# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`twod` is a Python library providing two-dimensional geometric primitives for humans. It offers float-based Point and Rect classes. The complex number implementations (CPoint and CRect) are deprecated and will be removed in 0.5.0.

## Development Commands

### Testing
- `pytest` - Run all tests
- `pytest tests/test_point.py` - Run specific test file
- `pytest tests/test_point.py::test_specific_function` - Run specific test
- `poe coverage` - Generate and view code coverage report

### Type Checking
- `poe ty` - Run ty type checker

### Code Quality
- `ruff check` - Run linter
- `ruff format` - Format code
- `poe ruff` - Format library source

### Package Management
- `uv sync` - Install dependencies
- `uv add <package>` - Add new dependency
- `uv remove <package>` - Remove dependency

### Documentation
- `poe docs_serve` - Serve documentation locally for development
- `poe docs_build` - Build documentation site
- `poe docs_deploy` - Deploy documentation to GitHub Pages

### Publishing
- `poe publish` - Publish patch version (default)
- `poe publish_minor` - Publish minor version
- `poe publish_major` - Publish major version

## Architecture

### Core Classes

**Point Classes:**
- `Point` (src/twod/point.py) - Traditional float-based 2D point with comprehensive geometric operations
- `CPoint` (src/twod/cpoint.py) - Deprecated complex number-based point; removed in 0.5.0

**Rectangle Classes:**
- `Rect` (src/twod/rect.py) - Traditional rectangle using Point internally
- `CRect` (src/twod/crect.py) - Deprecated complex number-based rectangle; removed in 0.5.0

**Supporting Components:**
- `constants.py` - Defines Quadrant enum and geometric constants
- `exceptions.py` - Custom exceptions like ColinearPoints
- `mixins/` - one module per mixin, exported from `mixins/__init__.py`: `Centered` for shapes located by a center Point, and `MixinPoint` and `MixinDimension` for CRect
- `ellipse.py` - Additional geometric primitives
- `line.py` - Line segment with geometric operations

### Key Design Patterns

1. **Single Implementation**: Point and Rect are the supported implementations. CPoint and CRect are deprecated, slower, and kept only until 0.5.0.

2. **Comprehensive Operator Support**: All classes support arithmetic operations (+, -, *, /, //, **) both regular and in-place variants.

3. **Flexible Input Handling**: Point.from_any() accepts various input types (complex, dict, list, tuple, scalar, string), and Point.from_point_like() is the conversion used wherever a Point is expected: a Point or a Sequence of two numbers, not strings, sets, dicts, complex numbers or iterators.

4. **Geometric Methods**: Both point classes provide distance, dot product, cross product, and winding direction (ccw) calculations.

5. **Mixins for Code Reuse**: CRect uses MixinPoint and MixinDimension to avoid code duplication.

### Testing Strategy

Tests are organized by class and operation:
- `test_point*.py` - Point class tests
- `test_cpoint*.py` - CPoint class tests  
- `test_rect*.py` - Rect class tests
- `test_crect*.py` - CRect class tests

Each operation type has its own test file (e.g., `test_point_add.py`, `test_cpoint_mul.py`).

### Development Notes

- The project requires Python 3.11+ and uses structural pattern matching in Point.from_any
- Complex number implementation leverages Python's cmath module for polar coordinates
- Both implementations maintain API compatibility where possible
- The library is designed for human-friendly usage with intuitive method names and comprehensive docstrings