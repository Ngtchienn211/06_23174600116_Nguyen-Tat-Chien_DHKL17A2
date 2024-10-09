class DaGiac:
    def __init__(self, so_canh):
        self.so_canh = so_canh

class HinhBinhHanh(DaGiac):
    def __init__(self, canh_dai, canh_ngan):
        super().__init__(4)
        self.canh_dai = canh_dai
        self.canh_ngan = canh_ngan

    def tinh_chu_vi(self):
        return 2 * (self.canh_dai + self.canh_ngan)

    def tinh_dien_tich(self):
        return self.canh_dai * self.canh_ngan

class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(chieu_dai, chieu_rong)

class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)

if __name__ == "__main__":
    canh_binh_hanh_dai = float(input("Nhập chiều dài hình bình hành: "))
    canh_binh_hanh_ngan = float(input("Nhập chiều ngắn hình bình hành: "))
    
    hinh_binh_hanh = HinhBinhHanh(canh_binh_hanh_dai, canh_binh_hanh_ngan)
    print("Chu vi hình bình hành:", hinh_binh_hanh.tinh_chu_vi())
    print("Diện tích hình bình hành:", hinh_binh_hanh.tinh_dien_tich())

    chieu_dai = float(input("Nhập chiều dài hình chữ nhật: "))
    chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))
    
    hinh_chu_nhat = HinhChuNhat(chieu_dai, chieu_rong)
    print("Chu vi hình chữ nhật:", hinh_chu_nhat.tinh_chu_vi())
    print("Diện tích hình chữ nhật:", hinh_chu_nhat.tinh_dien_tich())

    canh_vuong = float(input("Nhập cạnh hình vuông: "))
    
    hinh_vuong = HinhVuong(canh_vuong)
    print("Chu vi hình vuông:", hinh_vuong.tinh_chu_vi())
    print("Diện tích hình vuông:", hinh_vuong.tinh_dien_tich())
