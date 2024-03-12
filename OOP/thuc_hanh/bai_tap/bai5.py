# Thực hiện các phương thức với phân số
class Phanso:
    def __init__(self, ts, ms) -> None:
        self.tu = ts
        self.mau = ms
    
    def set_Phanso(self, t, m):
        self.tu = t
        self.mau = m
        
    def get_tuso(self):
        return self.tu
    def get_mauso(self):
        return self.mau
    
    def nhap(self):
        self.tu, self.mau = map(int, input("Nhập tử và mẫu số: ").split())
    
    def __str__(self) -> str:
        return f"{self.tu}/{self.mau}"
    
    def rut_gon(self):
        return self.tu/self.mau
    
    def phan_so_nghich_dao(self):
        temp = self.tu
        self.tu = self.mau
        self.mau = temp
        return self
    
    def __add__(self, other):
        if(isinstance(other, Phanso)):
            return Phanso(self.tu*other.mau + self.mau*other.tu, self.mau*other.mau)
        else:
            raise TypeError("Không khớp kiểu dữ liệu")
        
    def __sub__(self, other):
        if(isinstance(other, Phanso)):
            return Phanso(self.tu*other.mau - self.mau*other.tu, self.mau*other.mau)
        else:
            raise TypeError("Không khớp kiểu dữ liệu")
        
    def __mul__(self, other):
        if(isinstance(other, Phanso)):
            return Phanso(self.tu*other.tu, self.mau*other.mau)
        else:
            raise TypeError("Không khớp kiểu dữ liệu")
        
    def __truediv__(self, other):
        if(isinstance(other, Phanso)):
            return Phanso(self.tu*other.mau, self.mau*other.tu)
        else:
            raise TypeError("Không khớp kiểu dữ liệu")
        

ps1 = Phanso(1, 2)
ps2 = Phanso(1, 2)
print(f"{ps1} + {ps2} = {ps1 + ps2} = {(ps1 + ps2).rut_gon()}")
print()

print(f"{ps1} - {ps2} = {ps1 - ps2} = {(ps1 - ps2).rut_gon()}")
print()
    
print(f"{ps1} * {ps2} = {ps1 * ps2} = {(ps1 * ps2).rut_gon()}")
print()
    
print(f"{ps1} / {ps2} = {ps1 / ps2} = {(ps1 / ps2).rut_gon()}")
print()
    
