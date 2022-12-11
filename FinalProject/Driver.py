from Helpers.MessagePrompt import PromptFilterInputMessage
import Model.TM as tm
"""
Driver for the TM simulation
Author: Hyinjin Cho, Hieu Vu
"""

#Prompt user which TM to create and store the selectio.
TM = PromptFilterInputMessage('Select the turing machine',[turingmachine for turingmachine in dir(tm) if not turingmachine.startswith('__')])
print(TM)