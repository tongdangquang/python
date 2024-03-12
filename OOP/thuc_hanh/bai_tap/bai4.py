"""Xây dựng lớp tam giác có các thành phần:
Các thuộc tính: a, b, c
Các phương thức:
    Nhập độ dài 3 cạnh
    Tính chu vi và diện tích"""
from math import sqrt
class Triangle:
    def __init__(self) -> None:
        self.a = 0
        self.b = 0
        self.c = 0
    
    def nhap(self):
        self.a, self.b, self.c = map(int, input("Nhap lần lượt a, b, c: ").split())
    
    def chu_vi(self):
        return self.a + self.b + self.c
    
    def dien_tich(self):
        p = self.chu_vi()/2
        return sqrt(p*(p - self.a)*(p - self.b)*(p - self.c))
    
tg = Triangle()
tg.nhap()
print("-"*30)
print(f"Chu vi cua tam giac: {tg.chu_vi()}")
print("-"*30)
print(f"Dien tich cua tam giac: {tg.dien_tich()}")

