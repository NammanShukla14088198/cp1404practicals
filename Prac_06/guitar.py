"""CP1404 - Practical - Guitar"""
CUR_YEAR = 2023
VINTAGE_STATUS = 50


class Guitar:
    """Class which stores values for a Guitar"""

    def __init__(self, name="", year=0, cost=0):
        """Initialize the Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns a formatted string with details of a Guitar"""
        return f"{self.name} ({self.year}) : {self.cost} "

    def get_age(self):
        """Return the age of the Guitar"""
        return CUR_YEAR - self.year

    def is_vintage(self):
        """Determine if the Guitar is Vintage or not"""
        return self.get_age() >= VINTAGE_STATUS
