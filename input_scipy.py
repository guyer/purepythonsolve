#~ import time
#~ time.sleep(1)

import numpy as np
import scipy.sparse as sp
from scipy.sparse import linalg
np.set_printoptions(threshold=np.inf)

n = 10000
maior = 100
minor = -100

a = sp.lil_matrix((n, n))

i = np.arange(n)
j = np.arange(n)
a.setdiag((maior-minor)*np.random.rand(n)+minor, k=0)
a.setdiag((maior-minor)*np.random.rand(n)+minor, k=1)
a.setdiag((maior-minor)*np.random.rand(n)+minor, k=-1)

a = a.tocsr()

b = (maior-minor)*np.random.rand(n)+minor

x = linalg.spsolve(a, b)

# print(x)

