# về bản chất thì quan hệ kết tập trong python cũng tương tự C++
class Teacher:
    def __init__(self, name = "", age = 0, major = "") -> None:
        self.name = name
        self.age = age
        self.major = major
    
    def nhap(self):
        self.name = str(input("Nhap ten giang vien: "))
        self.age = int(input("Nhap tuoi giang vien: "))
        self.major = str(input("Chuyen mon: "))

    def xuat(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Major: {self.major}")
    

class Phong:
    def __init__(self, classname = "", classcode = "") -> None:
        self.classname = classname
        self.classcode = classcode
        self.teachers = [] # kết tập ở đây

    def nhap(self):
        self.classname = str(input("Nhap ten lop: "))
        self.classcode = str(input("Nhap ma lop: "))
        self.num_teachers = int(input("Nhap so luong giang vien: "))
        for i in range(self.num_teachers):
            print(f"Nhap thong tin giang vien thu {i + 1}")
            teacher = Teacher() # kết tập ở đây
            teacher.nhap()
            self.teachers.append(teacher)
            print()

    def xuat(self):
        print(f"Class name: {self.classname}")
        print(f"Class code: {self.classcode}")
        print(f"So giang vien cua lop: {self.num_teachers}")
        for teacher in self.teachers: # kết tập ở đây
            teacher.xuat()
            print()

p1 = Phong()
p1.nhap()
p1.xuat()
