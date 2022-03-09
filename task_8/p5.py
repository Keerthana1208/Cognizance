import numpy as np
#Multiplying a matrix
m1 = np.array([[1,4,7],[2,5,8]])
print("matrix 1 : ")
print(m1)
m2 = np.array([[1,4],[2,5],[3,6]])
print("matrix 2 : ")
print(m2)
m3 = np.dot(m1,m2)
print(" The multiplication of m1 and m2 is : ")
print(m3)

#identity matrix

dimension = int(input("Enter the dimension of identity matrix: "))
s = np.identity(dimension, dtype="int")
print ("the identity matrix is ")
print(s)



