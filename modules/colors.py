import itertools
import probability as p


class Color:
    def __init__(self, possible_numbers, max_guesses):
        self.possible_numbers = possible_numbers
        self.max_guesses = max_guesses
        self.template_colors = {"yellow": [i for i in range(1, 10)],
                                "light_blue": [i for i in range(10, 20)],
                                "gray": [i for i in range(20, 30)],
                                "green": [i for i in range(30, 40)],
                                "pink": [i for i in range(40, 50)],
                                "ivory": [i for i in range(50, 60)],
                                "red": [60]}

        self.templates = {}

        self.templates_combination = itertools.combinations_with_replacement(self.template_colors.keys(), 6)

        self.number_of_templates = 0

        for template in self.templates_combination:
            self.number_of_templates += 1
            combinations = 1
            colors = dict((i, template.count(i)) for i in template)

            # red just have one number, so it can't appear more than one time
            if 'red' in colors and colors['red'] > 1:
                continue

            min_values = []
            max_values = []
            for i in colors:
                combinations *= p.combination(len(self.template_colors[i]), colors[i])
                min_values += self.template_colors[i][0:colors[i]]
                max_values += self.template_colors[i][-colors[i]:]

            average_sum = (sum(min_values) + sum(max_values)) / 2
            self.templates[self.number_of_templates] = {
                'combinations': combinations,
                'average_sum': average_sum,
                'calculus': "{0:.2f}".format(float(combinations)/p.combination(self.possible_numbers, self.max_guesses))
            }

            if self.number_of_templates == 30:
                break

        print self.templates
