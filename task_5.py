class Game:
    """
    A class to represent a basketball game between two teams.

    Attributes:
        teams (dict): A dictionary containing names of 'command1' and 'command2'.
        score (dict): A dictionary tracking points for command 1 and command 2.
    """

    def __init__(self, teams_info: dict):
        """
        Initialize the game with team names and zero scores.

        Args:
            teams_info (dict): Dictionary with keys 'command1' and 'command2'.
        """
        self.teams = teams_info
        self.score = {1: 0, 2: 0}

    def ball_thrown(self, command: int, points: int) -> None:
        """
        Add points to the specified team.

        Args:
            command (int): The number of the team (1 or 2).
            points (int): Number of points to add.
        """
        if command in self.score:
            self.score[command] += points

    def get_score(self) -> tuple:
        """
        Get the current score of the game.

        Returns:
            tuple: A tuple containing (points_team_1, points_team_2).
        """
        return (self.score[1], self.score[2])

    def get_winner(self) -> str:
        """
        Determine the winner of the game.

        Returns:
            str: The name of the winning team or 'Ничья' if it's a draw.
        """
        if self.score[1] > self.score[2]:
            return self.teams['command1']
        if self.score[2] > self.score[1]:
            return self.teams['command2']
        return 'Ничья'