from typing import Iterable, List, SupportsIndex, Union, Callable, Any, Generator

State = int
Tape = str
Input = str
GoLeft, GoRight = 'L', 'R'
Direction = Union[GoLeft, GoRight]


# ----------------------------------------------------------------------
# -- createTM
# ----------------------------------------------------------------------
class Trans:
    def __init__(self,
        src: State,
        tape1: Tape,
        direction: Direction,
        dest: State,
        tape2: Tape) -> None:
        
        self.src = src
        self.tape1 = tape1
        self.direction = direction
        self.dest = dest
        self.tape2 = tape2
        
    def __repr__(self) -> str:
        res = f"{self.src} === '{self.tape1}'"\
              f" / '{self.tape2}' {self.direction} ===> {self.dest}"
        return res


def showListTrans(trans: List[Trans]) -> str:
    res_str = ""
    for tran in trans:
        res_str += "  " + str(tran) + "\n"
    return res_str

class TM:
    def __init__(self,
        states : List[State], # Q: all states.  
        inputs : List[Input], # Sigma: all possible inputs.
        tapesyms : List[Tape], # Gamma: all possible stack symbols.
        blank : Tape, # blank symbol
        leftend : Tape, # left endmarker
        trans : List[Trans], # R: transition relation
        start : State, # start state
        final : List[State] # final states
        ) -> None:

        self.states = states 
        self.inputs = inputs 
        self.tapesyms= tapesyms
        self.blank = blank 
        self.leftend = leftend 
        self.trans = trans 
        self.start = start 
        self.final = final 
    
    def __repr__(self) -> str:
        res = \
        "States: " + str(self.states) + "\n" \
        "Alphabet: " + str(self.inputs) + "\n" \
        "Tape symbols: " + str(self.tapesyms) + "\n"\
        "Blank: " + self.blank + "\n" \
        "Leftend: " + self.leftend + "\n" \
        "Transitions:\n" + showListTrans(self.trans) + "\n" \
        "Start state: " + str(self.start) + "\n" \
        "Final states: " + str(self.final)
        return res

# ----------------------------------------------------------------------
# -- Config & History
# ----------------------------------------------------------------------
class InfiniteStr(str):
    def __init__(self, core: Iterable, cache=' ') -> None:
        self.core = core
        self.cache = cache

    def __getitem__(self, i: Union[SupportsIndex, slice]) -> str:
        if isinstance(i, slice):
            stop = i.stop
            if stop is None: stop = i.start
        else:
            stop = i

        if stop >= len(self.core):
            temp = [self.cache] * (stop+1 - len(self.core))
            self.core = self.core + "".join(temp)
        
        return self.core[i]
        
    def __str__(self) -> str:
        cache_index = self.core.index(self.cache)
        return self.core[:cache_index]

class Config:
    def __init__(self, 
        state: State, 
        blank: Tape, 
        leftrev: List[Tape], 
        right: List[Tape]) -> None:
        '''
        Create a Config, which describe a snapshot of a run in a TM
        Including: 
            - current state
            - tape content & current readhead position, both are encoded by:
                - leftrev: reverse of the content of left part of the tape w.r.t. the readhead (readhead is on the first component of leftrev)
                - right: content of the right part of the tape
        '''
        
        self.state = state
        self.blank = blank
        self.leftrev = "".join(leftrev)
        self.right = InfiniteStr("".join(right + self.blank))

    def __repr__(self) -> str:
        '''
        show (Config st blank leftrev right) =
        "[" ++ show st ++ ": " ++ (show $ reverse leftrev) ++ " " ++ (show $ takeWhile      (/= blank) right) ++ "]"
        ''' # TODO takeWhile (/= blank) right
        res = f'[{self.state}: "{self.leftrev[::-1]}" "{self.right}"]'
        return res

Configs = List[Config]

