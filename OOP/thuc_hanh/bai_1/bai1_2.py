class rectangle():
    # phương thức khởi tạo
    def __init__(self, d = 0, r = 0) -> None:
        self.d = d
        self.r = r

    # hàm nhập thông tin HCN
    def nhap(self):
        self.d = int(input("Nhập chiều dài HCN : "))
        self.r = int(input("Nhập chiều rộng HCN: "))

    # hàm vẽ HCN
    def ve(self):
        for i in range(self.d):
            for j in range(self.r):
                print("*", end = " ")
            print()

    # hàm tính chu vi HCN
    def cv(self):
        return (self.d + self.r)*2
    
    # hàm tính diện tích HCN
    def dt(self):
        return self.d*self.r
    
k = rectangle()

k.nhap()

print()
k.ve()
print()

print(f"Chu vi HCN: {k.cv()}")
print(f"Diện tích HCN: {k.dt()}")
        