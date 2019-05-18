
import sys, getopt

# h - help
# d - detect
# c - clean
from detect_clean import analyze, clean


def print_help():
    print 'Eventually I will write some help to print on screen here XD'


def main(argv):
    sampleFile = ''
    try:
        opts, remainder_args = getopt.getopt(argv, "hac", ["analyze", "clean"])
    except getopt.GetoptError:
        print 'usage >> analyze.py -ac <sample_file>'
        sys.exit(2)

    if remainder_args is None or len(remainder_args) != 1:
        print 'no sample file argument passed'
        print_help()
        sys.exit(2)

    file_name = remainder_args[0]

    for opt, arg in opts:
        if opt == '-h':
            print_help
        elif opt in ('-a', '--analyze'):
            analyze(file_name)
        elif opt in ('-c', '--clean'):
            clean(file_name)
        else:
            print 'Wrong combination of parameters entered'
            print_help


if __name__ == "__main__":
   main(sys.argv[1:])