class History:
    def __init__(self, configs: List[Configs]) -> None:
        assert isinstance(configs, list)
        if len(configs) > 0: assert isinstance(configs[0], list)

        self.openHistory = configs
    
    def __repr__(self) -> str:
        res = ""
        for configs in self.openHistory:
            res += f"{configs}\n"
        return res

    def __getitem__(self, i):
        return self.openHistory[i]


def showConfig(config: Config) -> str:
    print(config)

def showHistory(history: History) -> str:
    '''
    show (History css) = 
    foldr (\ cs str -> show cs ++ "\n" ++ str) "" css
    '''
    print(history)

def newConfigs(tm: TM, config: Config) -> Configs:
    '''
    Given a TM, and a config, we check all possible way we can get to from that config.

    From list of transitions of the given TM, pick all transitions that has
        - source state equals to the given config's state
        - read character matches the character in the config's readhead points at
        - save a tuple with that transition info: 
        (destination state, written character, direction)
    For each match transition, create a new config
    Return list of possible configs 
    '''
    def shiftConfig(config: Config, direction: Direction) -> Config:
        '''
        Given a config and a direction, *move readhead* to the new position
        corresponding the moving direction.
        Return a new config object. 
        '''
        leftrev = config.leftrev
        right = config.right
        if direction == GoLeft:
            new_leftrev = leftrev[1:]
            new_right = leftrev[0] + right
        elif direction == GoRight:
            new_leftrev = right[0] + leftrev
            new_right = right[1:]
        return Config(config.state, config.blank, new_leftrev, new_right)

    def updateConfig(config: Config, 
        new_state: State, 
        new_tape: Tape,
        direction: Direction) -> Config:
        '''
        Given a config, a new state, a character, and a direction.
        First *rewrite the character*, then shift the given config, 
        to a new one corresponding to that information.

        This function assume the transition is valid (a valid move of a 
        given TM, only used inside an other function, not a standalone function)
        '''
        new_leftrev = [new_tape] + list(config.leftrev[1:])
        new_config = Config(new_state, config.blank, new_leftrev, config.right)
        return shiftConfig(new_config, direction)


    nexts = [(tran.dest, tran.tape2, tran.direction) for tran in tm.trans 
                if (config.state == tran.src) and (config.leftrev[0] == tran.tape1)]

    res = []
    for st, c, d in nexts:
        res.append(updateConfig(config, st, c, d))
    return res

# ----------------------------------------------------------------------
# -- initialConfig
# ----------------------------------------------------------------------
def initialConfig(tm: TM, input_str: List[Input]) -> Config:
    '''
    Given a TM and a string of input characters, and return the initial
    configuration of the machine, where the left endmarker is at very first cell 
    of the tape, then the input string comes next, and the readhead points to the
    start of the input string.
    '''
    return Config(tm.start, tm.blank, [input_str[0], tm.leftend], input_str[1:]) # TODO: infinite lazy array for "right"


def iterate(func: Callable, ele: Any):
    '''
    Simulate iterate function in haskell,
    taking a function, apply it to the ele to get result,
    keep applying the function with the result.
    
    This only create a generator to generate required elements, 
    can't create a list with lazy style in haskell
    '''
    res = ele
    while True:
        yield res
        res = func(res)
    
def take(n: int, generator: Generator):
    '''
    Simulate take funtion in haskell,
    taking n elements taken from a generator to create a list
    '''
    vals = []
    for _ in range(n):
        vals.append(next(generator))
    return vals

def configsLazy(tm: TM, input_str: List[Input]) -> Generator:
    '''
    Create a generator that generate configs with Breadth-first style, 
    keep appending configs corresponding to possible ways of moving,
    until there is no way to move, or terminate at a specific step
    '''
    def addNew(arr):
        if len(arr) == 0: return arr
        return arr[1:] + newConfigs(tm, arr[0])
    return iterate(addNew, [initialConfig(tm, input_str)])

