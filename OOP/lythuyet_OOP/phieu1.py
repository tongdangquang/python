class kiemke:
    def __init__(self, nhanvien = "", chucvu = "", phong = "", maphong = "", truongphong = "") -> None:
        self.nhanvien = nhanvien
        self.chucvu = chucvu
        self.phong = phong
        self.maphong = maphong
        self.truongphong = truongphong
    
    def nhap(self):
        self.nhanvien = str(input("Nhập nhân viên kiểm kê: "))
        self.chucvu = str(input("Chức vụ: "))
        self.phong = str(input("Phòng kiểm kê: "))
        self.maphong = str(input("Nhập mã phòng: "))
        self.truongphong = str(input("Nhập tên trưởng phòng: "))
    
    def xuat(self):
        print(f"Nhân viên kiểm kê: {self.nhanvien}".ljust(40) + f"Chức vụ: {self.chucvu}".ljust(40))
        print(f"Kiểm kê tại phòng: {self.phong}".ljust(40) + f"Mã phòng: {self.maphong}".ljust(40))
        print(f"Trưởng phòng: {self.truongphong}".ljust(40))
        
    
class taisan:
    def __init__(self, name = "", soluong = 0, tinhtrang = "") -> None:
        self.name = name
        self.soluong = soluong
        self.tinhtrang = tinhtrang

    def nhap(self):
        self.name = str(input("Nhập tên tài sản: "))
        self.soluong = int(input("Nhập số lượng: "))
        self.tinhtrang = str(input("Nhập tình trạng: "))
    
    def xuat(self):
        print(str(self.name).ljust(30) + str(self.soluong).ljust(30) + str(self.tinhtrang).ljust(30))


class phieu:
    def __init__(self, maphieu = "", date = "", hang = 0) -> None:
        self.maphieu = maphieu
        self.date = date
        self.hang = hang
        self.x = kiemke()
        self.m = []

    def nhap(self):
        self.maphieu = str(input("Nhập mã phiếu: "))
        self.date = str(input("Nhập ngày kiểm kê: "))
        self.x.nhap()
        self.hang = int(input("Nhập số lượng hàng hóa: "))
        for i in range(self.hang):
            ts = taisan()
            ts.nhap()
            self.m.append(ts)
            print()

    def xuat(self):
        print("\t\t\tPHIẾU KIỂM KÊ TÀI SẢN")
        print(f"Mã phiếu: {self.maphieu}".ljust(40) + f"Ngày kiểm kê: {self.date}".ljust(40))
        self.x.xuat()
        tong = 0
        print("Tên tài sản".ljust(30) + "Số lượng".ljust(30) + "Tình trạng".ljust(30))
        for ts in self.m:
            ts.xuat()
            tong += ts.soluong
        print(f"Số tài sản đã kiểm kê: {self.hang}".ljust(40) + f"Tổng số lượng: {tong}".ljust(40))
        
p = phieu()
p.nhap()
p.xuat()
