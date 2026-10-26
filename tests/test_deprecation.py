"""test the CPoint and CRect deprecation like a human™"""

import warnings

import pytest
import twod


@pytest.mark.parametrize("name, replacement", [("CPoint", "Point"), ("CRect", "Rect")])
def test_complex_classes_warn_on_access(name, replacement):
    with pytest.warns(DeprecationWarning, match=f"{name} is deprecated") as record:
        cls = getattr(twod, name)

    assert cls.__name__ == name
    assert f"use twod.{replacement}" in str(record[0].message)
    assert record[0].filename == __file__


def test_complex_classes_warn_on_from_import():
    with pytest.warns(DeprecationWarning, match="CPoint is deprecated") as record:
        from twod import CPoint  # noqa: F401

    assert record[0].filename == __file__


def test_supported_names_do_not_warn():
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        for name in twod.__all__:
            getattr(twod, name)


def test_complex_classes_are_not_in_all():
    assert "CPoint" not in twod.__all__
    assert "CRect" not in twod.__all__


def test_unknown_attribute_raises():
    with pytest.raises(AttributeError, match="no attribute 'Nope'"):
        twod.Nope
