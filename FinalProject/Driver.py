from Helpers.MessagePrompt import *
from Model.Functions import *
import Model.TM as tm
import Model.Functions as funcs
"""
Driver for the TM simulation
Author: Hyinjin Cho, Hieu Vu
"""

#Prompt user which TM to create and store the selectio.
TMSelection = PromptInputMessage('Select the turing machine',[turingmachine for turingmachine in dir(tm) if not turingmachine.startswith('__')])

#Load the turing machine and put it into variables
TuringMachine = eval('tm.%s()'%TMSelection)

# User prompt for the functions
# FuncSelection = PromptFunctionInputMessage('SelectFunctions (1,2,3 or 1-3 format works):',[functions for functions in dir(funcs) if not functions.startswith('__') and not functions.startswith('String') and functions!='run'])

Configs(TuringMachine)
# for func in FuncSelection:

# showTM(TuringMachine)