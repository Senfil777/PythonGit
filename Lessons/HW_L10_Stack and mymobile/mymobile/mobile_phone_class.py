class MobilePhone:
    """Class representing a simple mobile phone."""

    def __init__(self, number):
        self.number = number
        self.status = False

    def turn_on(self):
        self.status = True
        return f"mobile phone {self.number} is enabled"

    def turn_off(self):
        self.status = False
        return f"mobile phone {self.number} is turned off"

    def call(self, cally):
        if self.status:
            return f"calling {cally}"

        return f"mobile phone {self.number} is turned off"
