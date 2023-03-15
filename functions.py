import math

# number -> must be integer
def GetSQRoot(number):
    try:
        return math.sqrt(number)
    except TypeError:
        return "Error: You must input an integer!"

# integerList -> must be list or tuple
def GetMaxValue(integerList):
    if isinstance(integerList, list) or isinstance(integerList, tuple):
        # continue if it's list
        return max(integerList)
    else:
        return "Error: Must pass a list or tuple"

# integerList -> must be list or tuple
def GetMinValue(integerList):
    if isinstance(integerList, list) or isinstance(integerList, tuple):
        # continue if it's list
        return min(integerList)
    else:
        return "Error: Must pass a list or tuple"