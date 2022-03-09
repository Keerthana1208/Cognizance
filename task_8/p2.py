import numpy as np

x = np.random.randint(0, 4, 5)
print("First array:")
print(x)
y = np.random.randint(0, 3, 5)
print("Second array:")
print(y)
print("above two arrays are equal : ")
Z = np.allclose(x, y)
print(Z)
