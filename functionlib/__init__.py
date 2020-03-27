# sheet/functionlib/__init__.py

# import economyfunction
import functionlib.logicalfunction as logicalfunction
import functionlib.mathfunction as mathfunction
import functionlib.statisticalfunction as statisticalfunction
# import textfunction

def functions():
    # functions = economyfunctions
    functions= logicalfunction.functions
    functions.update(mathfunction.functions)
    functions.update(statisticalfunction.functions)
    # functions.update(textfunction.functions)
    return functions
