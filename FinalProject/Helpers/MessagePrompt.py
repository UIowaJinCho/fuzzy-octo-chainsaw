from Helpers.PromptColor import *
import re

"""
Prompt user to select TM
Author: Hyinjin Cho, Hieu Vu
"""

def PromptInputMessage(question,list):
    
    #print user the question
    print(StringInBlue(question))
    
    #supply the selection
    # for i in range(len(list)): 
    for i, option in enumerate(list, start=1):
        print(StringInBlue("%i:%s"%(i,option)))
    
    #Exception handling
    try:
        Input = int(input())
        # if the number is not in range .. etc
        if Input < 0:
            return list[Input]
        else:
            return list[Input-1]
    except Exception:
        raise Exception(StringInRed("Invalid selection."))

def PromptTuringMachineInputMessage(question,list):
    
    #((\d+,)+\d+)|((\d+ )+\d+)| for commas and white spaces (1 2 3 or 1,2,3 runs for 1 2 and 3)
    #\d+-\d+ for multiple selection, e.g. (1-2 runs for 1 to 2)

    #print user the question
    print(StringInBlue(question))
    
    #supply the selection
    # for i in range(len(list)): 
    for i, option in enumerate(list, start=1):
        print(StringInBlue("%i:%s"%(i,option)))
    
    #handle each cases based on input regular expression
    try:
        UserInput = input()

        if(re.match('\d+-\d+',UserInput)):
            tokens = UserInput.split('-')
            print(tokens)
            return list[int(tokens[0])-1:int(tokens[1])]

        elif(re.match('((\d+,)+\d+)',UserInput)):
            tokens = UserInput.split(',')
            print(tokens)
            filterList = []
            for token in tokens:
                filterList.append(list[int(token)-1])
            return filterList

        elif(re.match('((\d+ )+\d+)',UserInput)):
            tokens = UserInput.split(' ')
            print(tokens)
            filterList = []
            for token in tokens:
                filterList.append(list[int(token)-1])
            return filterList
        else:
            return [list[int(UserInput)-1]]
    except Exception:
        raise Exception(StringInRed("Invalid selection."))

