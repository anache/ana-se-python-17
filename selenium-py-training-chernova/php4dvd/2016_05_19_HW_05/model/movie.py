class Movie(object):

    def __init__(self, title="", year=2000):
        self.title = title
        self.year = year

    @classmethod
    def random(cls):
        from random import randint
        return cls(title="Movie " + str(randint(0, 1000000)), year=randint(1900, 2000))

    @classmethod
    def ForrestGump(cls):
        return cls(title="Forrest Gump", year=1994)

    @classmethod
    def Titanic(cls):
        return cls(title="Titanic", year=1996)

    @classmethod
    def Bad(cls):
        return cls(title="Bad", year="one")
