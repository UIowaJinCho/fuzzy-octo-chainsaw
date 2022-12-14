from MonoTM import *
# ----------------------------------------------------------------------
# -- recognize language ab


def checkABLeft(p, q): 
    return [*checkLeft(p, 'a', q), *checkLeft(p, 'b', q)]
    
def checkABRight(p, q): 
    return [*checkRight(p, 'a', q), *checkRight(p, 'b', q)]

trans = [
    *checkRight(1, 'a', 2),
    *checkLeft(2, 'a', 1),
    *goRight(2,'b', 'a', 3)
]

ww = TM([i for i in range(1,3)], "ab", "ab*! ", ' ', '!', trans, 1, [3])

inputstr = 'aa'
acceptTest = accepts(ww, inputstr)
configText = configs(ww, 100, inputstr)
print(f"accepts(ww, '{inputstr}')= ", acceptTest)

with open('tm4.txt', 'wt') as f:
    f.write(f'TM recognizes language ab, runs with input string: {inputstr}\n')
    f.write('TM Information:\n' + str(ww))
    f.write(f'\n\nAccepted the input string: {acceptTest}')    
    f.write(f'\n\nHistory:\n'+str(configText))
