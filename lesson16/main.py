import numpy as np

from numpy import random

arr = np.array([1, 2, 3, 4, 5])
# arr = np.array((1, 2, 3, 4, 5))

print(arr)
print(type(arr))

# 0-D array
arr_2 = np.array(42)
print(arr_2)

# 1-D array
arr_3 = np.array([1, 2, 3, 4, 5, 6])
print(arr_3)

# 2-D array
arr_4 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr_4)

# Indexation
print(arr_3[0])
print(arr_3[2] + arr_3[3])
print('2nd element on 1st row:', arr_4[0, 1])
print('Last element from 2nd dim:', arr_4[1, -1])

print(arr_3[1:5])
print(arr_3[-3:-1])
print(arr_3[1:5:2])

arr_5 = np.array([1, 2, 3])
arr_6 = np.array([4, 5, 6])
arr_7 = np.concatenate((arr_5, arr_6))
print(arr_7)

new_arr = np.array_split(arr_3, 3)
print(new_arr)
print(new_arr[0])
print(new_arr[1])
print(new_arr[2])

arr_8 = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr_8 == 4)
print(x)

# Generate random number
y = random.randint(100)
print(y)

z = random.rand()
print(z)

# Generate random array
y2 = random.randint(100, size=5)
print(y2)

z2 = random.rand(5)
print(z2)

x2 = random.choice([3, 5, 7, 9])
print(x2)

x3 = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=100)
print(x3)
