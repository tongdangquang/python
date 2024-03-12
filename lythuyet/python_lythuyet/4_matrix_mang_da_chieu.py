matrix = [
    [1, 2, 3, 4],
    [2, 5, 6, 4],
    [9, 8, 7, 2],
    [1, 8, 5, 6]
]
print(matrix) # in matrix(ma trận) ra màn hình
for i in matrix:
   # print(i) # chuyển ma trận từ hàng ngang thành hàng dọc
    for element in i:
        print("{:<10}".format(element), end = ' ') # tách các phần tử trong ngoặc [] thành các số tự nhiên thuộc kiểu int
    print()

# tạo 1 ma trận cỡ (a x b) với các phần tử cố định (dưới đây là 1)
a = 4
b = 3
matrix = [[1]*a]*b
print(matrix)
for i in matrix:
    print(i)

from random import randrange
# tạo 1 matrix với các phần tử ngẫu nhiên
lst = []
dong = int(input("Nhập số dòng cho ma trận: "))
cot = int(input("Nhập số cột cho ma trận: "))
for i  in range(dong):
    cot1 = []
    for i in range(cot):
        cot1.append(randrange(10, 100))
    lst.append(cot1)
print(lst)

'''có 2 cách xuất ma trận, như dưới đây'''
# cách 1
for i in lst:
    for e in i:
        print("{:<8}".format(e), end = ' ')
    print()
# cách 2
for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j], end = '\t')
    print()
# xuất hàng bất kỳ
s = int(input("Xuất hàng: "))
for i in range (len(lst)):
    if s == i:
        print(lst[i])

# nhập xuất mảng
d = int(input("Nhap so dong: "))
c = int(input("Nhap so cot : "))

m = [] 
for i in range (d):
    m1 = []
    for j in range(c):
        m1.append(int(input(f"Nhap m[{i}][{j}] = ")))
    m.append(m1)

print ("Matrix: ")
for i in range (d):
    for j in range (c):
        print (m[i][j], end = '\t')
    print()