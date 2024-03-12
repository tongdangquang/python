class student():
    def __init__(self, masv = 0, hoten = "", tuoi = 0, diem = 0) -> None:
        self.masv = masv
        self.hoten = hoten
        self.tuoi = tuoi
        self.diem = diem
    
    def nhap(self):
        self.masv = str(input("Nhập mã sinh viên: "))
        self.hoten = str(input("Nhập họ tên: "))
        self.tuoi = int(input("Nhập tuổi: "))
        self.diem = float(input("Nhập điểm: "))

    def xuat(self):
        print(f"Mã sinh viên: {self.masv}")
        print(f"Họ tên      : {self.hoten}")
        print(f"Tuổi        : {self.tuoi}")
        print(f"Điểm TB     : {self.diem}")

k = student()
k.nhap()
print()
k.xuat()