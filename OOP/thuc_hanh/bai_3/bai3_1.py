class sinhvien():
    def __init__(self, masv = "", hoten = "", diemtoan = 0, diemly = 0, diemhoa = 0) -> None:
        self.masv = masv
        self.hoten = hoten
        self.diemtoan = diemtoan
        self.diemly = diemly
        self.diemhoa = diemhoa

    def nhap(self):
        self.masv = str(input("Nhập mã SV: "))
        self.hoten = str(input("Nhập họ tên SV: "))
        self.diemtoan = float(input("Nhập điểm toán: "))
        self.diemly = float(input("Nhập điểm lý: "))
        self.diemhoa = float(input("Nhập điểm hóa: "))
    
    def tongdiem(self):
        return self.diemtoan + self.diemly + self.diemhoa
    
    def xuat(self):
        print(self.masv.ljust(15) + self.hoten.ljust(30) + str(self.diemtoan).ljust(15) + str(self.diemly).ljust(15) + str(self.diemhoa).ljust(15) + str(self.diemtoan + self.diemly + self.diemhoa))
    
while True:
    n = int(input("Nhập số lượng sinh viên (n >= 0): "))
    if(n > 0):
        break
    else:
        print("Số liệu không hợp lệ. Nhập lại!")
print()
m = []
for i in range(n):
    sv = sinhvien()
    print("Nhập thông tin sinh viên thứ ", i + 1)
    sv.nhap()
    print()
    m.append(sv)

m = sorted(m, key = lambda sv: sv.tongdiem())
print("DANH SÁCH SINH VIÊN SẮP XẾP THEO CHIỀU TĂNG DẦN TỔNG ĐIỂM:")
print("MA SV".ljust(15) + "HO TEN".ljust(30) + "DIEM TOAN".ljust(15) + "DIEM LY".ljust(15) + "DIEM HOA".ljust(15) + "TONG DIEM")
for i in m:
    i.xuat()


    