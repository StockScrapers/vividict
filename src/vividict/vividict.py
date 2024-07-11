# Quick class that allows for nested dictionaries without problems :)
class Vividict(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value
