"""
This is our turing machine is created
Author: Hyinjin Cho, Hieu Vu
"""


#if you create a TM here, it will be visible in the terminal for running.

#this is the testing turing machine template
"""
def TuringMachineTemplate():

    #States, input in number lists
    States = [1,2,3]

    #Input characters
    Inputs = ['a','b',':','*',' ']

    #Tape symbols
    TapeSyms = ['!','']

    #Black symbols
    Blank = ' '

    #Leftend symbols
    Leftend = '!'

    #Transition user input.
    #this is so that the user can input the transitions more intuitively.
    #TransInput will be parsed to a dictionary later in the code.
    TransInput = [
            
            [  1, 'a',  '/', '*',  2 ],

            [  2, 'a',  '/', 'a',  2 ],
            [  2, ':',  '/', ':',  3 ],
        ]

    #Start state
    Start = 1

    #Final states
    Final = [20]

    #Organize the TransInput list into Trans dictionary    
    Trans = {}
    for trans in TransInput:
        #check if the key is already in the dictionary
        if trans[0] not in Trans.keys():
            Trans[trans[0]] = [trans[1:]]
        else:
            Trans[trans[0]].append(trans[1:])
    
    InitialConfig = ""

    #Return Everything into a list.
    #Might change it to object oriented later.
    return [States, Inputs, TapeSyms, Blank,Leftend, TransInput, Trans, Start, Final, InitialConfig]
"""


#this is the testing turing machine from homework 4
def TM1():

    #States, input in number lists
    States = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,20]

    #Input characters
    Inputs = ['a','b',':','*',' ']

    #Tape symbols
    TapeSyms = ['!','']

    #Black symbols
    Blank = ' '

    #Leftend symbols
    Leftend = '!'

    #Transition user input.
    #this is so that the user can input the transitions more intuitively.
    #TransInput will be parsed to a dictionary later in the code.
    TransInput = [

            
            [  1, 'a',  '/', '*',  2 ],

            [  2, 'a',  '/', 'a', 15 ],
            [  2, ':',  '/', ':', 20 ],

            [  3, ' ',  '/', ' ', 20 ],
            [  3, 'a', '\\', '*', 4 ],

            [  4, 'a', '\\', 'a', 4 ],
            [  4, ':', '\\', ':',  5 ],

            [  5, 'a',  '\\', 'a', 5 ],
            [  5, '*',  '/', 'a',  6 ],

            [  6, ':',  '/', ':',  7 ],
            [  6, 'a',  '/', '*', 12 ],

            [  7, 'a',  '/', 'a',  7 ],
            [  7, '*',  '/', '*',  8 ],

            [  8, ' ',  '/', ' ', 20 ],
            [  8, 'a', '\\', 'a',  9 ],

            [  9, '*', '\\', '*', 10 ],

            [ 10, 'a' ,'\\', 'a', 10 ],
            [ 10, ':' ,'\\', ':', 11 ],

            [ 11, 'a' ,'\\', 'a', 11 ],
            [ 11, '!' , '/', '!',  6 ],

            [ 12, 'a' , '/', 'a', 12 ],
            [ 12, ':' , '/', ':', 13 ],

            [ 13, 'a' , '/', 'a', 13 ],
            [ 13, '*' , '/', 'a', 14 ],

            [ 14, 'a' ,'\\', '*',  4 ],

            [ 15, 'a' , '/', 'a', 15 ],
            [ 15, ':' , '/', ':',  3 ]

        ]

    #Start state
    Start = 1

    #Final states
    Final = [20]

    #Organize the TransInput list into Trans dictionary    
    Trans = {}
    for trans in TransInput:
        #check if the key is already in the dictionary
        if trans[0] not in Trans.keys():
            Trans[trans[0]] = [trans[1:]]
        else:
            Trans[trans[0]].append(trans[1:])
    
    InitialConfig = "!"
    Readhead = 1

    #Return Everything into a list.
    #Might change it to object oriented later.
    return [States, Inputs, TapeSyms, Blank,Leftend, TransInput, Trans, Start, Final, InitialConfig, Readhead]
