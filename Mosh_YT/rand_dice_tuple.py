import random
class DiceTuple:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return (first, second)


diceT=DiceTuple()
print(diceT.roll())