class StrandsDNA:
    """
    A class to store and manage DNA strands.

    Attributes:
        all_strands (list): A list of all added DNA strands.
    """

    def __init__(self):
        """
        Initialize an empty list to store DNA strands.
        """
        self.all_strands: list[str] = []

    def add_strands(self, strands: str) -> None:
        """
        Add DNA strands provided as a space-separated string.

        Args:
            strands (str): A string containing DNA strands separated by spaces.
        """
        new_strands = strands.split()
        self.all_strands.extend(new_strands)

    def get_max_strands(self) -> str:
        """
        Return a space-separated string of unique strands with the maximum length,
        sorted lexicographically.

        Returns:
            str: Space-separated longest strands.
        """
        if not self.all_strands:
            return ""

        max_len = len(max(self.all_strands, key=len))

        longest_unique = {s for s in self.all_strands if len(s) == max_len}

        return " ".join(sorted(longest_unique))

    def __str__(self) -> str:
        """
        Return a string representation of all stored strands separated by spaces.
        """
        return " ".join(self.all_strands)