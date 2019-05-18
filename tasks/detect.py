import sys

def has_problem(file_name):
    string_found = "Si quieres el titulo de experto... desinfectame xDDDDDDDD"
    with open(file_name, 'rb') as f:
        s = f.read()
    found = s.find(string_found)
    message = "File is infected... Watch out" if found is not -1 else "File is clean... No problem"
    print file_name," :: ", message


if __name__ == "__main__":
    if len(sys.argv) is not 2:
        print 'usage >> detect.py <sample_file>'
        sys.exit(2)
    has_problem(sys.argv[1])
