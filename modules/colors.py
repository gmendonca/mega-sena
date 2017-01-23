import itertools


class Color:
    def __init__(self):
        self.template_colors = {"yellow": [i for i in range(1, 10)],
                                "light_blue": [i for i in range(11, 20)],
                                "gray": [i for i in range(21, 30)],
                                "green": [i for i in range(31, 40)],
                                "pink": [i for i in range(41, 50)],
                                "ivory": [i for i in range(51, 60)],
                                "red": [60]}

        self.templates = {}

        self.templates_combination = itertools.combinations_with_replacement(self.template_colors.keys(), 6)

        self.number_of_templates = sum(1 for _ in self.templates_combination)
