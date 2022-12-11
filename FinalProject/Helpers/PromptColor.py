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

#Underline for the currently working character(will be used later)
def StringWorkingString(string,i):
    return (string[0:i]+'%s'+ string[i] +'%s'+string[i+1:]) %('\033[4m','\033[0m')