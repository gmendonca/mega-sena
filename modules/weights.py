class CalculateWeights:
    def __init__(self):
        self.weight = 0.01
        self.average_total_sum_weight = 10
        self.average_total_sum_template_weight = 10
        self.sum_of_percentages_weight = 10
        self.template_chance_weight = 10

    def close_to_average_total_sum(self, sum_values, average_total_sum, color=False):
        result = (1 + (1 - abs(sum_values - average_total_sum)/float(average_total_sum)))
        if color:
            return result * self.average_total_sum_template_weight
        else:
            return result * self.average_total_sum_weight

    def sum_of_percentages(self, sum_percentages):
        return (1 + sum_percentages) * self.sum_of_percentages_weight

    def template_chance(self, chance):
        return (1 + chance) * self.template_chance_weight
