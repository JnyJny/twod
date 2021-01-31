<!-- 2d two-dimension vector point geometry humans -->
# twod - A Two-Dimensional Geometry Library for Humans™
![version][pypi-version]
![pytest][pytest-action]
![license][license]
![monthly-downloads][monthly-downloads]
![Code style: black][code-style-black]

[twod][0] (pronounced "two dee") is a geometry library that supplies
simple two-dimensional geometric primtives:

- `twod.Point`
- `twod.Rect`

## Install

Installing `twod` is a snap!

```console
$ python3 -m pip install -U twod
```

## Development Workflow

```console
$ git clone https://github.com/JnyJny/twod.git
$ cd twod
$ poetry shell
...
(twod-...) $ 
```

## Usage Exmaples

```python

from twod import Point

o = Point()
b = Point.from_polar(10, 0)
assert b.distance(o) == 10.0
```

<!-- end links -->
[0]: https://github.com/JnyJny/twod.git

<!-- badges -->
[pytest-action]: https://github.com/JnyJny/twod/workflows/pytest/badge.svg
[code-style-black]: https://img.shields.io/badge/code%20style-black-000000.svg
[pypi-version]: https://img.shields.io/pypi/v/twod
[license]: https://img.shields.io/pypi/l/twod
[monthly-downloads]: https://img.shields.io/pypi/dm/twod
