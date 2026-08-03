# Python Code for Factory Method
# It comes under the Creational Design Pattern

class FrenchLocalizer:
    """It simply returns the French version."""

    def __init__(self):
        self.translations = {
            "car": "voiture",
            "bike": "bicyclette",
            "cycle": "cyclette"
        }

    def localize(self, msg):
        """Change the message using translations."""
        return self.translations.get(msg, msg)