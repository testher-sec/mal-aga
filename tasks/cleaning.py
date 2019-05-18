import sys


def clean_file(file_name):
    output_file_name = 'cleant_' + file_name
    with open(file_name, 'rb') as in_file:
        with open(output_file_name, 'wb') as out_file:
            out_file.write(in_file.read()[847:])


if __name__ == "__main__":
    if len(sys.argv) is not 2:
        print 'usage >> cleaning.py <sample_file>'
    	sys.exit(2)
    clean_file(sys.argv[1])
