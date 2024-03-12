# Có nhiều cách thực hiện phương thức ghi đè, những đặc điểm nhận dạng chung và cũng là điều bắt buộc đó là 
# phương thức của lớp cha và phương thức của lớp con phải trùng tên
class Animal:
    def __init__(self, id, name, age, gender) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender

    # nhập thông tin animal
    def nhap_animal(self):
        self.id = str(input("Nhap id: "))
        self.name = str(input("Nhap name: "))
        self.age = int(input("Nhap age: "))
        self.gender = str(input("Nhap gender: "))
    
    # xuất thông tin animal
    def xuat_animal(self):
        print("Id:", self.id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
    

class Cat(Animal):
    def __init__(self, id, name, age, gender, color) -> None:
        super().__init__(id, name, age, gender)
        # Animal.__init__(self, id, name, age, gender)
        self.color = color

    # ghi đè phương thức nhap_animal() của lớp cha
    def nhap_animal(self):
        super().nhap_animal()
        # Animal.nhap_animal(self)
        self.color = str(input("Nhap mau long: "))
    
    # ghi đè phương thức xuat_animal() của lớp cha
    def xuat_animal(self):
        super().xuat_animal()
        # Animal.xuat_animal(self)
        print("Color:", self.color)


meo = Cat("1234", "baby", 2, "male", "yellow")
meo.nhap_animal()
print()
meo.xuat_animal()