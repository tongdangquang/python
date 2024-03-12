# class variable trong python cũng chính là static(biến tĩnh) trong C++

class myclass:
    class_variable = 0 # class variable (biến lớp)

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable # biến instrance variable (biến thể hiện)

obj1 = myclass(1)
obj2 = myclass(2)

print(obj1.class_variable) # class variable có thể truy cập qua đối tượng
print(obj2.class_variable) 
print(myclass.class_variable) # class variable có thể truy cập qua tên lớp

myclass.class_variable = 10 # khi thay đổi class variable thì sẽ thay đổi ở cả 2 đối tượng
print(obj1.class_variable) 
print(obj2.class_variable)

obj1.class_variable = 20 # khi thay đổi class variable ở đối tượng 1 thì class variable ở đối tượng 2 không thay đổi
print(obj1.class_variable) # class variable thay đổi
print(obj2.class_variable) # class variable không thay đổi
