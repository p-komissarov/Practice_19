class User:
    """
    A class to represent a website user with flexible profile data.

    Attributes:
        id (int): Unique user identifier.
        nick_name (str): User login/alias.
        first_name (str): Given name.
        last_name (str): Family name (optional).
        middle_name (str): Patronymic (optional).
        gender (str): Gender (optional).
    """

    def __init__(
        self,
        id: int,
        nick_name: str,
        first_name: str,
        last_name: str = '',
        middle_name: str = '',
        gender: str = ''
    ):
        """
        Initialize the User instance with mandatory and optional fields.
        """
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def update(
        self,
        id: int = None,
        nick_name: str = None,
        first_name: str = None,
        last_name: str = None,
        middle_name: str = None,
        gender: str = None
    ) -> None:
        """
        Update attributes if provided values are truthy (non-zero/non-empty).
        """
        if id:
            self.id = id
        if nick_name:
            self.nick_name = nick_name
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if middle_name:
            self.middle_name = middle_name
        if gender:
            self.gender = gender

    def __str__(self) -> str:
        """
        Format the user data into a specific string for printing.
        """
        name_parts = [self.last_name, self.first_name, self.middle_name]
        full_name = ' '.join([part for part in name_parts]).strip()
        
        base_info = f"ID: {self.id} LOGIN: {self.nick_name} NAME: {full_name}"
        
        if self.gender:
            base_info += f" GENDER: {self.gender}"
            
        return base_info