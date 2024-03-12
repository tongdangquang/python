class sach():
    # phương thức khởi tạo
    def __init__(self, masach = "", tensach = "", nxb = "", sotrang = 0, giatien = 0) -> None:
        self.masach = masach
        self.tensach = tensach
        self.nxb = nxb
        self.sotrang = sotrang
        self.giatien = giatien

    # phương thức nhập
    def nhap(self):
        self.masach = str(input("Nhập mã sách: "))
        self.tensach = str(input("Nhập tên sách: "))
        self.nxb = str(input("Nhập nhà xuất bản: "))
        self.sotrang = int(input("Nhập số trang: "))
        self.giatien = float(input("Nhập giá tiền: "))
        
    # phương thức xuất
    def xuat(self):
        print(self.masach.ljust(25) + self.tensach.ljust(25) + self.nxb.ljust(25) + str(self.sotrang).ljust(25) + str(self.giatien).ljust(25))
    
while True:
    n = int(input("Nhập số lượng cuốn sách (n >= 0): "))
    if n >= 0:
        break
    else:
        print("Số liệu không hợp lệ! Nhập lại.")
print()

m = []
for i in range(n):
    k = sach()
    k.nhap()
    m.append(k)
    print()

print("Mã sách".ljust(25) + "Tên sách".ljust(25) + "Nhà xuất bản".ljust(25) + "Số trang sách".ljust(25) + "Giá tiền".ljust(25))
for k in m:
    k.xuat()
