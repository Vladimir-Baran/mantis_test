from sys import maxsize

class Progect:

    def __init__(self, category=None):
        self.category == category

    def __repr__(self):
        return self.category

    def __eq__(self, other):
        return (self.category is None or other.category is None or self.category == other.category)