"""Tạo class có tên SoHoc gồm có các thuộc tính và phương thức sau:
+ Thuộc tính: number1, number2
+ Phương thức:
- Phương thức tạo __init()__
- Các phương thức get, set cho tất cả các thuộc tính
- inputinfo(): dùng để nhập 2 số number1, number2
- printinfo(): dùng để hiển thị number1, number2
- addition(): dùng để cộng number1, number2
- subtract(): trừ number1, number2
- multi(): dùng để nhân number1, number2
- division(): dùng để chia number1, number2."""

class SoHoc:
    def __init__(self) -> None:
        self.number1 = 0
        self.number2 = 0

    def get_number1(self):
        return self.number1
    def get_number2(self):
        return self.number2
    
    def set_number1(self, n1):
        self.number1 = n1
    def set_number2(self, n2):
        self.number2 = n2
    
    def nhap(self):
        self.number1 = int(input("Nhập number1: "))
        self.number2 = int(input("Nhập number2: "))
    
    def xuat(self):
        print("Number1:", self.number1)
        print("Number2:", self.number2)
    
    def cong(self):
        return self.number1 + self.number2

    def tru(self):
        return self.number1 - self.number2
    
    def nhan(self):
        return self.number1 * self.number2
    
    def chia(self):
        if(self.number2 == 0):
            print("Không thể chia")
        else:
            return self.number1 / self.number2
    
num = SoHoc()
print("Nhập số: ")
num.nhap()
print()
num.xuat()
print("Tổng =", num.cong())
print("Hiệu =", num.tru())
print("Tích =", num.nhan())
print("Thương =", num.chia())

    