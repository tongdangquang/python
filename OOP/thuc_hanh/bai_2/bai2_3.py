class hang():
    def  __init__(self, mahang = "", tenhang = "", dongia = 0) -> None:
        self.mahang = mahang
        self.tenhang = tenhang
        self.dongia = dongia
    def nhap(self):
        self.mahang = str(input("Nhập mã hàng: "))
        self.tenhang = str(input("Nhập tên hàng: "))
        self.dongia = int(input("Nhập đơn giá: "))
    def xuat(self):
        print(self.mahang.ljust(30) + self.tenhang.ljust(30) + str(self.dongia).ljust(30))

class phieu():
    def __init__(self, maphieu = "", n = 0,) -> None:
        self.maphieu = maphieu
        self.n = n
        self.x = []
    def nhap(self):
        self.maphieu = str(input("Nhập mã phiếu: "))
        while True:
            self.n = int(input("Nhập số lượng mặt hàng: "))
            if self.n > 0:
                break
            else:
                print("Số không hợp lệ. Nhập lại!")
            print()
        for i in range(self.n):
            print(f"Nhập thông tin mặt hàng thứ {i + 1}")
            ts = hang()
            ts.nhap()
            print()
            self.x.append(ts)
        
    def xuat(self):
        print(f"Mã phiếu: {self.maphieu}")
        print(f"Số lượng mặt hàng: {self.n}\n")
        print("Mã hàng".ljust(30) + "Tên hàng".ljust(30) + "Đơn giá".ljust(30))
        for i in self.x:
            i.xuat()

k = phieu()
k.nhap()
k.xuat()
