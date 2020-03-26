# sheet/functionlib/statisticsfunction.py

def statistics_average(seq):
    '''Statistics function
list
average(seq) => float
return average number of seq.'''
    l = []
    for x in seq:
        if x:
            l.append(x)
    else:
        return static.fmean(l)

def statistics_sum(seq):
    '''Statistics function
list
sum(seq) => float
return sum of seq'''
    total = 0
    for x in seq:
        if x:
            total += x
    else:
        return total

functions = {
    'average':  statistics_average,
    'sum':      statistics_sum
    }
