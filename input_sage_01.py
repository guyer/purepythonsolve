#~ import time
#~ time.sleep(1)

import numpy as np
np.set_printoptions(threshold=np.inf)

n = 10000
maior = 100
minor = -100

a = np.zeros((n, n))
i = np.arange(n)
j = np.arange(n)
a.put(i*n + j, (maior-minor)*np.random.rand(n)+minor)
a.put(i[1:]*n + j[:-1], (maior-minor)*np.random.rand(n)+minor)
a.put(i[:-1]*n + j[1:], (maior-minor)*np.random.rand(n)+minor)

b = (maior-minor)*np.random.rand(n)+minor

x = np.linalg.solve(a, b)

print(x)

