# xSheets/functionlib/statisticalfunction.py

def statistical_average(seq):
    '''Statistical function
list
average(seq) => float
return average number of seq.'''
    l = []
    for x in seq:
        if x:
            l.append(x)
    else:
        return static.fmean(l)

def statistical_sum(seq):
    '''Statistical function
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
    'average':  statistical_average,
    'sum':      statistical_sum
    }
