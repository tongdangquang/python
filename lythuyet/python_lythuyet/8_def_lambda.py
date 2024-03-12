# cú pháp hàm lambda: lambda arguments: expression

# ví dụ đơn giản về hàm lambda
a = lambda so: so + 99
print(a(1))
# tương đương với hàm define như sau:
def a(so):
    return so + 99
print(a(1))

# hàm lambda với nhiều nhiều đầu vào
b = lambda x, y, z: x+y+z - x*y*z
print(b(2, 4, 5))


# lambda trong hàm sorted (dùng để sắp xếp các phần tử)
lst = [(1, 2,-2), (-1, 5, 0), (7, 4, 6), (4, 5, -3), (9, 4, -8)]
c = sorted(lst, key = lambda x: x[1])
print(c)
# sắp xếp theo trị tuyệt đối
lst2 = [1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6]
d = sorted(lst2, key = lambda x: abs(x))
print(d)


# sử dụng hàm lambda trong hàm map (ví dụ để viết hoa)
lst = ['tống', 'đăng', 'quang']
e = list(map(lambda x: x.title(), lst))
print(e)
# ta có thể viết hoa mà không nhất thiết phải dùng đến hàm lambda với hàm map như trên
lst2 = ['tống', 'đăng', 'quang']
f = [keyword.title() for keyword in lst2]
print(f)
# tổng quan
n = [str(x) for x in input("Nhập list: ").split()]
g = [kw.title() for kw in n]
print(g)
for i in g:
    print(i, end = ' ')


# sử dụng hàm lambda trong hàm filter
# ví dụ in ra số lẻ trong list
lst = [1, 2, 3, 4, 5, 8, 9, 6, 7, 3, 4]
h = list(filter(lambda x: x % 2 != 0, lst))
h = [x for x in lst if x % 2 != 0] # cũng có thể dùng cái này
print(h)


# hàm lambda trong hàm reduce
from functools import reduce
s = [1, 2, 3, 5, 6, 4, 7, 9, 8, 10]
i = reduce(lambda a, b: a+b, s) # in ra tổng của list
k = reduce(lambda a, b: a if a > b else b, s) # in ra số lớn nhất trong list
print(i)
print(k)