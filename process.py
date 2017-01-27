import sys
import getopt

from modules.colors import Color, what_template
from modules.numbers import NumbersWithHIghChanceOfWinning
from modules.probability import Probability
from prettytable import PrettyTable

from modules.weights import CalculateWeights

if __name__ == '__main__':

    possible_numbers = 60
    max_guesses = 6

    def usage():
        print """\
Usage: mega_sena [OPTIONS]
Tries to get a better chance of winning mega sena.
   -f, --file                     Mega Sena file name

"""

    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:q:m", ["file=", "quantity=", "max="])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    mega_sena_file = None

    for o, a in opts:
        if o in ("-f", "--file"):
            mega_sena_file = a
        elif o in ("-q", "--quantity"):
            possible_numbers = a
        elif o in ("-m", "--max"):
            max_guesses = a
        else:
            assert False, "Unhandled option"

    if not mega_sena_file:
        print "Parameters not specified!"
        usage()
        sys.exit(2)

    numbers_module = NumbersWithHIghChanceOfWinning(mega_sena_file)

    if len(args) > 0:
        w = CalculateWeights()

        results = map(int, args)
        results.sort()

        table = PrettyTable(["Descricao", "Valor"])

        p = Probability(possible_numbers, max_guesses, len(args))
        table.add_row(["Probabilidade da sena (1 em)", p.sena()])
        table.add_row(["Probabilidade da quina (1 em)", p.quina()])
        table.add_row(["Probabilidade da quadra (1 em)", p.quadra()])

        w.weight = 1.0 / p.sena()

        sum_numbers = sum(results)

        table.add_row(["Soma dos numeros", sum_numbers])

        w.weight *= w.close_to_average_total_sum(sum_numbers, numbers_module.average_total_sum)

        guessed = numbers_module.get_date_of_numbers(results)

        if guessed is not None:
            table.add_row(["Sequencia ja sorteada em", guessed])
            w.weight *= 0
        else:
            print "========> Numero nunca sorteado!"
            w.weight *= 1

        percentages = []

        for i in results:
            percentage = numbers_module.percentage_of_number[i] * 100
            table.add_row(["Probabilidade do numero " + str(i),
                           "{0:.2f}%".format(percentage)])
            percentages += [percentage]

        w.weight *= w.sum_of_percentages(sum(percentages))

        table.add_row(["Numero de sorteios", numbers_module.num_of_contests])
        table.add_row(["Sorteios com sena", numbers_module.get_won_contests()])

        if len(args) == 6:
            c = Color(possible_numbers, max_guesses, numbers_module.num_of_contests, numbers_module)

            dict_templates = c.templates[what_template(results)]

            for key, value in dict_templates.items():
                table.add_row([key, value])

            w.weight *= w.template_chance(float(dict_templates['Probablidade de ocorrer'][:-1])/100)

            w.weight *= w.close_to_average_total_sum(sum_numbers, int(dict_templates['Soma media']), True)

        print table

        print "========> Sua chance de ganhar:", w.weight





