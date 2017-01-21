import sys
import getopt
from modules.numbers import NumbersWithHIghChanceOfWinning

if __name__ == '__main__':

    def usage():
        print """\
Usage: mega_sena [OPTIONS]
Tries to get a better chance of winning mega sena.
   -f, --file                     Mega Sena file name
"""

    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:", ["file="])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    mega_sena_file = None

    for o, a in opts:
        if o in ("-f", "--file"):
            mega_sena_file = a
        else:
            assert False, "Unhandled option"

    if not mega_sena_file:
        print "Parameters not specified!"
        usage()
        sys.exit(2)

    numbers_module = NumbersWithHIghChanceOfWinning(mega_sena_file)

    print numbers_module.percentage_of_number[5]

    print numbers_module.unique_sequences
