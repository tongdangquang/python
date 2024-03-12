# lớp cha
class Person():
    # hàm khởi tạo
    def __init__(self, name = "", age = 0, hometown = "") -> None:
        self.__name = name # thuộc tính tiêng tư __
        self.__age = age
        self.__hometown = hometown

    def nhap(self):
        self.__name = str(input("Nhap ten: "))
        self.__age = int(input("Nhap tuoi: "))
        self.__hometown = str(input("Nhap que quan: "))

    def xuat(self):
        print(f"Ho ten: {self.__name}")
        print(f"Tuoi: {self.__age}")
        print(f"Que quan: {self.__hometown}")

# lớp con
class Student(Person):
    # hàm khởi tạo
    def __init__(self, name = "", age = 0, hometown = "", ma = 0, major = "") -> None:
        # có thể dùng hàm super() hoặc dùng tên lớp cha để kế thừa thuộc tính của lớp cha
        super().__init__(name, age, hometown)
        # Person.__init__(self, name, age, hometown)
        self.__ma = ma
        self.__major = major

    def nhap(self):
        Person.nhap(self) # reuse code
        self.__ma = int(input("Nhap ma sinh vien: "))
        self.__major = str(input("Nhap chuyen nganh: "))
    
    def xuat(self):
        Person.xuat(self) # reuse code
        print(f"Ma sinh vien: {self.__ma}")
        print(f"Chuyen nganh: {self.__major}")

# TH1: hàm khởi tạo có đối số thì có thể truyền hoặc không truyền data vào Student() ở sv1 = Student()
# TH2: hàm khởi tạo không có đối số thì bắt buộc phải truyền data vào Student() ở sv1 = Student()
sv1 = Student("quang", 20, "thai binh", 2022, "it")
sv1.nhap()
sv1.xuat()


# class item():
#     def __init__(self, name: str, price: float, quantity) -> None:
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#         # kiểm tra điều kiện thuộc tính (nằm trong hàm thuộc tính)
#         assert price > 0
#         assert quantity > 0

#     # khởi tạo phương thức thông thường
#     def tong_gia(self):
#         return self.price * self.quantity

#     # khởi tạo phương thức tĩnh
#     @staticmethod
#     def check(price):
#         if (price < 500):
#             print("Cheap, dat o tang 1")
#         else:
#             print("Expensive, dat o tang 2")


# # khởi tạo class con
# class phone(item):
#     def __init__(self, name: str, price: float, quantity, kind) -> None:
#         super().__init__(name, price, quantity)
#         self.kind = kind


# p1 = phone("Iphone 13", 1000, 5, "5G")
# print ()

