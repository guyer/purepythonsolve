#~ import time
#~ time.sleep(1)

import numpy as np
np.set_printoptions(threshold=np.inf)

a = (maior-minor)*np.random.rand(n, n)+minor
b = (maior-minor)*np.random.rand(n)+minor

x = np.linalg.solve(a, b)

print(x)

