#FUNCTIONS

import pandas as pd 
import numpy as np
import re
import os


# This function takes each string from the "date" column and returns only the year
# If the year can't be returned, it returns "unknown"
def checkDate(dateString):
    dateString=str(dateString)
    if re.findall(r'[0-9]{4}',dateString):
        return re.findall(r'[0-9]{4}',dateString)[0]
    else:
        return "unknown"

# This function takes each string from the "Species" column and returns the type of shark whenever possible
def sharkType(string):
    string = string.upper()
    if (len(re.findall(r'[A-Z]+\sSHARK', string))) > 0:
        return "".join(re.findall(r'[A-Z]+\sSHARK', string))
    else:
        return "Unknown"

# This function cleans the "Activity" column
def activity(string):
    string = string.upper()
    if (len(re.findall(r'SURF|BOARD', string))) > 0:
        return "SURFING/WATERSPORTS"
    elif (len(re.findall(r'SWIM|DIVE|BATH|DIVING|SNORKELING|WADING', string))) > 0:
        return "SWIMMING/DIVING"
    elif (len(re.findall(r'FISH', string))) > 0:
        return "FISHING"
    else:
        return string

# This function cleans the "FATAL" column to remove all the invalid inputs
def cleanFatal(string):
    string = string.upper()
    if (len(re.findall(r'Unknown|UNKNOWN|Uncertain|2017', string))) > 0:
        return "Unknown"
    elif (len(re.findall(r'Y{1}', string))) > 0:
        return "Y"
    else:
        return "N"