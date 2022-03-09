
# %%
"""
Simple Dice
    A dice.

"""

from random import choice

class Dice:
    def __init__(self, max_value=6):
        self.values = list(range(1, max_value))
    
    def shooted(self):
        return choice(self.values)

class SimpleDice:
    def __init__(self, max_value=6):
        self.dice = Dice(max_value)
    
    def shooted(self):
        return self.dice.shooted()

# %%
SimpleDice().shooted()

# %%
