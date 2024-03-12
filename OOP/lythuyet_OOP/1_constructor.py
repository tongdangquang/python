# KHỞI TẠO KHÔNG THAM SỐ
class teacher1:
    # cách 1:
    # name = "Nguyen Thị A"
    # age = 30
    # major = "Information Technology"

    # cách 2:
    def __init__(self):
        self.name = "Nguyen Thị A"
        self.age = 30
        self.major = "Information Technology"

# KHỞI TẠO CÓ THAM SỐ
class teacher2:
    # phương thức khởi tạo có tham số
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
    
    # # phương thức khởi tạo không có tham số
    # def __init__(self):
    #     self.name = "unknown"
    #     self.age = 0
    #     self.major = "unknown"

    # trong trường hợp như trên, chúng ta muốn tách 2 constuctor thì phải đặt constructor không đối số ở dưới và có đối số ở trên,
    # nếu không chương tình sẽ không chạy vì còn tên constuctor __init__ sẽ liên quan đến vấn đề ghi đè. 
    # Vì thế ta có thể kết hợp 2 constructor thành 1 constructor như sau: 
    def __init__(self, name = "unknown", age = 0, major = "unknown"):
        self.name = name
        self.age = age
        self.major = major

    # phương thức nhập
    def nhap(self):
        self.name = str(input("Nhap ten giao vien: "))
        self.age = int(input("Nhap tuoi giao vien: "))
        self.major = str(input("Nhap nganh chuyen mon: "))

    # phương thức xuất
    def xuat(self):
        print(f"Ten giao vien: {self.__name}")
        print(f"Tuoi giao vien: {self.__age}")
        print(f"Chuyen nganh: {self.__major}")
    

# tạo đối tượng 
t1 = teacher2()
t1.xuat()
print('-'*35)

t2 = teacher2("quang", 20, "httt")
t2.xuat()
print('-'*35)

t3 = teacher2()
t3.nhap()
print('-'*35)
t3.xuat()

