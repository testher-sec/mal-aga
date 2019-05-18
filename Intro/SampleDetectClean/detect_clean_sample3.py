
class Analyzer(object):

    def name(self):
        pass

    def has_problem(self, file_name):
        pass

    def clean(self, file_name):
        pass


class Sample3Analyzer(Analyzer):

    def name(self):
        return "Sample3 Analyzer"

    def has_problem(self, file_name):
        string_found = "Si quieres el titulo de experto... desinfectame xDDDDDDDD"
        with open(file_name, 'rb') as f:
            s = f.read()
        found = s.find(string_found)
        message = "File is infected... Watch out" if found is not -1 else "File is clean... No problem"
        print file_name, " :: ", message
        return found > 0

    def clean(self, file_name):
        output_file_name = 'cleant_' + file_name
        with open(file_name, 'rb') as in_file:
            with open(output_file_name, 'wb') as out_file:
                out_file.write(in_file.read()[847:])
        return True

