class mang():
    # phương thức khởi tạo
    def __init__(self, n = 0) -> None:
        self.n = n 
        self.m = []

    # phương thức nhập mảng
    def nhap(self):
        while True:
            self.n = int(input("Nhập số lượng phần tử của mảng (n >= 0): "))
            if self.n >= 0:
                break
            else:
                print("Số không hợp lệ! Nhập lại.")
        for i in range(self.n):
            self.m.append(float(input(f"Nhập m[{i}] = ")))

    # phương thức xuất mảng
    def xuat(self):
        for i in self.m:
            print(i, end = " ")

    # phương thức sắp xếp mảng tăng dần
    def tangdan(self):
        self.m.sort()

    # phương thức sắp xếp mảng giảm dần
    def giamdan(self):
        self.m.sort(reverse=True)

    # phương thức tìm phần tử max trong mảng
    def Max(self):
        return max(self.m)
    
    # phương thức tìm phân tử min trong mảng
    def Min(self):
        return min(self.m)

k = mang()
k.nhap()
print()

print("Mảng vừa nhập: ", end = " ")
k.xuat()
print()

print("Mảng tăng dần: ", end = " ")
k.tangdan()
k.xuat()
print()

print("Mảng giảm dần: ", end = " ")
k.giamdan()
k.xuat()
print()

print(f"Phần tử lớn nhất trong mảng: {k.Max()}")
print(f"Phần tử nhỏ nhất trong mảng: {k.Min()}")
