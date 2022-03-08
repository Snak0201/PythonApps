# %%
from random import choice


class Dice:

    def __init__(self, dice_max=6, zero_mode=False):
        """Dice.

        Parameters
        ----------
        dice_max : int
            Max value of dice
        zero_mode : bool
            If this is True, dice includes value "0"

        Attribute
        ---------
        value : int
            Range of dice value
        """
        if zero_mode:
            self.value = list(range(0, dice_max + 1))
        else:
            self.value = list(range(1, dice_max + 1))

    def shooted(self, n=1):
        """Shoot Dice.

        Parameters
        ----------
        n : int
            Number of dices

        Returns
        -------
        rolls : list
            List of dice values
        sum(rolls) : int
            Total value of dices
        """
        rolls = [choice(self.value) for _ in range(n)]
        return rolls, sum(rolls)
