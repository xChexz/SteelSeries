import random
import sys
sys.path.insert(0, '/Modules/')
from Modules.QckPrism import Qck
from Modules.Rival700 import Rival700
from Modules.Siberia840 import Siberia840

x = int(input("""1. Qck Prism
2. Rival700
3. Siberia840
>>>"""))
if x == 1: Qck()
if x == 2: Rival700()
if x == 3: Siberia840()
