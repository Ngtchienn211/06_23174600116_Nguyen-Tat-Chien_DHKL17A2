import numpy as np

arr = np.arange(10)

print("Mảng arr:", arr)
print("Kiểu dữ liệu:", arr.dtype)
print("Kích thước:", arr.shape)


arr_odd = arr[arr % 2 == 1]
arr_even = arr[arr % 2 == 0]

print("Mảng các số lẻ:", arr_odd)
print("Mảng các số chẵn:", arr_even)


arr_update_1 = arr.copy()
arr_update_1[arr_update_1 % 2 == 1] = 100

print("Mảng sau khi cập nhật:", arr_update_1)