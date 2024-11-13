import numpy as np
arr_a = [1,2,3,2,3,4,3,4,5,6]
arr_b = [7,2,10,2,7,4,9,4,9,8]

arr_c = np.intersect1d(arr_a, arr_b)
print("Các phần tử xuất hiện ở cả dãy a và b:", arr_c)

arr_d = np.setdiff1d(arr_a, arr_b)
print("Các phần tử chỉ xuất hiện ở dãy b:", arr_d)

arr_e = np.array([2, 6, 1, 9, 10, 3, 27, 8, 6, 25, 16])
print("Dãy e:", arr_e)

arr_f = arr_e[(arr_e >= 5) & (arr_e <= 10)]
print("Các phần tử dãy e trong khoảng từ 5 - 10 là:", arr_f)