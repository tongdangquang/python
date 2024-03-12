'''Viết class NhanVien gồm các thuộc tính:
+ Tên
+ Tuổi
+ Địa chỉ
+ Tiền lương
+ Tổng số giờ làm
Và các phương thức:
- Phương thức tạo
- inputinfo() : Nhập các thông tin cho nhân viên từ bàn phím
- printlnfo() : In ra tất cả các thông tin của nhân viên
- tinhThuong(): Tính toán và trả về số tiền thưởng của nhân viên theo công thức sau:
Nếu tổng số giờ làm của nhân viên >= 200 thì thưởng = lương * 20%
Nếu tổng số giờ làm của nhân viên < 200 và >= 100 thì thưởng = lương * 10%
Nếu tổng số giờ làm của nhân viên < 100 thì thưởng = 0'''
class Nhanvien:
    def __init__(self) -> None:
        self.ten = ""
        self.tuoi = 0
        self.diachi = ""
        self.tienluong = 0
        self.tong_gio_lam = 0
    
    def inputinfo(self):
        self.ten = str(input("Nhap ten nhan vien: "))
        self.tuoi = int(input("Nhap tuoi nhan vien: "))
        self.diachi = str(input("Nhap dia chi: "))
        self.tienluong = float(input("Nhap tien luong: "))
        self.tong_gio_lam = float(input("Nhap tong gio lam: "))
    
    def printinfo(self):
        print("Ho ten nhan vien:", self.ten)
        print("Tuoi:", self.tuoi)
        print("Dia chi:", self.diachi)
        print("Tien luong:", self.tienluong)
        print("TOng gio lam:", self.tong_gio_lam)

    def thuong(self):
        if(self.tong_gio_lam >= 200):
            return self.tienluong * 0.2
        elif(self.tong_gio_lam < 200 and self.tong_gio_lam >= 100):
            return self.tienluong * 0.1
        else:
            return 0
        
nv = Nhanvien()
print("Nhap thong tin cua nhan vien: ")
nv.inputinfo()
print()
print("Thong tin nhan vien: ")
nv.printinfo()
print()
print("Tien thuong nhan vien nhan duoc:", nv.thuong())