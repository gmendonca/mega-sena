import math


def combination(n1, n2):
    return math.factorial(n1) / \
           (math.factorial(n2) * (math.factorial(n1 - n2)))


def combination_less(n1, n2, n3, n4):
    return combination(n1, n2) * combination(n3, n4)


class Probability:
    def __init__(self, possible_numbers, max_guesses, quantity):
        self.possible_numbers = possible_numbers
        self.quantity = quantity
        self.max_guesses = max_guesses

        self.difference = self.possible_numbers - self.quantity

        self.chance = combination(self.possible_numbers, self.max_guesses)

    def sena(self):
        if self.max_guesses == self.quantity:
            return combination(self.possible_numbers, self.quantity)
        else:
            return self.chance / combination(self.possible_numbers, self.quantity)

    def quina(self, less_quantity=5, less_difference=1):
        return self.chance / combination_less(self.quantity, less_quantity, self.difference, less_difference)

    def quadra(self, less_quantity=4, less_difference=2):
        return self.chance / combination_less(self.quantity, less_quantity, self.difference, less_difference)
