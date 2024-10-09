class Ngay:
    def __init__(self, ngay: int, thang: int, nam: int):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def __str__(self):
        return f"{self.ngay:02d}/{self.thang:02d}/{self.nam}"
    
    
class Employee:
    def __init__(self, ho_ten: str, ngay_sinh: Ngay, ngay_lam: Ngay):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.ngay_lam = ngay_lam

    def __str__(self):
        return f"Tên: {self.ho_ten}, Ngày sinh: {self.ngay_sinh}, Ngày vào công ty: {self.ngay_lam}"

class QuanLyEmployee:
    def __init__(self):
        self.employee = []

    def them_employee(self, employee: Employee):
        self.employee.append(employee)

    def hien_thi_employee(self):
        for emp in self.employee:
            print(emp)

if __name__ == "__main__":
    ngay_sinh1 = Ngay(22, 2, 2005)
    ngay_lam1 = Ngay(15, 10, 2006)

    ngay_sinh2 = Ngay(10, 6, 2022)
    ngay_lam2 = Ngay(13, 6, 2022)

    employee1 = Employee("Nguyễn Tất Chiến", ngay_sinh1, ngay_lam1)
    employee2 = Employee("Đặng Mai Dương", ngay_sinh2, ngay_lam2)

    quan_ly = QuanLyEmployee()
    quan_ly.them_employee(employee1)
    quan_ly.them_employee(employee2)
    quan_ly.hien_thi_employee()