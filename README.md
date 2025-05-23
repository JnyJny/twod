<!-- 2d two-dimension vector point geometry humans -->
# twod - A Two-Dimensional Geometry Library for Humans™

[![Test & Publish][release-badge]][release]
![Version][pypi-version]
![Release Date][release-date]
![Python Version][python-version]
![License][license]
![Code Style: black][code-style-black]
![Monthly Downloads][monthly-downloads]

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

[pypi-version]: https://img.shields.io/pypi/v/twod
[python-version]: https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FJnyJny%2Ftwod%2Fmaster%2Fpyproject.toml
[license]: https://img.shields.io/pypi/l/twod
[dependencies]: https://img.shields.io/librariesio/github/JnyJny/twod
[monthly-downloads]: https://img.shields.io/pypi/dm/twod
[release-date]: https://img.shields.io/github/release-date/JnyJny/twod
[code-style-black]: https://img.shields.io/badge/code%20style-black-000000.svg
[release-badge]: https://github.com/JnyJny/twod/actions/workflows/release.yaml/badge.svg
[release]: https://github.com/JnyJny/twod/actions/workflows/release.yaml
