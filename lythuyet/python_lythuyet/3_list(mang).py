#          0               1              2           3
lst1 = ['quang', 'công nghiệp hà nội', 'hà nam', 'quỳnh côi']
#         -4              -3            -2            -1
lst2 = [1, 2, 3, "hello world"]

lst1[0] = 'tống đăng quang' # thay thế phần tử
del lst1[0: 2] # xóa list
lst2 += ['ngân hàng'] # cộng phần tử

# cách để nhập một list tử bàn phím
n = int(input("Nhap n = "))
lst = []
def nhap(m, n):
    for i in range (n):
        a = int(input(f"m[{i}] = "))
        m.append(a)

# tạo một list mới từ list cũ mà trong list mới có những phần tử chứa kí tự 'a' ở list cũ
newlist = [x for x in lst if 'a' in x]

# Có thể dùng cách này cho ngắn gọn
my_list = [str(x) for x in input("Mời nhập list: ").split(',')]
print(my_list)

# có thể nhập từ bàn phím bất kì kiểu dữ liệu nào bằng cách này, chỉ cần thay đổi giữa list-set-tuple
a = set(input('nhập giá trị: ').split( ))
print(a)

lst4 = [lst1, lst2] # list nối tiếp list
lst5 = lst1 * 2 # nhân list
print(len(lst1)) # đếm phần tử list
print(lst1[1: 3]) # xuất list
lst1.extend(lst2) # thêm list này vào cuối list 
lst1.reverse() # đảo ngược list (không nhập gì vào trong ngoặc)
lst1.remove("hà nam") # xóa phần tử trong list (chỉ xóa phần tử đầu tiên)
lst1.insert(3, "an vinh") # thêm phần tử vào vị trí bất kì trên list
lst1.index("hà nam") # chỉ ra vị trí xuất hiện đầu tiên của phần tử
lst1.pop() # chỉ ra phần tử cuối cùng của list và xóa nó khỏi list
lst1.append("an vinh") # thêm phần tử vào cuối list
lst1.sort() # sắp xếp theo thứ tự bảng chữ cái và thứ tự tăng dần của số
lst1.clear() # xóa toàn bộ trong list, sau khi xóa list sẽ trả về rỗng
lst3 = lst1.copy() # sao chép từ list này sang chuỗi kia
lst1.count("hà nam") # đếm xem phần tử xuất hiện bao nhiêu lần trong list
print(type(lst1)) # kiểu tra kiểu dữ liệu
lst2 = list(lst) # tạo một bản sao của list bằng câu lệnh list()

lst6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(lst6)) # min trong list
print(max(lst6)) # max trong list

# Bài 1
'''Bài 1: Viết chương trình tạo ra 1 list có n phần tử, các phần tử
          là một số ngẫu nhiên từ(1, 100)'''
from random import randrange
n = int(input("Mời nhập số: "))
lst = [0] * n
for i in range(n):
    lst[i] = randrange(1, 100)
print(lst)
# Bài 2
'''Bài 2: Viết chương trình nhập vào một danh sách list sau đó: 
          a) Tạo ra một list mới bình phương các phần tử
          b) Xác định xem trong list có bao nhiêu phần tử lớn hơn 50'''
n = int(input("Mời nhập số phần tử của list: "))
lst = []
dem = 0
while dem < n:
    dem += 1
    a = int(input("Hãy nhập thêm phần tử cho list: "))
# câu a
    lst.append(a**2)
else:
    print("Bạn đã nhập đủ số phần tử trong list")
    print("List bạn nhận được là: ", lst)
# câu b
dem1 = 0
for i in lst:
    if i > 50:
        dem1 += 1
print("Số phần tử lớn hơn 50 trong list là: ", dem1)
# Bài 3
'''Bài 3: Viết chương trình trả về kết quả các phép tính
         list = ["2 + 5 + 7 =", "5 * 10 =", "sqrt(16) =", "12 % 2 =", "5 // 2 ="]'''

lst = ["2 + 5 + 7 =", "5 * 10 =", "16 ** 0.5 =", "12 % 2 =", "5 // 2 ="]
for i in lst:
    a = i.strip("=")
    b = eval(a)
    c = float(input(i))
    if b == c:
        print("True")
    else:
        print("False, đáp án đúng = ", b)

