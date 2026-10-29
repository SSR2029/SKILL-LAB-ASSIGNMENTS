
import numpy as np


# 1. Array Creation and Manipulation

arr = np.random.randint(1, 21, (5, 5))
arr[:, 2] = 1

print("1.")
print(arr)


# 2. Replace Diagonal Elements with 0

arr = np.arange(1, 17).reshape(4, 4)
np.fill_diagonal(arr, 0)

print("2.")
print(arr)


# 3. Extract Border Elements

arr = np.random.randint(1, 21, (5, 5))

border = np.concatenate([
    arr[0, :],
    arr[-1, :],
    arr[1:-1, 0],
    arr[1:-1, -1]
])

print("3.")
print(arr)
print("Border elements:")
print(border)


# 4. Row-wise and Column-wise Sum

arr = np.arange(1, 17).reshape(4, 4)

print("4.")
print("Row sum:", arr.sum(axis=1))
print("Column sum:", arr.sum(axis=0))


# 5. Reshape Array

arr = np.arange(1, 10).reshape(3, 3)

print("5.")
print("Shape (1, 9):")
print(arr.reshape(1, 9))
print("Shape (9, 1):")
print(arr.reshape(9, 1))


# 6. Structured Array and Sorting by Age

data = np.array([
    ('Tom', 25, 60.5),
    ('Andy', 20, 55.2),
    ('Lucas', 30, 70.8)
], dtype=[
    ('name', 'U10'),
    ('age', 'i4'),
    ('weight', 'f4')
])

data = np.sort(data, order='age')

print("6.")
print(data)
