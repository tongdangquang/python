class date():
    def __init__(self, day = 0, mon = 0, year = 0) -> None:
        self.day = day
        self.mon = mon
        self.year = year
    def nhap(self):
        self.day, self.mon, self.year = map(int, input("Nhập ngày, tháng, năm: ").split())
    def xuat(self):
        print(f"{self.day}/{self.mon}/{self.year}")


class nhansu():
    def __init__(self, manhansu: str = "", hoten: str = "", ns = None) -> None:
        self.manhansu = manhansu
        self.hoten = hoten
        self.ns = ns
    def nhap(self):
        self.manhansu = str(input("Nhập mã nhân sự: "))
        self.hoten = str(input("Nhập họ tên: "))
        self.ns = date()
        self.ns.nhap()
    def xuat(self):
        print(f"Mã nhân sự: {self.manhansu}")
        print(f"Họ tên: {self.hoten}")
        print("Năm sinh:", end = " ")
        self.ns.xuat()

k = nhansu()
k.nhap()
print()
k.xuat()