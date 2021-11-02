from physical import *

# we need these to change the python search path so we can load custom modules
import sys
import os

# add the current dir to python search path
parent = os.path.dirname(__file__)
sys.path.append(parent)

import clr
sys.path.append(parent+os.path.sep+"hello_world\\bin\\Debug")
clr.AddReference("hello_world")
import hello_world

print hello_world.Greeter.Print("Bill")

