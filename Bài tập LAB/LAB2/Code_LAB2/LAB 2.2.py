import numpy as np
import pandas as pd

df = pd.read_csv('diem_hoc_phan.csv')
diem = df[['HP1', 'HP2', 'HP3']].to_numpy()

def quy_doi_diem(diem):
    if diem >= 8.5:
        return 'A'
    elif diem >= 8.0:
        return 'B+'
    elif diem >= 7.0:
        return 'B'
    elif diem >= 6.5:
        return 'C+'
    elif diem >= 5.5:
        return 'C'
    elif diem >= 5.0:
        return 'D+'
    elif diem >= 4.0:
        return 'D'
    else:
        return 'F'

diem_tin_chi = np.vectorize(quy_doi_diem)(diem)

diem_hp1 = diem[:, 0]
diem_hp2 = diem[:, 1]
diem_hp3 = diem[:, 2]

def phan_tich_hoc_phan(diem_hp):
    tong = np.sum(diem_hp)
    trung_binh = np.mean(diem_hp)
    do_lech_chuan = np.std(diem_hp)
    return tong, trung_binh, do_lech_chuan

tong_hp1, trung_binh_hp1, do_lech_chuan_hp1 = phan_tich_hoc_phan(diem_hp1)
tong_hp2, trung_binh_hp2, do_lech_chuan_hp2 = phan_tich_hoc_phan(diem_hp2)
tong_hp3, trung_binh_hp3, do_lech_chuan_hp3 = phan_tich_hoc_phan(diem_hp3)

print("Học phần 1: Tổng = {}, Trung bình = {}, Độ lệch chuẩn = {}".format(tong_hp1, trung_binh_hp1, do_lech_chuan_hp1))
print("Học phần 2: Tổng = {}, Trung bình = {}, Độ lệch chuẩn = {}".format(tong_hp2, trung_binh_hp2, do_lech_chuan_hp2))
print("Học phần 3: Tổng = {}, Trung bình = {}, Độ lệch chuẩn = {}".format(tong_hp3, trung_binh_hp3, do_lech_chuan_hp3))

def dem_loai_diem(diem_tin_chi):
    loai_diem, so_luong = np.unique(diem_tin_chi, return_counts=True)
    return dict(zip(loai_diem, so_luong))

so_luong_diem_hp1 = dem_loai_diem(diem_tin_chi[:, 0])
so_luong_diem_hp2 = dem_loai_diem(diem_tin_chi[:, 1])
so_luong_diem_hp3 = dem_loai_diem(diem_tin_chi[:, 2])

print("Số lượng sinh viên đạt từng loại điểm chữ học phần 1:", so_luong_diem_hp1)
print("Số lượng sinh viên đạt từng loại điểm chữ học phần 2:", so_luong_diem_hp2)
print("Số lượng sinh viên đạt từng loại điểm chữ học phần 3:", so_luong_diem_hp3)
