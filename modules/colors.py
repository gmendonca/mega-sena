import itertools
import probability as p


def what_color(num):
    if num in range(1, 10):
        return "yellow"
    elif num in range(10, 20):
        return "light_blue"
    elif num in range(20, 30):
        return "gray"
    elif num in range(30, 40):
        return "green"
    elif num in range(40, 50):
        return "pink"
    elif num in range(50, 60):
        return "ivory"
    elif num == 60:
        return "red"


def what_template(list_num):
    template_to_find = ()
    for num in list_num:
        template_to_find += (what_color(num),)
    return tuple(sorted(template_to_find))


class Color:
    def __init__(self, possible_numbers, max_guesses, num_of_contests, number_module):
        self.possible_numbers = possible_numbers
        self.max_guesses = max_guesses
        self.num_of_contests = num_of_contests
        self.number_module = number_module
        self.template_colors = {
            "yellow": [i for i in range(1, 10)],
            "light_blue": [i for i in range(10, 20)],
            "gray": [i for i in range(20, 30)],
            "green": [i for i in range(30, 40)],
            "pink": [i for i in range(40, 50)],
            "ivory": [i for i in range(50, 60)],
            "red": [60]
        }

        self.templates = {}

        self.templates_combination = itertools.combinations_with_replacement(self.template_colors.keys(), 6)

        self.number_of_templates = 0

        self.facts = {}

        for sequence in number_module.unique_sequences:
            template = what_template(sequence)
            if template in self.facts:
                self.facts[template] += 1
            else:
                self.facts[template] = 1

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
            calculus = float(combinations) / p.combination(self.possible_numbers, self.max_guesses)

            sorted_template = tuple(sorted(template))

            self.templates[sorted_template] = {
                'Template number': self.number_of_templates,
                'Number of combinations': combinations,
                'Average sum': average_sum,
                'Probability': "{0:.2f}".format(10000 * calculus) + "%",
                'Number of expected draws': int(self.num_of_contests * calculus),
                'Number of draws': self.facts[sorted_template] if sorted_template in self.facts else 0,
                'Template': sorted_template
            }
