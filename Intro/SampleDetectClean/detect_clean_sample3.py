
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
        print 'sample3. file name to analyze... ', file_name
        clean = True
        return clean

    def clean(self, file_name):
        print 'sample3. file name to clean... ', file_name
        output_file_name = 'cleant-' + file_name
        with open(file_name, 'rb') as in_file:
            with open(output_file_name, 'wb') as out_file:
                out_file.write(in_file.read()[847:])
        return True