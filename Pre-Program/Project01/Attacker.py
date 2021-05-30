import random
from GameOverException import GameOver


class Attacker:
    def __init__(self):
        self.name = "Attacker"
        self.n_dice = 3
        self.n_units = 0
        self.max_rolls = 0

    def set_units(self, units):
        self.n_units = units

    def get_units(self):
        return self.n_units

    def set_max_rolls(self, n):
        self.max_rolls = n

    def get_max_rolls(self):
        return self.max_rolls

    def roll_dice(self):
        results = []

        if self.n_units >= 3:
            self.set_max_rolls(3)

        elif self.n_units == 2:
            self.set_max_rolls(2)

        else:
            self.set_max_rolls(1)

        for i in range(0, self.max_rolls):
            rn = random.randint(1, 6)
            results.append(rn)

        results.sort(reverse=True)

        return results

    def loses(self):
        self.n_units = self.n_units - 1
        if self.n_units <= 0:
            raise GameOver



