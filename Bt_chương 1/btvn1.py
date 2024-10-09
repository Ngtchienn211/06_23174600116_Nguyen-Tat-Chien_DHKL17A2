class hcn:
    def __init__(self, chieudai = 0, chieurong = 0):
        self.chieudai = chieudai
        self.chieurong = chieurong
    
    def nhap_du_lieu(self):
        self.chieudai = float(input("Mời nhập chiều dài hình chữ nhật: "))
        self.chieurong = float(input("Mời nhập chiều rộng hình chứ nhật: "))
    
    def chu_vi(self):
        return (self.chieudai + self.chieurong) * 2
    
    def dien_tich(self):
        return self.chieudai * self.chieurong 
    
    def thong_tin(self):
        print(f"Chiều dài hình chữ nhật: {self.chieudai}")
        print(f"Chiều rộng hình chữ nhật: {self.chieurong}")
        print(f"Chu vi hình chữ nhật: {self.chu_vi()}")
        print(f"Diện tích hình chữ nhật: {self.dien_tich()}")
    
hcn = hcn()
hcn.nhap_du_lieu()
hcn.thong_tin()
