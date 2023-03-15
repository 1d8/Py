import math

def GetSQRoot(number):
    try:
        return math.sqrt(number)
    except TypeError:
        return "Error: You must input an integer!"

