
class Analizer(object):

    def name(self):
        pass

    def analize(self, file_name):
        pass

    def clean(self, file_name):
        pass


class Sample3Analizer(Analizer):

    def analize(self, file_name):
        print 'sample3. file name to analize... ', file_name
        clean = True
        return clean

    def clean(self, file_name):
        print 'sample3. file name to clean... ', file_name