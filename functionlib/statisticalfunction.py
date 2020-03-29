# xSheets/functionlib/statisticalfunction.py

import statistics

def statistical_average(seq):
    '''Statistical function
list
average(seq)
return average number of seq.'''
    l = []
    for x in seq:
        if x:
            l.append(x)
    else:
        return statistics.fmean(l)

def statistical_geometric_mean(seq):
    '''Statistical function
list
geometric_mean(seq)
return geometric mean of seq.'''
    l = []
    for x in seq:
        if x:
            l.append(x)
    else:
        return statistics.geometric_mean(l)

def statistical_harmonic_mean(seq):
    '''Statistical function
list
harmonic_mean(seq)
return harmonic mean of seq.'''

    l = []
    for x in seq:
        if x:
            l.append(x)
    else:
        return statistics.harmonic_mean(l)

def statistical_median(seq):
    '''Statistical function
list
geometric_mean(seq)
return median of seq.'''

    l = []
    for x in seq:
        if x:
            l.append(x)
    else:
        return statistics.median(l)

def statistical_sum(seq):
    '''Statistical function
list
sum(seq)
return sum of seq'''
    total = 0
    for x in seq:
        if x:
            total += x
    else:
        return total

functions = {
    'average':          statistical_average,
    'geometric_mean':   statistical_geometric_mean,
    'harmonic_mean':    statistical_harmonic_mean,
    'median':           statistical_median,
    'sum':              statistical_sum
    }
