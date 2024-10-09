import math
class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Elip(Diem):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a
        self.b = b

    def dien_tich(self):
        return math.pi * self.a * self.b

class DuongTron(Elip):
    def __init__(self, x, y, r):
        super().__init__(x, y, r, r)

if __name__ == "__main__":
    x = float(input("Nhập tọa độ x của elip: "))
    y = float(input("Nhập tọa độ y của elip: "))
    a = float(input("Nhập bán trục lớn a của elip: "))
    b = float(input("Nhập bán trục nhỏ b của elip: "))

    elip = Elip(x, y, a, b)
    print(f"Diện tích elip: {elip.dien_tich()}")

    r = float(input("Nhập bán kính r của đường tròn: "))
    duong_tron = DuongTron(x, y, r)
    print(f"Diện tích đường tròn: {duong_tron.dien_tich()}")
