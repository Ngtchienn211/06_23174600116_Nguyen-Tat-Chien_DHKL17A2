import numpy as np

efficiency = []
shifts = []

with open('efficiency.txt', 'r') as file_eff:
    for line in file_eff:
        efficiency.append(float(line.strip()))

with open('shifts.txt', 'r') as file_shifts:
    for line in file_shifts:
        shifts.append(line.strip())

np_shifts = np.array(shifts)
print(np_shifts)
print(type(np_shifts))

np_efficiency = np.array(efficiency)
print(np_efficiency)
print(type(np_efficiency))

morning_efficiency = np_efficiency[np_shifts == 'Morning']
average_morning_efficiency = np.mean(morning_efficiency)
print("Hiệu suất sản xuất trung bình ca Morning:", average_morning_efficiency)

non_morning_efficiency = np_efficiency[np_shifts != 'Morning']
average_non_morning_efficiency = np.mean(non_morning_efficiency)
print("Hiệu suất sản xuất trung bình các ca khác:", average_non_morning_efficiency)

workers_dtype = np.dtype([('shift', 'U10'), ('efficiency', 'f4')])
workers = np.array(list(zip(np_shifts, np_efficiency)), dtype=workers_dtype)
print(workers)

sorted_workers = np.sort(workers, order='efficiency')

highest_efficiency_shift = sorted_workers[-1]['shift']
lowest_efficiency_shift = sorted_workers[0]['shift']

print("Ca làm việc có hiệu suất cao nhất:", highest_efficiency_shift)
print("Ca làm việc có hiệu suất thấp nhất:", lowest_efficiency_shift)
