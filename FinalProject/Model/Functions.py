"""
These are the required functions
Author: Hyinjin Cho, Hieu Vu
"""

from Helpers.PromptColor import StringInRed,StringInBlue,StringWorkingString


#Creating TM with terminal was annoying, so I created the TM.py to make TMs.
#if you just declare a def there, it will show in the terminal prompt.
def CreateTM(list):
    print(StringInRed("Disabled, just a place holder for consistency to the requirements."))
    print(StringInRed("Please refer to TM.py to create turing machines."))

#basic printing. Simple enough
def ShowTM(TM):
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

#I don't know what to do with this either, will talk to the professor
def InitialConfig(TM):
    print(StringInRed("Disabled, just a place holder for consistency to the requirements."))
    print(StringInRed("Please refer to TM.py to put initial configuration."))

def Configs(TM):

    #This is base for each run, I will probably work on it more so that I will put this in a method and 
    #other "running" functions just make use of one function.
    #Confirm returning solution with Hieu tomorrow, different than my hw solution.

    #just putting TM into specific variables
    [States, Inputs, TapeSyms, Blank,Leftend, TransInput, Trans, Start, Final, InitialConfig, Readhead] = TM

    # Ask the user how many runs and the input string
    print(StringInBlue("How many steps do you want to run?"))
    Steps = int(input())
    print(StringInBlue("Insert the input string for this run:"))

    #start with the input at Readhead at index 1 and start state.
    InitialConfig = Leftend+input()
    Readhead = 1
    CurrentState = Start 

    print("Steps:")
    #in the number of steps..
    import pdb;pdb.set_trace()
    for i in range(Steps):
        #if tape is at the end, just append empty space at the corresponding index
        if(Readhead>=len(InitialConfig)):
            InitialConfig = InitialConfig + ' '

        #Debugging and printing purpose.
        # print("\t"+StringWorkingString(InitialConfig,Readhead) + "\t\tState:"+str(CurrentState)+"\t\tReadhead:"+str(Readhead))
        #I will update tomorrow to put the "currently working char"
        print("\t"+str(i)+".\t"+StringWorkingString(InitialConfig,Readhead) + "\t\tState:"+str(CurrentState))

        
        #take the currently working character
        char = InitialConfig[Readhead]

        #if we currentchar does not match any of the transition options, raise exception
        try: 
            #otherwise, get the corresponding transition   
            trans = Trans[CurrentState][[item[0] for item in Trans[CurrentState]].index(char)]
            #Right
            if trans[1] == '/':
                InitialConfig = InitialConfig[0:Readhead] + trans[2] + InitialConfig[Readhead+1:]
                Readhead+=1
                CurrentState = trans[3]
            #Left
            else:
                InitialConfig = InitialConfig[0:Readhead] + trans[2] + InitialConfig[Readhead+1:]
                Readhead-=1
                CurrentState = trans[3]
            
            #if the new state is in final state
            #print accepted and return
            if CurrentState in Final:
                print(StringInBlue("Accepted"))
                return
                
        except:
            #in case of exception, print the user it did not accept and return
            print(StringInRed("No matching character. Does not accept"))
            return

def accepting(TM):
    print()

def accepts(TM):
    print()

