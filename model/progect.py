from sys import maxsize

class Progect:

    def __init__(self, name=None, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.name is None or other.name is None or self.name == other.name) and \
               (self.id is None or other.id is None or self.id == other.id)

    def id_or_max(self):
        if self.id:
            return self.id
        else:
            return maxsize