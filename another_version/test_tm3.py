from MonoTM import * 

# ----------------------------------------------------------------------
# -- HW4: recognize { w0:w1:...:wk| wi \in {0,1}*, exist wi = w0 }

hw4_trans = [
    *goRight(1, 'a', '*', 2), 
    *checkRight(2, 'a', 15),
    *checkRight(2, ':', 20),

    *checkRight(3, ' ', 20),
    *goLeft(3, 'a', '*', 4),

    *loopLeft(4, 'a'),
    *checkLeft(4, ':', 5),

    *checkLeft(5, 'a', 5),
    *goRight(5, '*', 'a',  6),

    *checkRight(6, ':',  7),
    *goRight(6, 'a', '*', 12),

    *loopRight(7, 'a'),
    *checkRight(7, '*',  8),

    *checkRight(8, ' ', 20),
    *checkLeft(8, 'a',  9),

    *checkLeft(9, '*', 10),

    *checkLeft(10, 'a', 10),
    *checkLeft(10, ':', 11),

    *checkLeft(11, 'a', 11),
    *checkRight(11, '!', 6),

    *checkRight(12, 'a', 12),
    *checkRight(12, ':', 13),

    *checkRight(13, 'a', 13),
    *goRight(13, '*', 'a', 14),

    *goLeft(14, 'a' , '*',  4),

    *loopRight(15, 'a'),
    *checkRight(15, ':',  3)
]

hw4 = TM(
    [i for i in range(1, 21)],
    "ab:* ",
    "ab:* !",
    ' ',
    '!', 
    hw4_trans, 
    1,
    [20]
)

inputstr = 'aa:aaa'
acceptTest = accepts(hw4, inputstr)
configText = configs(hw4, 50, inputstr)

with open('tm3.txt', 'wt') as f:
    f.write(f'TM recognizes language {{ w0:w1:...:wk| wi \in {{0,1}}*, exist wi = w0 }}, runs with input string: {inputstr}\n')
    f.write('TM Information:\n' + str(hw4))
    f.write(f'\n\nAccepted the input string: {acceptTest}')    
    f.write(f'\n\nHistory:\n'+str(configText))

