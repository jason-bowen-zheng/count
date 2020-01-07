# count Extra Module
#
# Please Read This File CAREFULLY
#
# NOTE:
#  Every file(extra/*.py) must have a search()
#  function, set of all function in this
#  module, Or raise a error like this:
#   > ERROR: 'module' is a broken module
#
# NOTE:
#  There are some rules for search()
#   - If you don't want to return anything,
#     you must return None.
#   - If you want to return a command to
#     run, you should return:
#     > {'c':'command'}
#   - If you want to return a new data table,
#     you should return:
#     > {'d[-]':[data], 'l[-]':[list]}
#   - If function not exist, you must return
#     False
#
# NOTE:
# This version was too simple to found
# same name in different module. So you
# must be careful!
