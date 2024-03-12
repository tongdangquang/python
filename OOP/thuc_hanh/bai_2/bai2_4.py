class quanly():
    def __init__(self, maql = "", hoten = "") -> None:
        self.maql = maql
        self.hoten = hoten

    def nhap(self):
        self.maql = str(input("Nhập mã quản lý: "))
        self.hoten = str(input("Nhập họ tên: "))

    def xuat(self):
        print(f"Mã quản lý: {self.maql}")
        print(f"Họ tên quản lý: {self.hoten}")

class may():
    def __init__(self, mamay = "", kieumay = "", tinhnang = "") -> None:
        self.mamay = mamay
        self.kieumay = kieumay
        self.tinhnang = tinhnang

    def nhap(self):
        self.mamay = str(input("Nhập mã máy: "))
        self.kieumay = str(input("Nhập kiểu máy: "))
        self.tinhnang = str(input("Nhập tính năng: "))

    def xuat(self):
        print(self.mamay.ljust(30) + self.kieumay.ljust(30) + self.tinhnang.ljust(30))
        
class phongmay():
    def __init__(self, maphong = "", tenphong = "", dientich = 0, n = 0) -> None:
        self.maphong = maphong
        self.tenphong = tenphong
        self.dientich = dientich
        self.ql = quanly()
        self.n = n

    def nhap(self):
        self.maphong = str(input("Nhập mã phòng: "))
        self.tenphong = str(input("Tên phòng: "))
        self.dientich = float(input("Nhập diện tích phòng: "))
        self.ql.nhap()
        while True:
            self.n = int(input("Nhập số lượng máy trong phòng: "))
            if self.n > 0:
                break
            else:
                print("Số liệu không hợp lệ. Nhập lại!")
        print()
        self.m = []
        for i in range(self.n):
            ts = may()
            print(f"Nhập thông tin thiết bị thứ {i + 1}:")
            ts.nhap()
            print()
            self.m.append(ts)
        
    def xuat(self):
        print(f"Mã phòng: {self.maphong}")
        print(f"Tên phòng: {self.tenphong}")
        print(f"Diện tích: {self.dientich}m2")
        self.ql.xuat()
        print("\t\tThông tin thiết bị trong phòng")
        print("MÃ MÁY".ljust(30) + "KIỂU MÁY".ljust(30) + "TÍNH NĂNG".ljust(30))
        for ts in self.m:
            ts.xuat()

k = phongmay()
k.nhap()
k.xuat()