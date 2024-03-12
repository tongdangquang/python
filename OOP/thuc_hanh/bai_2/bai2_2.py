class nsx():
    def __init__(self, mansx = "", tennsx = "", dcnsx = "") -> None:
        self.mansx = mansx
        self.tennsx = tennsx
        self.dcnsx = dcnsx
    def nhap(self):
        self.mansx = str(input("Nhập mã NSX: "))
        self.tennsx = str(input("Nhập tên NSX: "))
        self.dcnsx = str(input("Nhập địa chỉ NSX: "))
    def xuat(self):
        print(f"Mã NSX: {self.mansx}")
        print(f"Tên NSX: {self.tennsx}")
        print(f"Địa chỉ: {self.dcnsx}")

class hang():
    def  __init__(self, mahang = "", tenhang = "", x = None) -> None:
        self.mahang = mahang
        self.tenhang = tenhang
        self.x = x
    def nhap(self):
        self.mahang = str(input("Nhập mã hàng: "))
        self.tenhang = str(input("Nhập tên hàng: "))
        self.x = nsx()
        self.x.nhap()
    def xuat(self):
        print(f"Mã hàng: {self.mahang}")
        print(f"Tên hàng: {self.tenhang}")
        self.x.xuat()

k = hang()
k.nhap()
print()
print("Thông tin mặt hàng:")
k.xuat()