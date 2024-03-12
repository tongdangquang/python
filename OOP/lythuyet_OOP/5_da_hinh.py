# Từ "đa hình" có nghĩa là "nhiều dạng" và trong lập trình, 
# nó đề cập đến các phương thức/hàm/toán tử có cùng tên có thể được thực thi trên nhiều đối tượng hoặc lớp.
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self): # trùng tên phương thức
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self): # trùng tên phương thức
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self): # trùng tên phương thức
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

# đa hình thể hiện ở đây
for x in (car1, boat1, plane1):
  x.move()






# ĐA HÌNH TRONG KẾ THỪA HAY CŨNG CHÍNH LÀ PHƯƠNG THỨC GHI ĐÈ
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self): # trùng tên phương thức
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self): # trùng tên phương thức
    print("Sail!")

class Plane(Vehicle):
  def move(self): # trùng tên phương thức
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  # gọi đến đối tượng nào thì in ra thuộc tính của đối tượng đó
  print(x.brand)
  print(x.model)
  x.move()
  print()