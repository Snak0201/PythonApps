# %%
import random


class Dice:

    def __init__(self, dice_max=6, zero_mode=False):
        self.zero_mode = zero_mode
        if zero_mode:
            self.value = list(range(0, dice_max + 1))
        else:
            self.value = list(range(1, dice_max + 1))

    def shooted(self, n=1):
        rolls = [random.choice(self.value) for i in range(n)]
        return rolls, sum(rolls)


class Player:

    def __init__(self, name=''):
        self.name = name

    def shoot_dice(self, dice_max=6, n=1, zero_mode=False):
        rolls = Dice(dice_max, zero_mode).shooted(n)
        print(f'{self.name}の出目は{rolls[0]}、合計{rolls[1]}')


# %%
james = Player('James')

james.shoot_dice(n=5)

# %%
