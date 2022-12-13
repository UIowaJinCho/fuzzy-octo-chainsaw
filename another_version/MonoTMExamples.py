from MonoTM import *



# ----------------------------------------------------------------------
# -- recognize {a^n b^n c^n | n in Nat }

tripletm_trans = [
                    *checkRight(1, ' ', 6),
                    *loopRight(1, "*"), 
                    *goRight(1, 'a', '*', 2),
                    *loopRight(2, "a*"),
                    *goRight(2, 'b', '*', 3),
                    *loopRight(3, "b*"),
                    *goRight(3, 'c', '*', 4),
                    *loopRight(4, "c*"),
                    *checkLeft(4, ' ', 5),
                    *loopLeft(5, "abc*"),
                    *checkRight(5, '!', 1) 
                ]
tripletm = TM([i for i in range(1,7)],
                "acb", "abc*!", ' ', '!', tripletm_trans, 1, [6])

test = configs_finite(tripletm, 35, 'aabbcc')
print("configs_finite(tripletm, 35, 'aabbcc')= ", test)
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

test2 = accepts(ww, 'aa')
print("accepts(ww, 'aa')=", test2)

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

test = configs_infinite(hw4, 20, 'aa:aa')
import pdb;pdb.set_trace()