import numpy as np

arr = np.full((3, 3), True)
print("Array arr (3x3 với giá trị True):\n", arr)

arr_1D = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
arr_2D = arr_1D.reshape((3, 3))
print("\nArray arr_2D ban đầu:\n", arr_2D)

arr_2D[:, [0, 2]] = arr_2D[:, [2, 0]]
print("\nArray arr_2D sau khi hoán đổi cột 1 và cột 3:\n", arr_2D)
arr_2D[[0, 1]] = arr_2D[[1, 0]]
print("\nArray arr_2D sau khi hoán đổi dòng 1 và dòng 2:\n", arr_2D)

arr_2D = arr_2D[::-1]
print("\nArray arr_2D sau khi đảo ngược các dòng:\n", arr_2D)

arr_2D = arr_2D[:, ::-1]
print("\nArray arr_2D sau khi đảo ngược các cột:\n", arr_2D)

arr_2D_null = np.array([[1, 2, 3], [np.NaN, 5, 6], [7, np.NaN, 9], [4, 5, 6]])
print("\nArray arr_2D_null ban đầu:\n", arr_2D_null)
has_null = np.isnan(arr_2D_null).any()
print("\nCó giá trị null trong arr_2D_null không?", has_null)
arr_2D_null = np.nan_to_num(arr_2D_null, nan=0)
print("\nArray arr_2D_null sau khi thay thế null bằng 0:\n", arr_2D_null)