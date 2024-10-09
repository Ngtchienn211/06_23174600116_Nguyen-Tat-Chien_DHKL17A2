class TS:
    def __init__(self,hoten = "", diemtoan = 0, diemly = 0, diemhoa = 0):
        self.hoten = hoten
        self.diemtoan = diemtoan
        self.diemly = diemly
        self.diemhoa = diemhoa
    
    def nhap_thong_tin(self):
        self.hoten = int(input("Nhập tên thí sinh: "))
        self.diemtoan = float(input("Nhập điểm Toán: "))
        self.diemly = float(input("Nhập điểm Lý: "))
        self.diemhoa = float(input("Nhập điểm Hóa: "))
    
    def in_thong_tin(self):
        print(f"Họ tên thí sinh: {self.hoten}")
        print(f"Điểm Toán: {self.diemtoan}")
        print(f"Điểm Lý: {self.diemly}")
        print(f"Điểm Hóa: {self.diemhoa}")
        
    def tong_diem(self):
        return self.diemtoan + self.diemly + self.diemhoa
    
def nhap_ds_thi_sinh():
        danh_sach_thi_sinh = []
        so_luong = int(input("Nhập số lượng thí sinh: "))
        
        for i in range(so_luong):
            thi_sinh = TS()
            thi_sinh.nhap_thong_tin()
            danh_sach_thi_sinh.append(thi_sinh)
        return danh_sach_thi_sinh
    
def in_ds_trung_tuyen(danh_sach_thi_sinh, diem_chuan):
        print(f"\nDanh sách thí sinh trúng tuyển với điểm chuẩn {diem_chuan}: ")
        for thi_sinh in danh_sach_thi_sinh:
            if thi_sinh.tong_diem() >= diem_chuan:
                thi_sinh.in_thong_tin()
            if thi_sinh.tong_diem() < diem_chuan:
                print("Không có thí sinh nào trúng tuyển.")
                  
ds = nhap_ds_thi_sinh()
diem_chuan = float(input("Nhập điểm chuẩn: "))
in_ds_trung_tuyen(danh_sach_thi_sinh, diem_chuan)