
from detect_clean_sample3 import Sample3Analyzer, Analyzer

analyzer_list =  {"sample3": Sample3Analyzer()} #, "sample4" : Analyzer()}

def __analyze(file_name, analyzer):
    dirty = analyzer.has_problem(file_name)
    print '-->', analyzer.name(), '::file name to analyze... ', file_name, ' has a friend... ', dirty
    return dirty
    # More to add

def analyze(file_name):
    all_clean = True
    for name, analyzer in analyzer_list.items():
        sample_dirty = __analyze(file_name, analyzer)
        if sample_dirty:
            all_clean = False
    print "--------> ", file_name, ' CLEAN....? ', all_clean
    # More to add


def clean(file_name):
    all_clean = True
    for name, analyzer in analyzer_list.items():
        if analyzer.has_problem(file_name):
            ok = __clean(file_name, analyzer)
            all_clean = all_clean and ok
    print "--------> ", file_name, ' ALL CLEAN.... ', all_clean
    return

def __clean(file_name, analyzer):
    ok = analyzer.clean(file_name)
    print file_name , ' --> cleant from ... ', analyzer.name(), ' was ', ok
    return ok


