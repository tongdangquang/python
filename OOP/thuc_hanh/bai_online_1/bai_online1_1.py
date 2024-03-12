class Date:
    def __init__(self) -> None:
        self.d = self.m = self.y = 0
    def nhap(self):
        self.d, self.m, self.y = map(int,input("Nhập lần lượt ngày, tháng, năm: ").split())
    def xuat(self) -> str:
        print(f"{self.d}/{self.m}/{self.y}")
    
class Nha_cung_cap:
    def nhap(self):
        self.mancc = str(input("Nhập mã nhà cung cấp: "))
        self.tenncc = str(input("Nhập tên nhà cung cấp: "))
        self.diachi = str(input("Nhập địa chỉ nhà cung cấp: "))
    
class Hang:
    def nhap(self):
        self.tenhang = str(input("Nhập tên hàng hóa: "))
        self.dongia = float(input("Nhập đơn giá: "))
        self.soluong = int(input("Nhập số lượng: "))
    def getThanhtien(self):
        return self.dongia*self.soluong
    
    def __str__(self):
        return self.tenhang.ljust(25) + str(self.dongia).ljust(25) + str(self.soluong).ljust(25) + str(round(self.getThanhtien(), 1))
    
class Phieu:
    ngaylap = Date()
    ncc = Nha_cung_cap()
    n = None
    m = []
    def nhap(self):
        self.maphieu = str(input("Nhập mã phiếu: "))
        self.ngaylap.nhap()
        self.ncc.nhap()
        while True:
            self.n = int(input("Nhập số lượng mặt hàng: "))
            if(self.n > 0):
                break
            else:
                print("Số liệu không hợp lệ. Nhập lại!")
        print()
        for i in range(self.n):
            print("Nhập thông tin mặt hàng thứ", i + 1)
            hh = Hang()
            hh.nhap()
            print()
            self.m.append(hh)

    def xuat(self):
        print("PHIẾU NHẬP HÀNG".rjust(35))
        print("Mã phiếu:".ljust(10) + self.maphieu.ljust(30) + "Ngày lập:", end=" ")
        self.ngaylap.xuat()
        print("Mã NCC: ".ljust(10) + self.ncc.mancc.ljust(30) + "Tên NCC: " + str(self.ncc.tenncc))
        print("Địa chỉ: ".ljust(10) + self.ncc.diachi)
        print("TÊN HÀNG".ljust(25) + "ĐƠN GIÁ".ljust(25) + "SỐ LƯỢNG".ljust(25) + "THÀNH TIỀN")
        tong = 0
        for i in self.m:
            print(i)
            tong += i.getThanhtien()
        print("\t\t\tCộng thành tiền".ljust(75-12-9) + str(tong))
        
p = Phieu()
p.nhap()
print('-'*35)
p.xuat()