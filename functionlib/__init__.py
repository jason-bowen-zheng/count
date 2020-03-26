# sheet/functionlib/__init__.py

# import economyfunction
import functionlib.logicalfunction as logicalfunction
import functionlib.mathfunction as mathfunction
import functionlib.statisticsfunction as statisticsfunction
# import textfunction

def functions():
    # functions = economyfunctions
    functions= logicalfunction.functions
    functions.update(mathfunction.functions)
    functions.update(statisticsfunction.functions)
    # functions.update(textfunction.functions)
    return functions
