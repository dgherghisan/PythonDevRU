from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# part 1
sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()

# part 2
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()

# part 3
sns.distplot(random.normal(size=1000), hist=False)
plt.show()

# part 4
sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
plt.show()

# part 5
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
plt.show()

# part 6
sns.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()

# part 7
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
    z.append(i + j)
print(z)

# part 8
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)
print(z)

# part 9
arr_1 = np.array([10, 11, 12, 13, 14, 15])
arr_2 = np.array([20, 21, 22, 23, 24, 25])

new_arr = np.add(arr_1, arr_2)
print(new_arr)

# part 10
arr_1 = np.array([10, 11, 12, 13, 14, 15])
arr_2 = np.array([20, 21, 22, 23, 24, 25])

new_arr = np.subtract(arr_1, arr_2)
print(new_arr)

# part 11
arr = np.around(3.1666, 2)
print(arr)

# part 12
arr = np.floor([-3.1666, 3.6667])
print(arr)

# part 13
arr = np.ceil([-3.1666, 3.6667])
print(arr)
