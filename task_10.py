from task_6 import Point


class Segment:
    """
    Represents a line segment between two Point objects.

    Attributes:
        p1 (Point): Start point.
        p2 (Point): End point.
        one_intersection (bool): True if the segment intersects exactly one axis.
    """

    def __init__(self, p1: Point, p2: Point):
        """
        Initialize segment and determine axis intersections.
        """
        self.p1 = p1
        self.p2 = p2

        intersects_x = (p1.y * p2.y) < 0
        intersects_y = (p1.x * p2.x) < 0

        self.one_intersection = (intersects_x + intersects_y) == 1

    def __str__(self) -> str:
        """String representation."""
        return f"({self.p1}, {self.p2})"
    
    def __repr__(self) -> str:
        """Formal string representation."""
        return f"({self.p1}, {self.p2})"


class CoordinateSystem:
    """
    Represents a coordinate system containing multiple segments.

    Attributes:
        segments (list): List of Segment objects.
    """

    def __init__(self):
        """Initialize an empty coordinate system."""
        self.segments: list[Segment] = []

    def add_segment(self, segment: Segment) -> None:
        """Add a segment to the system."""
        self.segments.append(segment)

    def axis_intersection(self) -> int:
        """
        Count segments that intersect exactly one axis.
        """
        return sum(1 for s in self.segments if s.one_intersection)

    def __str__(self) -> str:
        """Return list of segments as string."""
        return str(self.segments)