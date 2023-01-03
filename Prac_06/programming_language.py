"""CP1404 - Practical - Programming language"""


class ProgrammingLanguage:
    """Represents a Programming Language"""

    def __init__(self,name, typing, reflection, year):
        """Initialise the programming language instance has all the fields with parameters"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Returns a single string formatted for a programming language"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """check if the language is dynamic or not"""
        return self.typing == "Dynamic"

