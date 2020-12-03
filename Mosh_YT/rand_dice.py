import random
class Dice:
    def roll(self):
        numbers=[]
        for i in range(2):
            elements=[1,2,3,4,5,6]
            ele=random.choice(elements)
            numbers.append(ele)
        print(numbers)
output=[]
Dice.roll(output)

dice=Dice()
dice.roll()


class DiceTuple:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return (first, second)


diceT=DiceTuple()
print(diceT.roll())