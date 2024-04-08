import numpy as np

tab2D = np.zeros((5, 5), dtype=int)
pierwszyWiersz = np.array([2, 3, 4, 5, 6])
tab2D[0] = pierwszyWiersz

for i in range(1, 5):
    tab2D[i] = tab2D[i - 1] ** 2

print(tab2D)
