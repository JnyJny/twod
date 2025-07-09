"""a line segment for humans™"""

from __future__ import annotations

import math
import operator
from dataclasses import dataclass
from typing import Any, Callable, Optional

from .point import Point
from .exceptions import ColinearPoints


@dataclass(slots=True)
class Line:
    """A line segment defined by two points.
    
    The Line class represents a geometric line segment with start and end points
    and provides many helpful properties and methods for geometric operations.
    
    >>> line = Line(Point(0, 0), Point(3, 4))
    >>> line.length
    5.0
    >>> line.angle_degrees
    53.13010235415598
    """
    
    start: Point = None
    end: Point = None
    
    def __post_init__(self):
        """Ensure start and end are Point instances."""
        if self.start is None:
            self.start = Point()
        elif not isinstance(self.start, Point):
            self.start = Point(*self.start) if hasattr(self.start, '__iter__') else Point(self.start, 0)
        
        if self.end is None:
            self.end = Point()
        elif not isinstance(self.end, Point):
            self.end = Point(*self.end) if hasattr(self.end, '__iter__') else Point(self.end, 0)
    
    @property
    def length(self) -> float:
        """The length of this line segment."""
        return self.start.distance(self.end)
    
    @property
    def length_squared(self) -> float:
        """The squared length of this line segment (faster than length)."""
        return self.start.distance_squared(self.end)
    
    @property
    def vector(self) -> Point:
        """The vector from start to end point."""
        return self.end - self.start
    
    @property
    def direction(self) -> Point:
        """The unit vector in the direction from start to end."""
        if self.length == 0:
            return Point()
        return self.vector / self.length
    
    @property
    def angle_radians(self) -> float:
        """The angle of this line in radians, measured counter-clockwise from positive x-axis."""
        return self.vector.radians
    
    @property
    def angle_degrees(self) -> float:
        """The angle of this line in degrees, measured counter-clockwise from positive x-axis."""
        return self.vector.degrees
    
    @property
    def slope(self) -> float:
        """The slope of this line (rise over run)."""
        dx = self.end.x - self.start.x
        if dx == 0:
            return float('inf') if self.end.y > self.start.y else float('-inf')
        return (self.end.y - self.start.y) / dx
    
    @property
    def midpoint(self) -> Point:
        """The midpoint of this line segment."""
        return self.start.midpoint(self.end)
    
    @property
    def is_point(self) -> bool:
        """True if this line has zero length (start == end)."""
        return self.start == self.end
    
    @property
    def is_horizontal(self) -> bool:
        """True if this line is horizontal (same y coordinates)."""
        return self.start.y == self.end.y
    
    @property
    def is_vertical(self) -> bool:
        """True if this line is vertical (same x coordinates)."""
        return self.start.x == self.end.x
    
    def reverse(self) -> Line:
        """Return a new line with start and end points swapped."""
        return Line(self.end, self.start)
    
    def extend(self, distance: float, from_end: bool = True) -> Line:
        """Extend the line by a given distance.
        
        Args:
            distance: Distance to extend (positive extends outward, negative inward)
            from_end: If True, extend from end point; if False, extend from start point
            
        Returns:
            New Line extended by the specified distance
        """
        if self.is_point:
            return Line(self.start, self.end)
        
        direction = self.direction
        if from_end:
            new_end = self.end + (direction * distance)
            return Line(self.start, new_end)
        else:
            new_start = self.start - (direction * distance)
            return Line(new_start, self.end)
    
    def point_at_parameter(self, t: float) -> Point:
        """Get point on line at parameter t.
        
        Args:
            t: Parameter where 0 = start point, 1 = end point
            
        Returns:
            Point on the line at parameter t
        """
        return self.start + (self.vector * t)
    
    def distance_to_point(self, point: Point) -> float:
        """Calculate the shortest distance from a point to this line segment.
        
        Args:
            point: Point to calculate distance to
            
        Returns:
            Shortest distance from point to line segment
        """
        if self.is_point:
            return self.start.distance(point)
        
        # Project point onto line
        v = self.vector
        w = point - self.start
        
        # Calculate parameter t for projection
        t = w.dot(v) / v.dot(v)
        
        # Clamp t to [0, 1] to stay within line segment
        t = max(0, min(1, t))
        
        # Find closest point on segment
        closest = self.start + (v * t)
        return point.distance(closest)
    
    def closest_point_on_line(self, point: Point) -> Point:
        """Find the closest point on this line segment to the given point.
        
        Args:
            point: Point to find closest point to
            
        Returns:
            Closest point on the line segment
        """
        if self.is_point:
            return self.start
        
        # Project point onto line
        v = self.vector
        w = point - self.start
        
        # Calculate parameter t for projection
        t = w.dot(v) / v.dot(v)
        
        # Clamp t to [0, 1] to stay within line segment
        t = max(0, min(1, t))
        
        return self.start + (v * t)
    
    def intersects_line(self, other: Line) -> bool:
        """Check if this line segment intersects with another line segment.
        
        Args:
            other: Other line segment to check intersection with
            
        Returns:
            True if the line segments intersect
        """
        return self.intersection_point(other) is not None
    
    def intersection_point(self, other: Line) -> Optional[Point]:
        """Find the intersection point of two line segments.
        
        Args:
            other: Other line segment to find intersection with
            
        Returns:
            Intersection point if it exists, None otherwise
        """
        # Get line segment vectors
        d1 = self.vector
        d2 = other.vector
        
        # Check if lines are parallel
        cross = d1.cross(d2)
        if abs(cross) < 1e-10:  # Lines are parallel or collinear
            return None
        
        # Calculate intersection parameters
        start_diff = other.start - self.start
        t1 = start_diff.cross(d2) / cross
        t2 = start_diff.cross(d1) / cross
        
        # Check if intersection is within both line segments
        if 0 <= t1 <= 1 and 0 <= t2 <= 1:
            return self.point_at_parameter(t1)
        
        return None
    
    def parallel_to(self, other: Line) -> bool:
        """Check if this line is parallel to another line.
        
        Args:
            other: Other line to check parallelism with
            
        Returns:
            True if lines are parallel
        """
        if self.is_point or other.is_point:
            return False
        
        # Lines are parallel if their cross product is zero (relative to vector magnitudes)
        v1, v2 = self.vector, other.vector
        cross = v1.cross(v2)
        magnitude_product = v1.radius * v2.radius
        
        if magnitude_product == 0:
            return True  # At least one is zero vector
            
        return abs(cross / magnitude_product) < 1e-10
    
    def perpendicular_to(self, other: Line) -> bool:
        """Check if this line is perpendicular to another line.
        
        Args:
            other: Other line to check perpendicularity with
            
        Returns:
            True if lines are perpendicular
        """
        if self.is_point or other.is_point:
            return False
        
        # Lines are perpendicular if their dot product is zero (relative to vector magnitudes)
        v1, v2 = self.vector, other.vector
        dot = v1.dot(v2)
        magnitude_product = v1.radius * v2.radius
        
        if magnitude_product == 0:
            return False  # At least one is zero vector
            
        return abs(dot / magnitude_product) < 1e-10
    
    def angle_between(self, other: Line) -> float:
        """Calculate the angle between this line and another line in radians.
        
        Args:
            other: Other line to calculate angle with
            
        Returns:
            Angle between lines in radians (0 to π)
        """
        if self.is_point or other.is_point:
            return 0.0
        
        # Normalize vectors
        v1 = self.direction
        v2 = other.direction
        
        # Calculate angle using dot product
        dot_product = v1.dot(v2)
        dot_product = max(-1.0, min(1.0, dot_product))  # Clamp to avoid numerical errors
        
        return math.acos(abs(dot_product))
    
    def contains_point(self, point: Point, tolerance: float = 1e-10) -> bool:
        """Check if a point lies on this line segment.
        
        Args:
            point: Point to check
            tolerance: Tolerance for floating point comparison
            
        Returns:
            True if point lies on the line segment
        """
        return self.distance_to_point(point) <= tolerance
    
    def __eq__(self, other: object) -> bool:
        """Check equality with another Line."""
        if not isinstance(other, Line):
            return NotImplemented
        return self.start == other.start and self.end == other.end
    
    def __len__(self) -> int:
        """Return 2 (number of points defining the line)."""
        return 2
    
    def __getitem__(self, key: int) -> Point:
        """Get start (0) or end (1) point."""
        if key == 0:
            return self.start
        elif key == 1:
            return self.end
        else:
            raise IndexError(f"Line index {key} out of range")
    
    def __setitem__(self, key: int, value: Point) -> None:
        """Set start (0) or end (1) point."""
        if not isinstance(value, Point):
            value = Point(*value) if hasattr(value, '__iter__') else Point(value, 0)
        
        if key == 0:
            self.start = value
        elif key == 1:
            self.end = value
        else:
            raise IndexError(f"Line index {key} out of range")
    
    def __iter__(self):
        """Iterate over start and end points."""
        yield self.start
        yield self.end
    
    def _op(self, other: Any, op: Callable) -> Line:
        """Apply operation to both start and end points."""
        try:
            if isinstance(other, Point):
                return Line(op(self.start, other), op(self.end, other))
            elif isinstance(other, (list, tuple)) and len(other) == 2:
                point = Point(*other)
                return Line(op(self.start, point), op(self.end, point))
            elif isinstance(other, (float, int)):
                return Line(op(self.start, other), op(self.end, other))
            else:
                return NotImplemented
        except (TypeError, ValueError):
            return NotImplemented
    
    def __add__(self, other: Any) -> Line:
        """Add a point or scalar to both endpoints."""
        return self._op(other, operator.add)
    
    def __sub__(self, other: Any) -> Line:
        """Subtract a point or scalar from both endpoints."""
        return self._op(other, operator.sub)
    
    def __mul__(self, other: Any) -> Line:
        """Multiply both endpoints by a point or scalar."""
        return self._op(other, operator.mul)
    
    def __truediv__(self, other: Any) -> Line:
        """Divide both endpoints by a point or scalar."""
        return self._op(other, operator.truediv)
    
    def __neg__(self) -> Line:
        """Return line with negated coordinates."""
        return Line(-self.start, -self.end)
    
    def __abs__(self) -> Line:
        """Return line with absolute coordinates."""
        return Line(abs(self.start), abs(self.end))