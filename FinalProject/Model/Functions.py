"""
These are the required functions
Author: Hyinjin Cho, Hieu Vu
"""

from Helpers.PromptColor import StringInRed,StringInBlue


def CreateTM(list):
    print(StringInRed("Disabled, just a place holder for consistency to the requirements."))
    print(StringInRed("Please refer to TM.py to create turing machines."))

def ChowTM(TM):
    print("States:\t\t"  + str(TM[0]))
    print("Inputs:\t\t"  + str(TM[1]))
    print("TapeSyms:\t"+ str(TM[2]))
    print("Blank:\t\t\'"   + TM[3]+"\'")
    print("Leftend:\t" + TM[4])
    print("Trans:")
    for states in TM[0]:
        print("\t\t" + str(TM[5][states]))
    print("Start:\t"   + str(TM[7]))
    print("Final:\t"   + str(TM[8]))

def ShowConfig(TM):
    #I actually dont know which config he wants us to print here
    print()

def ShowHistory(TM):
    #what history? based on what?
    print()

def InitialConfig(TM):
    print(StringInRed("Disabled, just a place holder for consistency to the requirements."))
    print(StringInRed("Please refer to TM.py to put initial configuration."))

def Configs(TM):

    #This is base for each run, I will probably work on it more so that I will put this in a method and 
    #other "running" functions just make use of one function.
    [States, Inputs, TapeSyms, Blank,Leftend, TransInput, Trans, Start, Final, InitialConfig, Readhead] = TM
    print(StringInBlue("How many steps do you want to run?"))
    Steps = int(input())
    print(StringInBlue("Insert the input string for this run:"))
    InitialConfig = Leftend+input()
    Readhead = 1
    CurrentState = Start 
    for i in range(Steps):
        if(Readhead>=len(InitialConfig)):
            InitialConfig = InitialConfig + ' '
        char = InitialConfig[Readhead]
        try:    
            trans = Trans[CurrentState][[item[0] for item in Trans[CurrentState]].index(char)]
            if trans[1] == '/':
                InitialConfig = InitialConfig[0:Readhead] + trans[2] + InitialConfig[Readhead+1:]
                Readhead+=1
                CurrentState = trans[3]
            else:
                InitialConfig = InitialConfig[0:Readhead] + trans[2] + InitialConfig[Readhead+1:]
                Readhead-=1
                CurrentState = trans[3]
        except:
            print(StringInRed("No matching character. Does not accept"))
            return
        print(InitialConfig + "\t\tState:"+str(CurrentState)+"\t\Readhead:"+str(Readhead))

def accepting(TM):
    print()

def accepts(TM):
    print()

