class Date:
    d = 0
    m = 0
    y = 0
    
class Hang:
    def __init__(self) -> None:
        self.mahang = ""
        self.tenhang = ""
        self.ngaysx = Date()

    def nhap(self):
        self.mahang = str(input("Nhập mã hàng: "))
        self.tenhang = str(input("Nhập tên hàng: "))
        self.ngaysx.d, self.ngaysx.m, self.ngaysx.y = map(int, input("Nhập ngày, tháng, năm sản xuất: ").split())

    def __str__(self) -> str:
        return f"{self.mahang.ljust(25)}{self.tenhang.ljust(25)}{self.ngaysx.d}/{self.ngaysx.m}/{self.ngaysx.y}"
    
while True:
    n = int(input("Nhập số lượng hàng hóa: "))
    if(n > 0):
        break
    else:
        print("Số liệu không hợp lệ. Nhập lại!")

print()
m = []
for i in range(n):
    hh = Hang()
    print("Nhập thông tin hàng hóa thứ", i + 1)
    hh.nhap()
    print()
    m.append(hh)

print("DANH SÁCH HÀNG HÓA: ")   
print("MÃ HÀNG".ljust(25) + "TÊN HÀNG".ljust(25) + "NGÀY SẢN XUẤT")
for i in m:
    print(i)