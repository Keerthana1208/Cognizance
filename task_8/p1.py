import numpy as np
x = input("Enter the first number ")
y = input("Enter the second number ")
x = int(x)
y = int(y)
A = ". 0. 0. 0. 0. 0."
z = ""
for i in range(x,y):
    z = z+str(i)+A
print("vector with 5 consecutive zeros interleaved between each value ")
k = z+str(y)
print(k)