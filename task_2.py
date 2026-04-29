class NotSleeping:
    """
    Represents a person trying to fall asleep by counting sheep.

    Attributes:
        name (str): The name of the person.
        count_sheeps (int): The current number of sheep counted.
    """

    def __init__(self, name: str, count_sheeps: int = 0):
        """
        Initialize the person with a name and an optional initial sheep count.

        Args:
            name (str): The name of the person.
            count_sheeps (int): Initial number of sheep (defaults to 0).
        """
        self.name = name
        self.count_sheeps = count_sheeps

    def add_sheep(self) -> None:
        """
        Increment the sheep counter by one.
        """
        self.count_sheeps += 1