import random

class Flag:
    def __init__(self, country, path, acceptableNames=[], hint=""):
        self.path = path
        self.country = country
        self.hint = hint
        self.acceptableNames = acceptableNames.append(country)


def selectFlag(flagList):
    selectionIndex = random.randint(0, len(flagList)-1)

    return flagList[selectionIndex], selectionIndex