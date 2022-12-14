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

inputstr = 'aabbcc'
test = configs(tripletm, 35, inputstr)
print(f"configs(tripletm, 35, '{inputstr}')= ", test)

with open('tm1.txt', 'wt') as f:
    f.write(f'TM recognizes {{a^n b^n c^n | n in Nat }}, runs with input string: {inputstr}')
    f.write(str(test))

