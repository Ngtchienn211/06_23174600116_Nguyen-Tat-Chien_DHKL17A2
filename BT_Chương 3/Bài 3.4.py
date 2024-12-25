import numpy as np
arr_zeros = np.zeros(10)
arr_zeros[4] = 1

print(arr_zeros)

arr_h = np.arange(10, 25)
print(arr_h[::-1])

arr_k = np.array([1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 0])
arr_1 = arr_k[(arr_k != 0)]

print(arr_1)