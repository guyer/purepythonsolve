#!python2

## README:
"""
Please read the file "Readme.txt"
"""

## Import sage_interface for SageMathCell server:
from sage_interface import *

## Import numpy and matplotlib.pyplot: (here I suppose the local python environment has only numpy and matplotlib as basic math libraries)
import numpy as np
np.set_printoptions(threshold=np.inf)

import matplotlib.pyplot as plt

import time






### Example #1 with script without inputs for SageMathCell:
print('------------------------------')
print("Example #1 with script without inputs for SageMathCell:")

filename1 = 'input_sage_01.py'

start_time = time.time()
sage_output_01 = execute_sage_script(filename1)
stop_time = time.time()

print("Output by SageMathCell:")
for j in range(len(sage_output_01)):
  print(sage_output_01[j])
  print(type(sage_output_01[j]))

print("Size of output list after execution of script '" + filename1 + "':")
print(len(sage_output_01))
print("Seconds for execution of the script by SageMathCell = %s" % (stop_time-start_time))







### Example #2 with script with inputs for SageMathCell:
print('------------------------------')
print("Example #2 with script with inputs for SageMathCell:")

filename2 = 'input_sage_02.py'

sage_inputs_01 = namestr( n=10000 , maior=100 , minor=-100)

start_time = time.time()
sage_output_02 = execute_sage_script_w_inputs(sage_inputs_01, filename2)
stop_time = time.time()

print("Output by SageMathCell:")
for j in range(len(sage_output_02)):
  print(sage_output_02[j])
  print(type(sage_output_02[j]))

print("Size of output list after execution of script '" + filename2 + "':")
print(len(sage_output_02))
print("Seconds for execution of the script by SageMathCell = %s" % (stop_time-start_time))







### Example #3 with built-in Python core:
print('------------------------------')
print("Example #3 with built-in Python core:")

filename1 = 'input_sage_01.py'

start_time = time.time()
sage_output_03 = execfile(filename1)
stop_time = time.time()

print("Seconds for execution of the script by SageMathCell = %s" % (stop_time-start_time))

