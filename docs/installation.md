# Installation

## Requirements

twod requires Python 3.10 or higher. You can check your Python version with:

```bash
python --version
```

## Install from PyPI

The easiest way to install twod is from PyPI using pip:

```bash
pip install twod
```

To upgrade to the latest version:

```bash
pip install --upgrade twod
```

## Install from Source

To install the latest development version from GitHub:

```bash
pip install git+https://github.com/JnyJny/twod.git
```

## Development Installation

If you want to contribute to twod or modify the source code, you'll need a development installation:

### 1. Clone the Repository

```bash
git clone https://github.com/JnyJny/twod.git
cd twod
```

### 2. Install Dependencies

The project uses `uv` for dependency management. Install it first:

```bash
pip install uv
```

Then sync the development dependencies:

```bash
uv sync --group dev --group docs
```

### 3. Verify Installation

Run the tests to ensure everything is working:

```bash
pytest
```

Check code coverage:

```bash
poe coverage
```

Run type checking:

```bash
poe check
```

## Virtual Environment

We recommend using a virtual environment to avoid conflicts with other packages:

### Using venv

```bash
python -m venv twod-env
source twod-env/bin/activate  # On Windows: twod-env\Scripts\activate
pip install twod
```

### Using conda

```bash
conda create -n twod-env python=3.10
conda activate twod-env
pip install twod
```

## Verification

After installation, verify that twod is working correctly:

```python
from twod import Point, Rect, Line

# Test basic functionality
p1 = Point(0, 0)
p2 = Point(3, 4)
distance = p1.distance(p2)
print(f"Distance: {distance}")  # Should print: Distance: 5.0

# Test complex number implementation
from twod import CPoint
cp = CPoint(3+4j)
print(f"CPoint radius: {cp.radius}")  # Should print: CPoint radius: 5.0
```

If this runs without errors, twod is successfully installed!

## Troubleshooting

### Python Version Issues

If you encounter issues with Python version compatibility:

```bash
# Check your Python version
python --version

# If you have multiple Python versions, try:
python3.10 -m pip install twod
# or
python3.11 -m pip install twod
```

### Import Errors

If you get import errors, ensure you're in the correct environment:

```bash
# Check which Python is being used
which python

# Check installed packages
pip list | grep twod
```

### Development Dependencies

For development, ensure all dependency groups are installed:

```bash
uv sync --group dev --group docs
```

## Next Steps

Now that you have twod installed, check out the [quickstart guide](quickstart.md) to learn how to use it!