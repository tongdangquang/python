from math import sqrt
class PTB2:
    def __init__(self, x = 0, y = 0, z = 0) -> None:
        self.a = x
        self.b = y
        self.c = z

    def nhap(self):
        self.a, self.b, self.c = map(int, input("Nhập hệ số a (a != 0), b, c của phương trình: ").split())

    def xuat(self):
        print(f"{self.a}x2 + {self.b}x + {self.c} = 0")

    def giai(self):
        if self.a == 0:
            print("Hệ số a = 0")
            return
        else:
            delta = self.b*self.b - 4*self.a*self.c
            if delta > 0:
                x1 = (-self.b + sqrt(delta))/(2*self.a)
                x2 = (-self.b - sqrt(delta))/(2*self.a)
                print(f"Tập nghiệm của phương trình: S = ({x1}, {x2})")
            elif delta == 0:
                x = (-self.b)/(2*self.a)
                print(f"Tập nghiệm của phương trình: S = ({x})")
            else:
                print("Phương trình vô nghiệm")

pt = PTB2()
pt.nhap()
print()
pt.xuat()
print()
pt.giai()