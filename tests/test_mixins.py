"""Tests for mixins.py module"""

import pytest
from twod.mixins import MixinPoint, MixinDimension
from twod import CPoint


class TestMixinPoint:
    """Test cases for MixinPoint class"""

    def test_mixin_point_x_property(self):
        """Test x property getter"""
        mixin = MixinPoint()
        mixin._p = CPoint(5, 10)
        assert mixin.x == 5

    def test_mixin_point_x_setter(self):
        """Test x property setter"""
        mixin = MixinPoint()
        mixin._p = CPoint(0, 0)
        mixin.x = 7
        assert mixin._p.x == 7

    def test_mixin_point_y_property(self):
        """Test y property getter"""
        mixin = MixinPoint()
        mixin._p = CPoint(5, 10)
        assert mixin.y == 10

    def test_mixin_point_y_setter(self):
        """Test y property setter"""
        mixin = MixinPoint()
        mixin._p = CPoint(0, 0)
        mixin.y = 12
        assert mixin._p.y == 12

    def test_mixin_point_xy_property(self):
        """Test xy property getter"""
        mixin = MixinPoint()
        mixin._p = CPoint(3, 4)
        assert mixin.xy == (3, 4)

    def test_mixin_point_xy_setter(self):
        """Test xy property setter"""
        mixin = MixinPoint()
        mixin._p = CPoint(0, 0)
        mixin.xy = (8, 9)
        assert mixin._p.xy == (8, 9)

    def test_mixin_point_xy_setter_with_list(self):
        """Test xy property setter with list"""
        mixin = MixinPoint()
        mixin._p = CPoint(0, 0)
        mixin.xy = [6, 7]
        assert mixin._p.xy == (6, 7)

    def test_mixin_point_setters_with_float(self):
        """Test setters with float values"""
        mixin = MixinPoint()
        mixin._p = CPoint(0, 0)
        mixin.x = 1.5
        mixin.y = 2.5
        assert mixin.x == 1.5
        assert mixin.y == 2.5

    def test_mixin_point_setters_with_int(self):
        """Test setters with int values"""
        mixin = MixinPoint()
        mixin._p = CPoint(0, 0)
        mixin.x = 3
        mixin.y = 4
        assert mixin.x == 3
        assert mixin.y == 4


class TestMixinDimension:
    """Test cases for MixinDimension class"""

    def test_mixin_dimension_w_property(self):
        """Test w property getter"""
        mixin = MixinDimension()
        mixin._d = CPoint(15, 20)
        assert mixin.w == 15

    def test_mixin_dimension_w_setter(self):
        """Test w property setter"""
        mixin = MixinDimension()
        mixin._d = CPoint(0, 0)
        mixin.w = 25
        assert mixin._d.x == 25

    def test_mixin_dimension_h_property(self):
        """Test h property getter"""
        mixin = MixinDimension()
        mixin._d = CPoint(15, 20)
        assert mixin.h == 20

    def test_mixin_dimension_h_setter(self):
        """Test h property setter"""
        mixin = MixinDimension()
        mixin._d = CPoint(0, 0)
        mixin.h = 30
        assert mixin._d.y == 30

    def test_mixin_dimension_wh_property(self):
        """Test wh property getter"""
        mixin = MixinDimension()
        mixin._d = CPoint(11, 12)
        assert mixin.wh == (11, 12)

    def test_mixin_dimension_wh_setter(self):
        """Test wh property setter"""
        mixin = MixinDimension()
        mixin._d = CPoint(0, 0)
        mixin.wh = (35, 40)
        assert mixin._d.xy == (35, 40)

    def test_mixin_dimension_wh_setter_with_list(self):
        """Test wh property setter with list"""
        mixin = MixinDimension()
        mixin._d = CPoint(0, 0)
        mixin.wh = [45, 50]
        assert mixin._d.xy == (45, 50)

    def test_mixin_dimension_setters_with_float(self):
        """Test setters with float values"""
        mixin = MixinDimension()
        mixin._d = CPoint(0, 0)
        mixin.w = 1.5
        mixin.h = 2.5
        assert mixin.w == 1.5
        assert mixin.h == 2.5

    def test_mixin_dimension_setters_with_int(self):
        """Test setters with int values"""
        mixin = MixinDimension()
        mixin._d = CPoint(0, 0)
        mixin.w = 3
        mixin.h = 4
        assert mixin.w == 3
        assert mixin.h == 4


class TestMixinIntegration:
    """Test integration of mixins with CRect"""

    def test_mixin_integration_with_crect(self):
        """Test that mixins work properly with CRect"""
        from twod import CRect
        
        rect = CRect(1, 2, 3, 4)
        
        # Test MixinPoint functionality
        assert rect.x == 1
        assert rect.y == 2
        assert rect.xy == (1, 2)
        
        # Test MixinDimension functionality
        assert rect.w == 3
        assert rect.h == 4
        assert rect.wh == (3, 4)
        
        # Test setters
        rect.x = 10
        rect.y = 20
        rect.w = 30
        rect.h = 40
        
        assert rect.x == 10
        assert rect.y == 20
        assert rect.w == 30
        assert rect.h == 40
        
        # Test xy and wh setters
        rect.xy = (5, 6)
        rect.wh = (7, 8)
        
        assert rect.xy == (5, 6)
        assert rect.wh == (7, 8)