class NSX:
    Mansx = ""
    Tennsx = ""
    Dcnsx = ""
    
class Hang:
    Mahang = ""
    Tenhang = ""
    Dongia = 0
    Trongluong = 0
    nsx = NSX()

    def nhap(self):
        self.Mahang = str(input("Nhập mã hàng: "))
        self.Tenhang = str(input("Nhập tên hàng: "))
        self.Dongia = float(input("Nhập đơn giá: "))
        self.Trongluong = float(input("Nhập trọng lượng: "))
        self.nsx = NSX() # khai báo lại 1 lần để tránh bị trùng lặp dữ liệu
        self.nsx.Mansx = str(input("Nhập mã NSX: "))
        self.nsx.Tennsx = str(input("Nhập tên NSX: "))
        self.nsx.Dcnsx = str(input("Nhập địa chỉ NSX: "))
    
    def xuat(self):
        print(self.Mahang.ljust(20) + self.Tenhang.ljust(20) + str(self.Dongia).ljust(20) + str(self.Trongluong).ljust(20) + self.nsx.Mansx.ljust(20) + self.nsx.Tennsx.ljust(20) + self.nsx.Dcnsx)


while True:
    n = int(input("Nhập số lượng mặt hàng: "))
    if n > 0:
        break
    else:
        print("Số liệu không hợp lệ.")
m = []
for i in range(n):
    hh = Hang()
    print("Nhập thông tin hàng hóa thứ", i + 1)
    hh.nhap()
    print()
    m.append(hh)

print("DANH SÁCH HÀNG HÓA: ")
print("MÃ HÀNG HÓA".ljust(20) + "TÊN HÀNG HÓA".ljust(20) + "ĐƠN GIÁ".ljust(20) + "TRỌNG LƯỢNG".ljust(20) + "MÃ NSX".ljust(20) + "TÊN NSX".ljust(20) + "ĐỊA CHỈ NSX")
for i in m:
    i.xuat()
