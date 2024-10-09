class PS:
    def __init__(self, tu = 0, mau = 1):
        self.tu = tu
        self.mau = mau
        
    def ktra_tinh_hop_le(self):
        return self.mau != 0
    
    def nhap_phan_so(self):
        self.tu = int(input("Nhập tử số: "))
        self.mau = int(input("Nhập mẫu số: "))
        
    def in_phan_so(self):
        if self.mau == 1:
            print(f"{self.tu}")
        elif self.mau == -1:
            print(f"{-self.mau}")
        else:
            print(f"{self.tu}/{self.mau}")
            
ps = PS()
ps.nhap_phan_so()
print("Phân số đã nhập là: ", end="")
ps.in_phan_so()
