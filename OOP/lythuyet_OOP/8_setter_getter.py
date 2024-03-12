# SỬ DỤNG SETTER VÀ GETTER THÔNG THƯỜNG
class RAM:
    def __init__(self, storage, speed) -> None:
        self._storage = storage
        self._speed = speed

    # sử dụng getter để trả về giá trị của thuộc tính trong class
    def get_storage(self):
        return self._storage
    def get_speed(self):
        return self._speed
    
    # sử dụng setter để đặt giá trị cho thuộc tính trong class
    def set_storage(self, new_storage):
        self._storage = new_storage
    def set_speed(self, new_speed):
        self._speed = new_speed

ram = RAM(8, 3200)
# sử dụng getter
sto1 = ram.get_storage()
sp1 = ram.get_speed()
print("Storage of RAM:", sto1)
print("Speed of RAM:", sp1)
print()

# sử dụng setter
ram.set_storage(16)
ram.set_speed(2500)
sto2 = ram.get_storage()
sp2 = ram.get_speed()
print("Storage of RAM is changed:", sto2)
print("Speed of RAM is changed:", sp2)

    
# SỬ DỤNG SETTER VÀ GETTER TRONG property
class Myclass:
    def __init__(self, variable) -> None:
        self._my_variable = variable

    # getter
    @property
    def my_variable(self):
        return self._my_variable
    
    # setter
    @my_variable.setter
    def my_variable(self, new_value):
        self._my_variable = new_value

    # deleter
    @my_variable.deleter
    def my_variable(self):
        print("Deleted")
        del self._my_variable

obj = Myclass(10)
# sử dụng getter để đọc giá trị thuộc tính
print(obj.my_variable)

# sử dụng setter để thay đổi giá trị thuộc tính
obj.my_variable = 20
print(obj.my_variable)

# sử dụng deleter để xóa thuộc tính
del obj.my_variable


