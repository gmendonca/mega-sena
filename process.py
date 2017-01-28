import sys
import getopt
import random
import itertools
import operator
import time
from modules.colors import Color, what_template
from modules.numbers import NumbersWithHIghChanceOfWinning
from modules.probability import Probability
from prettytable import PrettyTable
from modules.weights import CalculateWeights

if __name__ == '__main__':
    def usage():
        print """\
Usage: mega_sena [OPTIONS]
Tries to get a better chance of winning mega sena.
   -f, --file                     Mega Sena file name

"""

    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:q:m:h", ["file=", "quantity=", "max=", "howmany="])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    mega_sena_file = None
    possible_numbers = 60
    max_guesses = 6
    how_many = 1

    for o, a in opts:
        if o in ("-f", "--file"):
            mega_sena_file = a
        elif o in ("-q", "--quantity"):
            possible_numbers = a
        elif o in ("-m", "--max"):
            max_guesses = a
        elif o in ("-h", "--howmany"):
            how_many = a
        else:
            assert False, "Unhandled option"

    if not mega_sena_file:
        print "Parameters not specified!"
        usage()
        sys.exit(2)

    numbers_module = NumbersWithHIghChanceOfWinning(mega_sena_file)
    c = Color(possible_numbers, max_guesses, numbers_module.num_of_contests, numbers_module)

    start_time = time.time()
    numbers = []

    if len(args) == 0:
        numbers = random.sample(range(1, 60), 6)
    elif len(args) > 0:
        numbers = args

    results = map(int, numbers)
    results.sort()

    numbers_len = len(numbers)

    p = Probability(possible_numbers, max_guesses, numbers_len)

    if how_many == 1:
        w = CalculateWeights()

        table = PrettyTable(["Descricao", "Valor"])
        table.add_row(["Sequencia", results])

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

        if numbers_len == 6:
            start_time_inner = time.time()
            print("--- Inner %s seconds ---" % (time.time() - start_time_inner))

            dict_templates = c.templates[what_template(results)]

            for key, value in dict_templates.items():
                table.add_row([key, value])

            w.weight *= w.template_chance(float(dict_templates['Probablidade de ocorrer'][:-1])/100)

            w.weight *= w.close_to_average_total_sum(sum_numbers, int(dict_templates['Soma media']), True)

        print table

        print "========> Sua chance de ganhar:", "{0:.5f}%".format(w.weight)
    else:
        dict_of_percentages = {}
        for num in itertools.combinations(xrange(1, 61), 6):
            w = CalculateWeights()

            w.weight = 1.0 / p.sena()

            sum_numbers = sum(results)

            w.weight *= w.close_to_average_total_sum(sum_numbers, numbers_module.average_total_sum)

            guessed = numbers_module.get_date_of_numbers(results)

            if guessed is not None:
                continue

            percentages = []

            for i in results:
                percentage = numbers_module.percentage_of_number[i] * 100
                percentages += [percentage]

            w.weight *= w.sum_of_percentages(sum(percentages))

            if numbers_len == 6:
                dict_templates = c.templates[what_template(results)]

                w.weight *= w.template_chance(float(dict_templates['Probablidade de ocorrer'][:-1]) / 100)

                w.weight *= w.close_to_average_total_sum(sum_numbers, int(dict_templates['Soma media']), True)

            dict_of_percentages[num] = format(w.weight)

        print dict(sorted(dict_of_percentages.iteritems(), key=operator.itemgetter(1), reverse=True)[:how_many])

    print("--- Total %s seconds ---" % (time.time() - start_time))






