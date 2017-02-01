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
Usage: python process.py [OPTIONS]
Tries to get a better chance of winning mega sena.
   -f, --file                     Mega Sena file name
   -q, --quantity                 The total of numbers available to be draw, defaults to 60
   -m, --max                      Total of draw numbers, defaults to 6.
   -h, --howmany                  Number of possible 6 numbers to be draw with higher probability

"""

    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:q:m:h:", ["file=", "quantity=", "max=", "howmany="])
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
            possible_numbers = int(a)
        elif o in ("-m", "--max"):
            max_guesses = int(a)
        elif o in ("-h", "--howmany"):
            how_many = int(a)
        else:
            assert False, "Unhandled option"

    if not mega_sena_file:
        print "Parameters not specified!"
        usage()
        sys.exit(2)

    numbers_module = NumbersWithHIghChanceOfWinning(mega_sena_file)

    start_time = time.time()
    numbers = []

    if len(args) == 0:
        numbers = random.sample(range(1, possible_numbers), max_guesses)
    elif len(args) > 0:
        numbers = args

    results = map(int, numbers)
    results.sort()

    numbers_len = len(numbers)

    c = Color(possible_numbers, max_guesses, numbers_module.num_of_contests, numbers_module)

    p = Probability(possible_numbers, max_guesses, numbers_len)

    if how_many == 1:
        w = CalculateWeights()

        table = PrettyTable(["Description", "Value"])
        table.add_row(["Sequence", results])

        table.add_row(["Probability getting 6 correct (1 in)", p.sena()])
        table.add_row(["Probability getting 5 correct (1 in)", p.quina()])
        table.add_row(["Probability getting 4 correct (1 in)", p.quadra()])

        w.weight = 1.0 / p.sena()

        sum_numbers = sum(results)

        table.add_row(["Sequence sum", sum_numbers])

        w.weight *= w.close_to_average_total_sum(sum_numbers, numbers_module.average_total_sum)

        guessed = numbers_module.get_date_of_numbers(results)

        if guessed is not None:
            table.add_row(["Sequence already draw at", guessed])
            w.weight *= 0
        else:
            print "========> Number never draw before!"
            w.weight *= 1

        percentages = []

        for i in results:
            percentage = numbers_module.percentage_of_number[i] * 100
            table.add_row(["Probability of number " + str(i),
                           "{0:.2f}%".format(percentage)])
            percentages += [percentage]

        w.weight *= w.sum_of_percentages(sum(percentages))

        table.add_row(["Total number of drawings", numbers_module.num_of_contests])
        table.add_row(["Total number of drawings with winners", numbers_module.get_won_contests()])

        if numbers_len == 6:

            dict_templates = c.templates[what_template(results)]

            for key, value in dict_templates.items():
                table.add_row([key, value])

            w.weight *= w.template_chance(float(dict_templates['Probability'][:-1])/100)

            w.weight *= w.close_to_average_total_sum(sum_numbers, int(dict_templates['Average sum']), True)

        print table

        print "========> Chance of winning:", "{0:.10f}%".format(w.weight)
    else:
        progress = 1
        dict_of_percentages = {}
        for num in itertools.combinations(xrange(1, possible_numbers + 1), max_guesses):
            progress += 1
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

                w.weight *= w.template_chance(float(dict_templates['Probability'][:-1]) / 100)

                w.weight *= w.close_to_average_total_sum(sum_numbers, int(dict_templates['Average sum']), True)

            dict_of_percentages[num] = format(w.weight)
            print progress

        print dict(sorted(dict_of_percentages.iteritems(), key=operator.itemgetter(1), reverse=True)[:how_many])

    print("--- Total %s seconds ---" % (time.time() - start_time))
