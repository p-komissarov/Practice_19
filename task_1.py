class Dog:
    """
    A class used to represent a Dog.

    Attributes:
        name (str): The name of the dog.
    """

    def __init__(self, name: str):
        """
        Initialize the dog with a name.

        Args:
            name (str): The name to assign to the dog.
        """
        self.name = name

    def say(self) -> None:
        """
        Output the dog's bark to the console.
        """
        print("Гав!")

