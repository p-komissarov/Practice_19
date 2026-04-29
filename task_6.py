import math

class Point:
    """
    Represents a point in 2D space.

    Attributes:
        x (int | float): The x-coordinate of the point.
        y (int | float): The y-coordinate of the point.
    """

    def __init__(self, coordinates: tuple = (0, 0)):
        """
        Initialize the point with a tuple of coordinates.

        Args:
            coordinates (tuple): A tuple containing (x, y). Defaults to (0, 0).
        """
        self.x = coordinates[0]
        self.y = coordinates[1]

    def get_x(self) -> int | float:
        """
        Return the x-coordinate.
        """
        return self.x

    def get_y(self) -> int | float:
        """
        Return the y-coordinate.
        """
        return self.y

    def distance(self, other: 'Point') -> float:
        """
        Calculate the Euclidean distance between this point and another.

        Args:
            other (Point): The other point to measure distance to.

        Returns:
            float: The calculated distance.
        """
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def sum(self, other: 'Point') -> 'Point':
        """
        Create a new point by summing coordinates of two points.

        Args:
            other (Point): The point to add to the current one.

        Returns:
            Point: A new instance of Point with summed coordinates.
        """
        return Point((self.x + other.x, self.y + other.y))

    def __str__(self) -> str:
        """
        Return a string representation of the point in (x; y) format.
        """
        return f"({self.x}; {self.y})"
    
    def __repr__(self) -> str:
        """
        Return a formal string representation of the point in (x; y) format.
        """
        return f"({self.x}; {self.y})"