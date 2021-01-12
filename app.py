# 1/11 Random Values
import random

class Dice:
    def roll(self):
        rollone = random.randint(1, 6)
        rolltwo = random.randint(1, 6)
        return rollone, rolltwo


dice = Dice()
print(dice.roll())
