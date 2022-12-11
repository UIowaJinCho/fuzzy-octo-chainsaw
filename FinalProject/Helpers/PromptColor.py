"""
This script is to print in command prompt with colors
Author: Hyinjin Cho, Hieu Vu
"""

#Print in Blue in terminal
def StringInBlue(string):
    return ('%s'+ string +'%s') %('\033[34m','\033[0m')

#Print in Red in terminal
def StringInRed(string):
    return ('%s'+ string +'%s') %('\033[31m','\033[0m')