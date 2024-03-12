class Sinhvien:
    def nhap(self):
        self.masv = str(input("Nhập mã sinh viên: "))
        self.tensv = str(input("Nhập tên sinh viên: "))
        self.lop = str(input("Nhập lớp: "))
        self.khoa = int(input("Nhập khóa: "))
    def xuat(self):
        print("Mã sinh viên: ".ljust(15) + self.masv.ljust(25) + "Tên sinh viên: " + self.tensv)
        print("Lớp: ".ljust(15) + self.lop.ljust(25) + "Khóa: " + str(self.khoa))

class Hocphan:
    def nhap(self):
        self.ten_mon = str(input("Nhập tên môn: "))
        self.sotrinh = int(input("Nhập số trình: "))
        self.diem = float(input("Nhập điểm: "))
    def get_diem(self):
        return self.sotrinh*self.diem
    def xuat(self):
        print(self.ten_mon.ljust(25) + str(self.sotrinh).ljust(25) + str(self.diem))

class Phieu:
    sv = Sinhvien()
    m = []
    def nhap(self):
        self.sv.nhap()
        while True:
            self.n = int(input("Nhập số học phần: "))
            if self.n > 0:
                break
            else:
                print("Số liệu không hợp lệ. Nhập lại.")
        print()
        for i in range(self.n):
            hp = Hocphan()
            print("Nhập thông tin học phần thứ:", i + 1)
            hp.nhap()
            print()
            self.m.append(hp)
    
    def xuat(self):
        print("\t\t\tPHIẾU BÁO ĐIỂM")
        self.sv.xuat()
        print("Bảng điểm:")
        print("TÊN MÔN".ljust(25) + "SỐ TRÌNH".ljust(25) + "ĐIỂM")
        tong_diem = 0
        tong_so_trinh = 0
        for i in self.m:
            i.xuat()
            tong_diem += i.get_diem()
            tong_so_trinh += i.sotrinh
        print("Điểm trung bình".ljust(49), round(tong_diem/tong_so_trinh, 2))


def chen(ph):
    pass

ph = Phieu()
ph.nhap()
print()
ph.xuat()