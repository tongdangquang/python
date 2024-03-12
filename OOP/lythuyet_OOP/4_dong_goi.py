# sử dụng thuộc tính private trong lập trình hướng đối tượng python
# Để truy cập đến những thuộc tính riêng tư của 1 class ta phải sự dụng tên biến đổi như sau:
# _tên lớp__tên thuộc tính riêng tư
# cũng có thể truy cập đến thuộc tính riêng tư bằng getter và setter
class Myclass:
    def  __init__(self) -> None:
        self.__private_variable = 20
    
obj = Myclass()
obj._Myclass__private_variable = 100 # thay đổi giá trị của thuộc tính riêng tư
# print(obj.__private_variable) # Chương trình báo lỗi không thể truy cập đến thuộc tính riêng tư
print(obj._Myclass__private_variable) # Chương trình in ra giá trị của __private_vairable


# class bank():
#     def __init__(self, name, cccd):
#         self.name = name # thuộc tính public trong lớp
#         self.cccd = cccd  

# class staff(bank):
#     def __init__(self, name, cccd):
#         super().__init__(name, cccd)
#         self.__luong = 5000 # sử dụng __ để khai báo thuộc tính riêng tư trong lớp
#         # self._luong = 5000 # sử dụng _ đẻ khai báo thuộc tính protected

#     # setter và getter để truy cập đến các thuộc tính riêng tư
#     def getluong(self):
#         return self.__luong
    
#     def setluong(self, luong_moi):
#         self.__luong = luong_moi


# s1 = staff("quang", 12234)
# s1.setluong(1000) # sử dụng setter để truy cập vào thuộc tính private