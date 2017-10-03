

Hi Jonathan, the main script to execute is 'sage_test.py'.

You must install the pure-python library 'websocket-client' with the common 'pip install websocket-client' in order to use the script 'sage_interface.py' that uses the remote server as python environment.

Try to execute 'sage_test.py'. Try to see hoe the script calls the remote server provided by SageMathCell.

With my computer, example #1 and #2 (both use the remote server) work but example #3 gives Out of Memory error. Maybe your computer is faster/with more ram and example #3 works with your computer.

The 3 examples perform the same calculation but the first and second examples use the remote server, the third uses the local python core (resources of user computer).


My purpose is to adapt FiPy in order to use it using the solvers provided by the remote server.

Thank you for FiPy
Matteo