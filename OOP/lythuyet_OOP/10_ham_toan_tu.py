class Toa_do:
# hàm khởi tạo __init__, hàm luôn được thực thi khi lớp được khởi tạo
    def __init__(self, a, b) -> None:
        self.x = a
        self.y = b

# toán tử chuyển đổi và biểu diễn chuỗi:
    # hàm biểu diễn class, hàm được gọi đến khi bạn sử dụng print. Ví dụ: print(object) 
    def __str__(self) -> str:
        return (f"({self.x}, {self.y})")
    # chuyển đối tượng thành chuỗi biểu diễn nó
    def __repr__(self) -> str:
        return (f"({self.x}, {self.y})")
        
# toán tử số học
    # toán tử cộng
    def __add__(self, other):
        return Toa_do(self.x + other.x, self.y + other.y)
    # toán tử trừ
    def __sub__(self, other):
        return Toa_do(self.x - other.x, self.y - other.y)
    # toán tử nhân
    def __mul__(self, other):
        return Toa_do(self.x * other.x, self.y * other.y)
    # toán tử chia
    def __truediv__(self, other):
        return Toa_do(self.x / other.x, self.y / other.y)
    # toán tử chia lấy nguyên
    def __floordiv__(self, other):
        return Toa_do(self.x // other.x, self.y // other.y)
    # toán tử chia lấy dư
    def __mod__(self, other):
        return Toa_do(self.x % other.x, self.y % other.y)

# toán tử so sánh
    # so sánh bằng ==
    def __eq__(self, other) -> bool:
        if(self.x == other.x and self.y == other.y):
            return True
        else:
            return False
    # so sánh khác !=
    def __ne__(self, other) -> bool:
        if(self.x == other.x and self.y == other.y):
            return False
        else:
            return True
    # so sánh nhỏ hơn < và nhỏ hơn hoặc bằng <=
    def __lt__(self, other):
        if(self.x < other.x and self.y < other.y):
            return True
        else:
            return False
    # so sánh nhỏ hơn > hoặc lớn hơn hoặc bằng >=
    def __le__(self, other):
        if(self.x > other.x and self.y > other.y):
            return True
        else:
            return False
    
# p1 = Toa_do(3, 4)
# p2 = Toa_do(3, 5)
# # print(p1) # in đối tượng sử dụng hàm __str__ và __repr__
# print(f"{p1} + {p2} = {p1 + p2}") # sử dụng hàm toán tử cộng và trừ



# toán tử so sánh
class Songuyen:
    def __init__(self, n) -> None:
        self.x = n

    def __str__(self) -> str:
        return f"Giá trị trả về: {self.x}"
    
    # so sánh bằng ==
    def __eq__(self, other) -> bool:
        if(self.x == other.x):
            return True
        else:
            return False
    # so sánh khác !=
    def __ne__(self, other) -> bool:
        if(self.x != other.x):
            return False
        else:
            return True
    # so sánh nhỏ hơn < và nhỏ hơn hoặc bằng <=
    def __lt__(self, other):
        if(self.x < other.x):
            return True
        else:
            return False
    # so sánh nhỏ hơn > hoặc lớn hơn hoặc bằng >=
    def __le__(self, other):
        if(self.x > other.x):
            return True
        else:
            return False
        
# toán tử gán
    # cộng và gán
    def __iadd__(self, other):
        if(isinstance(other, Songuyen)):
            self.x += other.x
            return self
        else:
            raise TypeError("Không cùng kiểu đối tượng")
        
    # trừ và gán
    def __isub__(self, other):
        if(isinstance(other, Songuyen)):
            self.x -= other
            return self
        else:
            raise TypeError("Không cùng kiểu đối tượng")

    # nhân và gán
    def __isub__(self, other):
        if(isinstance(other, Songuyen)):
            self.x *= other
            return self
        else:
            raise TypeError("Không cùng kiểu đối tượng")
    
    # chia và gán
    def __isub__(self, other):
        if(isinstance(other, Songuyen)):
            self.x /= other
            return self
        else:
            raise TypeError("Không cùng kiểu đối tượng")

sn1 = Songuyen(10)
sn2 = Songuyen(20)
print(sn1 == sn2) # sử dụng toán tử =
print(sn1 < sn2)
sn1 = Songuyen(10)
sn2 = Songuyen(20)
sn1 += sn2 # sử dụng toán tử cộng và gán
print(sn1)



# toán tử logic
class Doi_tuong_logic:
    def __init__(self, gia_tri) -> None:
        self.value = gia_tri
    
    def __str__(self) -> str:
        return f"Giá trị trả về: {self.value}"
    
    # toán tử and
    def __and__(self, other):
        if(isinstance(other, Doi_tuong_logic)): # hàm isinstance() để kiểm tra xem 2 đối tượng có thuộc 1 lớp cụ thể hay không
            return Doi_tuong_logic(self.value and other.value)
        else:
            # từ khóa raise dùng để trả về 1 giá trị ngoại lệ
            raise TypeError("Loại toán hạng không được hỗ trợ: Bạn chỉ có thể sử dụng AND logic giữa hai đối tượng DoiTuongLogic")
    
    # toán tử or
    def __or__(self, other):
        if(isinstance(other, Doi_tuong_logic)):
            return Doi_tuong_logic(self.value or other.value)
        else:
            raise TypeError("Loại toán hạng không được hỗ trợ: Bạn chỉ có thể sử dụng OR logic giữa hai đối tượng DoiTuongLogic")

    # toán tử not
    def __not__(self):
        return Doi_tuong_logic(not self.value)
        
# tạo 2 đối tượng logic
logic1 = Doi_tuong_logic(True)
logic2 = Doi_tuong_logic(False)
print(logic1 & logic2) # sử dụng toán tử and
print()
print(logic1 | logic2) # sử dụng toán tử or
print()
print(not logic1) # sử dụng toán tử not