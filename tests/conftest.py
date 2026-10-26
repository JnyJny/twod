"""pytest twod configuration for humans™"""

import pytest
from twod import Point


@pytest.fixture()
def point():
    return Point()