def configs(tm: TM, step: int, input_str: List[Input]) -> History:
    '''
    Takes a TM, a number of steps to run the simulation, and an input string, 
    and returns the History representing running the given nondeterministic TM 
    that many steps.
    '''
    history = take(step, configsLazy(tm, input_str))
    history = History(history)
    return history

def configs_finite(tm: TM, step: int, input_str: List[Input]) -> History:
    '''
    Finite version, more intuitive implementation.

    Takes a TM, a number of steps to run the simulation, and an input string, 
    and returns the History representing running the given nondeterministic TM 
    that many steps.

    This is like running TM in breadth-first manner:
        - initalize history with initalConfig of the given tm
        - initialize the queue with the initaliConfig
        - For each step:
            - take the first element in the queue
            - check all possible way to go and append them into queue
            - take a snapshot of the queue append to history
    '''
    histories = [[initialConfig(tm, input_str)]]
    queue = [histories[0][0]]
    def BFS(queue):
        if len(queue) == 0: 
            return queue
        else:
            return queue[1:] + newConfigs(tm, queue[0])

    for i in range(step):
        queue = BFS(queue)
        histories.append(queue)

    return History(histories)


# ----------------------------------------------------------------------
# -- accepts
# ----------------------------------------------------------------------
def accepts(tm: TM, input_str: List[Input], max_step=5000) -> bool:
    '''
    takes a TM and an input string, tries to return the first 
    Config it finds whose state is a final state.

    max_step prevents infinite loop
    '''
    final_states = set(tm.final)

    def acceptingConfig(configs: Configs):
        if len(configs) == 0: return False

        config = configs[0] 
        if config.state in final_states:
            return True
        
        return False

    config_generator = configsLazy(tm, input_str)
    
    history = []
    for i in range(max_step):
        config = next(config_generator)
        if len(config) > 0:
            history.append(config)
        else:
            break
    
    for configs in history:
        if acceptingConfig(configs):
            return True
    
    return False



# ----------------------------------------------------------------------
# -- support functions for creating transitions
# ----------------------------------------------------------------------
def epsEdge(p: State, intermediate: State, q: State, ts: List[Tape]):
    '''
    transition from p to q with no change to the tape or readhead position
    '''
    all_trans = []
    for t in ts:
        eps_trans = [Trans(p, t, GoRight, intermediate, t),
                    Trans(intermediate, t, GoLeft, q, t)]
        all_trans.extend(eps_trans)
    return all_trans

def goRight(st: State, g: Tape, g1: Tape, st1: State) -> Trans:
    '''
    Create a list of one transition that corresponds to:
    - moving from current state st to another state st1
    - rewrite the character from g to g1
    - move the readhead to the right
    '''
    return [Trans(st, g, GoRight, st1, g1)]

def goLeft(st: State, g: Tape, g1: Tape, st1: State) -> Trans:
    '''
    Create a list of one transition that corresponds to:
    - moving from current state st to another state st1
    - rewrite the character from g to g1
    - move the readhead to the left
    '''
    return [Trans(st, g, GoLeft, st1, g1)]


def checkRight(p: State, g: Tape, q: State):
    '''
    goRight without changing tape character
    '''
    return goRight(p, g, g, q)

def checkLeft(p: State, g: Tape, q: State):
    '''
    goLeft without changing tape character
    '''
    return goLeft(p, g, g, q)

def loopRight(st: State, gs: List[Tape]) -> List[Trans]:
    '''
    A loop at the current state, 
    keep moving readhead right without changing the tape content
    '''
    all_trans = [Trans(st, g, GoRight, st, g) for g in gs]
    return all_trans

def loopLeft(st: State, gs: List[Tape]) -> List[Trans]:
    '''
    A loop at the current state, 
    keep moving readhead right without changing the tape content
    '''
    all_trans = [Trans(st, g, GoLeft, st, g) for g in gs]
    return all_trans
