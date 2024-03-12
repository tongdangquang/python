class hanghoa():
    # phương thức khởi tạo
    def __init__(self, mahang = "", tenhang = "", dongia = 0, soluong = 0) -> None:
        self.mahang = mahang
        self.tenhang = tenhang
        self.dongia = dongia
        self.soluong = soluong
    
    # phương thức nhập
    def nhap(self):
        self.mahang = str(input("Nhập mã hàng: "))
        self.tenhang = str(input("Nhập tên hàng: "))
        self.dongia = float(input("Nhập đơn giá: "))
        self.soluong = int(input("Nhập số lượng: "))
    
    # phương thức xuất
    def xuat(self):
        print(self.mahang.ljust(25) + self.tenhang.ljust(25) + str(self.dongia).ljust(25) + str(self.soluong).ljust(25) + str(self.dongia * self.soluong).ljust(25))

while True:
    n = int(input("Nhập số lượng mặt hàng (n >= 0): "))
    if n > 0:
        break
    else:
        print("Số không hợp lệ! Nhập lại.")
print()

m = []
for i in range(n):
    print(f"Nhập thông tin mặt hàng {i + 1}: ")
    k = hanghoa()
    k.nhap()
    m.append(k)
    print()

print("Mã hàng".ljust(25) + "Tên hàng".ljust(25) + "Đơn giá".ljust(25) + "Số lượng".ljust(25) + "Thành tiền".ljust(25))
for k in m:
    k.xuat()

    