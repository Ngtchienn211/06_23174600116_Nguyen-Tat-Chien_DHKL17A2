import math
class TamGiac:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def dien_tich(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

class TamGiacCan(TamGiac):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        if a != b and b != c:
            raise ValueError("Tam giác cân phải có hai cạnh bằng nhau.")

class TamGiacVuong(TamGiac):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        if not self.is_vuong():
            raise ValueError("Không phải tam giác vuông.")

    def is_vuong(self):
        return any([self.a**2 + self.b**2 == self.c**2, 
                    self.a**2 + self.c**2 == self.b**2, 
                    self.b**2 + self.c**2 == self.a**2])

class TamGiacDeu(TamGiacCan):
    def __init__(self, a):
        super().__init__(a, a, a)

if __name__ == "__main__":
    a, b, c = float(input("Nhập cạnh a: ")), float(input("Nhập cạnh b: ")), float(input("Nhập cạnh c: "))
    
    try:
        tg = TamGiac(a, b, c)
        print(f"Diện tích tam giác: {tg.dien_tich()}")
    except ValueError as e:
        print(e)

    try:
        tg_can = TamGiacCan(a, b, c)
        print(f"Cạnh bằng của tam giác cân: {tg_can.canh_bang}")
    except ValueError as e:
        print(e)

    try:
        tg_vuong = TamGiacVuong(a, b, c)
        print("Đây là tam giác vuông.")
    except ValueError as e:
        print(e)

    try:
        tg_deu = TamGiacDeu(a)
        print("Đây là tam giác đều.")
    except ValueError as e:
        print(e)
