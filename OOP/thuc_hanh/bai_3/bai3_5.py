class array:
    # phương thức khởi tạo
    def __init__(self, n) -> None:
        self.m = []
        self.n = 0
        for i in range(self.n):
            self.m[i] = 0

    # phương thức hủy
    def __del__(self):
        self.n = 0

    def nhap(self):
        while True:
            self.n = int(input("Nhập số lượng phần tử của mảng: "))
            if self.n > 0:
                break
            else:
                print("Số liệu không hợp lệ")

        for i in range(self.n):
            self.m.append(int(input(f"Nhập [{i}] = ")))
    
    def xuat(self):
        for i in self.m:
            print(i, end=" ")
        print()

a = array(5)
a.nhap()
print()
print("Mảng vừa nhập:", end=" ")
a.xuat()
del a