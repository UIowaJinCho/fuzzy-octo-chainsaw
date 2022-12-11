from Helpers.MessagePrompt import PromptInputMessage
import Model.TM as tm
"""
Driver for the TM simulation
Author: Hyinjin Cho, Hieu Vu
"""

#Prompt user which TM to create and store the selectio.
TMSelection = PromptInputMessage('Select the turing machine',[turingmachine for turingmachine in dir(tm) if not turingmachine.startswith('__')])

#Load the turing machine and put it into variables
TuringMachine = eval('tm.%s()'%TMSelection)