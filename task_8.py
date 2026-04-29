class MorseMsg:
    """
    A class to decode and analyze messages written in Morse code.

    Attributes:
        msg (str): The original encoded Morse string.
        _morse_to_eng (dict): Dictionary for English decoding.
        _morse_to_ru (dict): Dictionary for Russian decoding.
    """

    _morse_map = {
        '.-': ('A', 'А'), '-...': ('B', 'Б'), '.--': ('W', 'В'),
        '--.': ('G', 'Г'), '-..': ('D', 'Д'), '.': ('E', 'Е'),
        '...-': ('V', 'Ж'), '--..': ('Z', 'З'), '..': ('I', 'И'),
        '.---': ('J', 'Й'), '-.-': ('K', 'К'), '.-..': ('L', 'Л'),
        '--': ('M', 'М'), '-.': ('N', 'Н'), '---': ('O', 'О'),
        '.--.': ('P', 'П'), '.-.': ('R', 'Р'), '...': ('S', 'С'),
        '-': ('T', 'Т'), '..-': ('U', 'У'), '..-.': ('F', 'Ф'),
        '....': ('H', 'Х'), '-.-.': ('C', 'Ц'), '---.': ('CH', 'Ч'),
        '----': ('SH', 'Ш'), '--.-': ('Q', 'Щ'), '--.--': ('', 'Ъ'),
        '-.--': ('Y', 'Ы'), '-..-': ('X', 'Ь'), '..-..': ('', 'Э'),
        '..--': ('', 'Ю'), '.-.-': ('', 'Я')
    }

    _vowels = {
        'eng': set("AEIOUY"),
        'ru': set("АЕЁИОУЫЭЮЯ")
    }
    
    _consonants = {
        'eng': set("BCDFGHJKLMNPQRSTVWXZ"),
        'ru': set("БВГДЖЗЙКЛМНОПРСТФХЦЧШЩЪЬ")
    }

    def __init__(self, msg: str):
        """
        Initialize with a Morse code string where letters are separated by spaces.
        """
        self.msg = msg
        self._encoded_chars = msg.split()

    def eng_decode(self) -> str:
        """
        Decode the Morse message into English uppercase letters.
        """
        return "".join(self._morse_map[char][0] for char in self._encoded_chars if char in self._morse_map)

    def ru_decode(self) -> str:
        """
        Decode the Morse message into Russian uppercase letters.
        """
        return "".join(self._morse_map[char][1] for char in self._encoded_chars if char in self._morse_map)

    def get_vowels(self, lang: str) -> list:
        """
        Get a list of vowels from the decoded message in their order of appearance.
        """
        decoded = self.eng_decode() if lang == 'eng' else self.ru_decode()
        target_vowels = self._vowels.get(lang, set())
        return [char for char in decoded if char in target_vowels]

    def get_consonants(self, lang: str) -> list:
        """
        Get a list of consonants from the decoded message in their order of appearance.
        """
        decoded = self.eng_decode() if lang == 'eng' else self.ru_decode()
        target_consonants = self._consonants.get(lang, set())
        return [char for char in decoded if char in target_consonants]
    
    def __str__(self) -> str:
        """
        Return a string representation of the message.
        """
        return self.msg