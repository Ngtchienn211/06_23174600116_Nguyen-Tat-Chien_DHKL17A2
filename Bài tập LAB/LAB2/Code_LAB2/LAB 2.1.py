import numpy as np

np.random.seed(2222)
nhiet_do = np.round(np.random.uniform(15, 35, size=30), 2)
nhiet_do_tb = np.mean(nhiet_do)

print("Dữ liệu nhiệt độ hàng ngày:", nhiet_do)
print("Nhiệt độ trung bình trong tháng:", round(nhiet_do_tb, 2))

nhiet_do_cao_nhat = np.max(nhiet_do)
nhiet_do_thap_nhat = np.min(nhiet_do)
ngay_cao_nhat = np.argmax(nhiet_do) + 1
ngay_thap_nhat = np.argmin(nhiet_do) + 1

chenh_lech_nhiet_do = np.abs(np.abs(nhiet_do[1:] - nhiet_do[:-1]))
ngay_chenh_lech_lon_nhat = np.argmax(chenh_lech_nhiet_do) + 1

print("Ngày có nhiệt độ cao nhất:", ngay_cao_nhat, "với nhiệt độ:", nhiet_do_cao_nhat)
print("Ngày có nhiệt độ thấp nhất:", ngay_thap_nhat, "với nhiệt độ:", nhiet_do_thap_nhat)
print("Chênh lệch nhiệt độ giữa các ngày:", chenh_lech_nhiet_do)
print("Ngày có sự biến đổi nhiệt độ lớn nhất:", ngay_chenh_lech_lon_nhat, "với chênh lệch:", chenh_lech_nhiet_do[ngay_chenh_lech_lon_nhat - 1])

ngay_tren_20_do = np.where(nhiet_do > 20)[0] + 1
nhiet_do_tren_20 = nhiet_do[nhiet_do > 20]

ngay_cu_the = [5, 10, 15, 20, 25]
nhiet_do_ngay_cu_the = nhiet_do[np.array(ngay_cu_the) - 1]

ngay_tren_tb = np.where(nhiet_do > nhiet_do_tb)[0] + 1
nhiet_do_tren_tb = nhiet_do[nhiet_do > nhiet_do_tb]

nhiet_do_ngay_chan = nhiet_do[1::2]
nhiet_do_ngay_le = nhiet_do[0::2]

print("Các ngày có nhiệt độ cao hơn 20°C:", ngay_tren_20_do)
print("Nhiệt độ của các ngày trên 20°C:", nhiet_do_tren_20)

print("Nhiệt độ của ngày 5, 10, 15, 20, và 25:", nhiet_do_ngay_cu_the)

print("Các ngày có nhiệt độ trên trung bình:", ngay_tren_tb)
print("Nhiệt độ của các ngày trên trung bình:", nhiet_do_tren_tb)

print("Nhiệt độ của các ngày chẵn:", nhiet_do_ngay_chan)
print("Nhiệt độ của các ngày lẻ:", nhiet_do_ngay_le)
