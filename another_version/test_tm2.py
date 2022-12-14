from MonoTM import *
# ----------------------------------------------------------------------
# -- recognize language { ww | w in {a,b}* }


def checkABLeft(p, q): 
    return [*checkLeft(p, 'a', q), *checkLeft(p, 'b', q)]
    
def checkABRight(p, q): 
    return [*checkRight(p, 'a', q), *checkRight(p, 'b', q)]

trans = [
    # -- [w2] (i) nondeterministically pick an a and erase it
    *loopRight(1, "ab"),
    *goLeft(1, 'a', '*', 2),

    # -- [w2] (ii) erase a b
    *goLeft(1, 'b', '*', 8),

    # ------------------------------------------
    # -- the a loop
    # ------------------------------------------
    
    # -- [w1] move left through a's and b's only until hitting erasure or left end, then erase matching a
    *loopLeft(2, "ab"),
    *checkRight(2, '*', 12),
    *checkRight(2, '!', 12),
    *goRight(12, 'a', '*', 3),
    
    # -- [w1] skip a's and b's to get to w2
    *loopRight(3, "ab"),

    # -- [w2] skip erasures moving right
    *checkRight(3, '*', 4),
    *loopRight(4, "*" ),

    # -- [w2] (i) erase first a encountered, then skip all the erasures moving left
    *goLeft(4, 'a', '*', 5),
    *loopLeft(5, "*" ),

    # -- [w1] (a) skip at least one a or b to move back to the start of the a loop
    *checkABLeft(5, 2), 

    # -- [w1] (b) instead nondeterministically erase an a, because otherwise you might be moving to the left of the last remaining a
    *goRight(5, 'a', '*', 3),

    # -- [w2] (ii) if instead of an a, you see b, drop down to the b loop
    *goLeft(4, 'b', '*', 11),

    # -- [w2] skip erasures
    *loopLeft(11, "*" ),

    # -- [w1] (a) skip at least one a or b to move back to start of the b loop
    *checkABLeft(11, 8), 

    # -- [w1] (b) instead nondeterministically erase a b, since otherwise you might move past the last remaining b
    *goRight(11, 'b', '*', 9),

    # ------------------------------------------
    # -- the b loop
    # ------------------------------------------

    # -- [w1] move left through a's and b's to erase a b
    *loopLeft(8, "ab"),
    *checkRight(8, '*', 13),
    *checkRight(8, '!', 13),
    *goRight(13, 'b', '*', 9),
    
    # -- [w1] skip a's and b's to get to w2
    *loopRight(9, "ab"),

    # -- [w2] skip erasures moving right
    *checkRight(9, '*', 10),
    *loopRight(10, "*" ),

    # -- [w2] (i) erase first b encountered, then skip all the erasures moving left
    *goLeft(10, 'b', '*', 11),

    # -- [w2] (ii) if instead of a b, you see an a, pop up to the a loop
    *goLeft(10, 'a', '*', 5),

    # ---------------------------------
    # -- check all erased
    # ---------------------------------

    # -- if we reach a blank (so after w2)
    *checkLeft(4, ' ', 6),
    *checkLeft(10, ' ', 6),

    # -- skip all erasures, looking for the left endmarker
    *loopLeft(6, "*" ),
    *checkRight(6, '!', 7)
]

ww = TM([i for i in range(1,13)], "abc", "abc*! ", ' ', '!', trans, 1, [7])

inputstr = 'aa'
acceptTest = accepts(ww, inputstr)
configText = configs(ww, 20, inputstr)
print(f"accepts(ww, '{inputstr}')=", acceptTest)

with open('tm2.txt', 'wt') as f:
    f.write(f'TM recognizes language {{ ww | w in {{a,b}}* }}, runs with input string: {inputstr}\n')
    f.write('TM Information:\n' + str(ww))
    f.write(f'\n\nAccepted the input string: {acceptTest}')    
    f.write(f'\n\nHistory:\n'+str(configText))

