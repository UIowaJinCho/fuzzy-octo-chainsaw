========================
Hieu Vu, Hyunjin Cho
========================

Tooling:
    We implemented our Turing machine with Python. Our implementation does 
not require any additional installation of packages, nor libraries. However, 
we can only guarantee to work with python 3.9.  

Sources: 
	MonoTM.py		 

Tests: 
    We test our implementation with 3 TMs (`test_tm1.py`, `test_tm2.py`, `test_tm3.py`), for each TM, we tested with one input string, we save the following information to the corresponding result file:
    - convert TM to string
    - show if the TM accepts the input string or not
    - show the running history (also included showing the config)
    We also add an simple TM (`test_tm4.py`) with an infinite run, we prevent the infinite runs by setting a large predefined max running steps (5000)
    
Implementation: 
    - We do it in Object-Oriented Programming style, with corresponding class defintions for Turing Machine, Transition, Config, History
    - We organize the code as in haskell code with similar function names
    - We added comments for corresponding functions
    - Required functions to convert object to string are implemented in `__repr__` in corresponding classes, so we can just call `print(obj)` or `str(obj)` to print the corresponding objects


Status: 
	Fully functional nondeterministic Turing Machine simulator. 

Course evaluation:
    we evaluated the course.