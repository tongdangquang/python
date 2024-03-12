"""Học viện V1Study thực hiện trao học bổng cho các học viên xuất sắc và đáp ứng đủ các yêu cầu sau:
a. Là học viên đăng ký khóa học HDSE
b. Có điểm tổng kết >= 75%
c. Không vi phạm nội quy của trung tâm
d. Các kì thi chỉ thi lần đầu tiên
Các dữ liệu a b c d của 1 học viên được nhập từ bàn phím.
Viết chương trình xem học viên đó có được học bổng không."""
class hocvien:
    def __init__(self) -> None:
        self.dang_ky = ""
        self.vi_pham_noi_quy = ""
        self.diem = 0
    def nhap(self):
        self.dang_ky = str(input("Sinh vien đăng ky khoa hoc chua? - (yes/no): "))
        self.vi_pham_noi_quy = str(input("Sinh vien co vi pham noi quy? - (yes/no): "))
        self.diem = float(input("Nhap diem GPA: "))

    def xuat(self):
        print("Sinh vien da dang ky hoc")
        print("Sinh vien khong vi pham noi quy")
        print(f"Sinh vien co diem GPA la {self.diem}")

    def xet_hoc_bong(self):
        if(self.dang_ky.lower() == "yes" and self.vi_pham_noi_quy.lower() == "no" and self.diem >= 8.5):
            return True
        else:
            return False
        
hv = hocvien()
print("Nhap thong tin học vien: ")
hv.nhap()
print('-'*30)
hv.xuat()
print('-'*30)
if(hv.xet_hoc_bong()):
    print("=> Sinh vien duoc nhan học bong")
else:
    print("=> Sinh vien khong duoc nhan hoc bong")