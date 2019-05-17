
from detect_clean_sample3 import Sample3Analizer, Analizer

analizer_list =  {"sample3": Sample3Analizer(), "sample4" : Analizer()}

def analize(file_name, analizer):
    sample_clean = analizer.analize(file_name)
    print '-->', analizer.name(), 'file name to analize... ', file_name, ' was clean ', sample_clean
    return sample_clean
    # More to add

def analize(file_name):
    all_clean = True
    for name, analizer in analizer_list.items():
        sample_clean = analizer.analize(file_name)
        all_clean = all_clean and sample_clean
    print 'file name to analize... ', file_name, ' ALL CLEAN.... ', all_clean
    # More to add


def clean(file_name):
    clean(file_name)
    print 'all cleant'
    return


