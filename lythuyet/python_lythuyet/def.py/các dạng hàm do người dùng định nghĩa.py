# 1: Hàm không có tham số và không có giá trị trả về
def hello():
    print("hello world")
a = hello()

# 2: Hàm có tham số và không có giá trị trả về
def hello(tên):
    print("Hello " + tên.title())
name = "quang"
hello(name)

# 3: Hàm với nhiều tham số
def sum(a, b, c):
    print("Tổng 3 số = ", a + b + c)
a = int(input("Nhập giá trị a = "))
b = int(input("Nhập giá trị b = "))
c = int(input("Nhập giá trị c = "))
sum1 = sum(a, b, c)

# 4: Hàm với số lượng tham số có thể thay đổi được
# cách 1
def sum_5_so(a, b, c, d, e):
    print(a + b + c + d + e)
x1, x2, x3, x4, x5 = 1, 2, 3, 4, 5
sum1 = sum_5_so(x1, x2, x3, x4, x5)
# cách 2
def sum_nhieu_so (*a):
    tong = 0
    for s in a:
        tong += s
    print(tong)
a, b, c, d, e, f, g = 12, 13, 14, 15, 16, 17, 18
sum_nhieu_so(a, b, c, d, e, f, g)

# 5: Hàm có tham số có giá trị mặc định
def user (ten, tuoi = '20'):
    print("Tên tôi là: " + ten.title())
    print("Tuổi tôi là: " + tuoi)
name = "Tống Đăng Quang"
user(name)

# 6: Hàm có giá trị trả về (có return)
def user(ho, dem, ten):
    ho_va_ten = ho + " " + dem + " " + ten
    return ho_va_ten.title()
a = "tống"
b = "đăng"
c = "quang"
print(user(a, b, c))
