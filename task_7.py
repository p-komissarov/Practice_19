class TrafficLight:
    """
    A class representing a traffic light with a specific sequence of signals.

    Attributes:
        permissible_values (list): List of signals in their correct order.
        current_signal (str): The signal currently displayed.
    """

    permissible_values: list = ['зеленый', 'желтый', 'красный', 'желтый']

    def __init__(self):
        """
        Initialize the traffic light starting with the green signal.
        """
        self._index = 0
        self.current_signal = self.permissible_values[self._index]

    def next_signal(self) -> None:
        """
        Switch the current signal to the next one in the sequence.
        """
        self._index = (self._index + 1) % len(self.permissible_values)
        self.current_signal = self.permissible_values[self._index]