# tìm số nhỏ nhất trong list
n = int(input("Nhập số phần tử cho list: "))
lst = []
for i in range(n):
    lst.append(int(input()))
min_value = lst[0]
for i in lst:
    if i < min_value:
        min_value = i
print('Số nhỏ nhất trong list là: ', min_value)

# tính tổng phần tử trong list
n = int(input("Nhập số phần tử cho list: "))
dem = 0
lst = []
for i in range(n):
    dem += 1
    lst.append(int(input(f"Nhập giá trị {dem}/{n} của list: ")))
print(lst)
a = 0
for i in lst:
    a = a + i
print("Tổng các phần tử trong list = ", a)

# hàm nhập mảng
def nhap (m, n):
    for i in range(n):
        m.append(int(input(f"Nhap m[{i}] = ")))

# hàm xuất mảng
def xuat (m, n):
    for i in range (n):
        print(m[i], end = '\t')
    print()

# hàm tính bình phương các phần tử
def binhphuong (m, n):
    x = []
    for i in range(n):
        x.append(m[i]*m[i])
    for i in range (n):
        print (x[i], end = '\t')
    print()
        
# hàm đếm phần tử nhỏ hơn 50 trong mảng
def soluong(m, n):
    dem = 0
    for i in range(n):
        if (m[i] < 50):
            dem += 1
    print("So phan tu nho hon 50 trong mang la:", dem)

# hàm tìm phần tử nhỏ nhất trong mảng
def find (m, n):
    min_value = m[0]
    for i in range (n):
        if (m[i] < min_value):
            min_value = m[i]
    print("Phan tu nho nhat trong mang la: min_value =", min_value)

# hàm sắp xếp mảng tăng dần
def xep(m, n):
    for i in range (n):
        for j in range (i + 1, n):
            if (m[i] > m[j]):
                t = m[i]
                m[i] = m[j]
                m[j] = t

# hàm đảo ngược mảng
def dao_nguoc(m, n):
    s = 0
    e = n - 1
    while (s < e):
        t = m[s]
        m[s] = m[e]
        m[e] = t
        s += 1
        e -= 1

# hàm chèn mảng
def chen(m, n):
    k = int(input("Nhap vi tri muon chen: "))
    x = int(input("Nhap gia tri muon chen: "))
    m.insert(k, x)
    n += 1

# quick sort
def quick(m, l, r):
    if l < r:
        i = l
        j = r
        p = m[(l + r) // 2]

        while i <= j:
            while m[i] < p:
                i += 1
            while m[j] > p:
                j -= 1
            if i <= j:
                m[i], m[j] = m[j], m[i]  # Swap m[i] và m[j]
                i += 1
                j -= 1

        quick(m, l, j)  # Gọi đệ quy cho phần bên trái của pivot
        quick(m, i, r)  # Gọi đệ quy cho phần bên phải của pivot

# ghép mảng
def ghep(m, a, n, b):
    k = 0
    c = []
    for i in range(n):
        c.append(m[i])
        k += 1
    for i in range(b):
        c.append(a[i])
        k += 1
    xuat(c, k)

# tách mảng thành 2 mảng chẵn lẻ
def tach(m, n):
    c = []
    l = []
    for i in range(n):
        if m[i] % 2 == 0:
            c.append(m[i])
        else:
            l.append(m[i])

    print("Mang chan: ", end = '')
    xuat(c, len(c))
    print("Mang le: ", end = '')
    xuat(l, len(l))



n = int(input ("Nhap n = "))
m = []
print ("Nhap mang: ")
nhap(m, n)
print ('-'*40)
print ("Xuat mang:", end = '\t')
xuat(m,  n)
print ('-'*40)

print("Mang binh phuong cac phan tu mang:", end = '\t')
binhphuong(m, n)
print ('-'*40)

soluong(m, n)
print ('-'*40)

find (m, n)
print ('-'*40)

# print("Phan tu nho nhat trong mang la: min_value =", min(m))

xep(m, n)
print ("Mang tang dan:", end = '\t')
xuat(m, n)


