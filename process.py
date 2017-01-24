import sys
import getopt

from modules.colors import Color
from modules.numbers import NumbersWithHIghChanceOfWinning
from modules.probability import Probability
from prettytable import PrettyTable

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
        results = map(int, args)
        results.sort()

        table = PrettyTable(["Descricao", "Valor"])

        p = Probability(possible_numbers, max_guesses, len(args))
        table.add_row(["Probabilidade da sena (1 em)", p.sena()])
        table.add_row(["Probabilidade da quina (1 em)", p.quina()])
        table.add_row(["Probabilidade da quadra (1 em)", p.quadra()])

        guessed = numbers_module.get_date_of_numbers(results)

        if guessed is not None:
            table.add_row(["Sequencia ja sorteada em", guessed])
        else:
            print "========> Numero nunca sorteado!"

        for i in results:
            table.add_row(["Probabilidade do numero " + str(i),
                           "{0:.2f}%".format(numbers_module.percentage_of_number[i] * 100)])

        table.add_row(["Numero de sorteios", numbers_module.num_of_contests])
        table.add_row(["Sorteios com sena", numbers_module.get_won_contests()])

        print table

        c = Color(possible_numbers, max_guesses, numbers_module.num_of_contests, numbers_module)

        print c.templates[tuple(sorted(('yellow', 'light_blue', 'gray', 'green', 'pink', 'ivory')))]

