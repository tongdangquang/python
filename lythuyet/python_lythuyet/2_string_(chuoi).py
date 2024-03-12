#    012345678901234
a = "tống đăng quang"
#   -543210987654321
b = "đại học công nghiệp hà nội"
c = a + " " + b # cộng hai chuỗi
d = "*" * 20 # nhân chuỗi

print(a[3]); a[1: 3: 1]; a[3: 6]; a[3:]; a[:3]; a[::-1] # xuất kí tự ở vị trí n

# CÁC HÀM QUAN TRỌNG
print(len(a)) # đếm số kí tự trong chuỗi (chiều dài chuỗi)
print("tống" in a) # kiểm tra xem kí tự có nằm trong chuỗi không
a.find("g", '''start''', '''end''') # tìm vị trí đầu tiên của phần tử trong chuối hoặc khoảng chuỗi
a.rfind() # tìm vị trí cuối cùng của phần tử trong chuỗi
a.index() # giống hàm find bên trên nhưng nếu không tìm thấy sẽ báo là ngoại lệ
a.rindex() # tìm vị trí cuối cùng của phần tử trong chuỗi, nếu không tìm thấy sẽ báo là ngoại lệ
a.isalnum() # kiểm tra xem có phải chuối chỉ chứa kí tự số và chữ không
a.isalpha() # kiểm tra xem có phải chuỗi chứa duy nhất kí tự chữ hay không
a.isdigit() # kiểm tra xem có phải chuỗi chứa duy nhất kí tự số hay không
a.isdecimal() # kiểm tra xem chuỗi có phải chỉ chứa các phần tử thập phân hay không
a.islower() # kiểm tra xem có phải chuỗi chứa duy nhất kí tự chưa in thường hay không
a.isupper() # kiểm tra xem có phải chuỗi chứa duy nhất kí tự chưa in hoa hay không
a.isnumeric() # kiểm tra xem có phải chuỗi chứa duy nhất kí tự số hay không
a.isspace() # kiểm tra xem có phải chuỗi chỉ chứa kí tự trống hay không
a.istitle() # kiểm tra xem chuỗi có phải là tiêu đề hay không, nếu là tiêu đề thì các chữ cái đầu phải viết hoa
a.join(d) # thêm chuỗi này vào cuối chuỗi kia và trả về 1 chuỗi bao gồm cả 2 chuỗi xen kẽ nhau
a.lower() # chuyển chuỗi về dạng chữ thường
a.upper() # chuyển chuỗi về dạng chữ hoa
a.strip() # loại bỏ kí tự thừa ở cả đầu và cuối chuỗi, như kiểu (lstrip + rstrip)
a.replace() # hàm này có tác dụng tìm và thay thế, cú pháp hơi dài nên lên google tìm hiểu
max(a) # trả về chữ cái cuối cùng trong bảng chữ cái xuất hiện trong chuỗi
min(a) # trả về chữ cái đầu tiên trong bảng chữ cái xuất hiện trong chuỗi
a.title() # chuyển chuỗi sang dạng tiêu đề
a.swapcase() # chuyển chuỗi sang dạng nghịch đảo (hoa sang thường và ngược lại)
a.split('kí tự cần tìm và tách chuỗi ở chỗ đó, số lượng phần tử theo thứ tự trái sang phải chuyển thành list') # chuyển string sang list
a.startswith() # hàm này kiểm tra xem chuỗi hoặc khoảng chuỗi có phải bắt đầu bởi kí tự nào đó không
x = "python"
print("p" in x) # kiểm tra xem một chuỗi có nằm trong chuỗi khác hay không
print("p" not in x) # kiểm tra xem một chuỗi có không nằm trong chuỗi khác hay không
# HẾT

a.capitalize() # in hoa chữ cái đầu tiên trong chuỗi
a.center(40, "*") # trả về chuối được hiển thị ở giữa một chuỗi, ở đây chuỗi a hiển thị giữa chuối *
a.count("g", '''start''', '''end''') # xem trong chuỗi có bao nhiêu kí tự từ đoạn start đến end
a.decode() # giải mã chuỗi trong python
a.encode() # mã hóa một chuỗi
a.endswith("g", '''start''', '''end''') # kiểm tra xem chuỗi hoặc khoảng chuỗi có được kết thúc bằng kí tự nào đó hay không
a.expandtabs() # tìm kiếm và thay thế kí tự \t bằng một khoảng trống
a.ljust(100, "*") # trả về một chuỗi với độ dài xác định (100) nếu chuỗi không đủ thì sẽ bù (*) vào bên phải chuỗi
a.ljust(100, "*") # như bên trên những hàm này là bù vào bên trái chuỗi
a.zfill() # hàm này như hàm ljust() những nó chỉ thêm được kí tự "0" vào đầu chuỗi
a.lstrip("*") # loại bỏ kí tự thừa ở đầu chuỗi nếu có ví dụ như (*)
a.rstrip() # như lstrip những loại kí tự ở cuối chuỗi
a.splitlines() # hàm này tách chuỗi khi gặp các kí tự \n

# Bài 1:
'''Bài 1: Viết chương trình in ra vị trí của kí tự a trong chuỗi 
         'university of technology and education' ra màn hình'''
a = "university of technology and education"
b = ""
for i in range(len(a)):
    if a[i] == "a":
        b = b + " " + str(i)
print(b)

# Bài 2:
'''Bài 2: Cho chuỗi s = "english = 78 science = 83 math = 68 history = 65"
1. Tính tổng các số trong chuỗi
2. Tính trung bình cộng'''

s = "english = 78 science = 83 math = 68 history = 65"
def tinh (s):
    a = s.split()
    b = 0
    dem = 0
    for i in a:
        if i.isdigit():
            b += int(i)
            dem += 1
    c = b/dem
    print ("Tong day so =", b)
    print ("Trung binh cong day so:", c)

# Bài 3:
'''Bài 3: Viết chương trình tính số nguyên âm trong chuỗi bất kì. 
        Nguyên âm bao gồm (u, e, o, a, i)'''
n = str(input("Mời bạn nhập chuỗi: "))
dem = 0
for i in n:
    if i in {"u", "e", "o", "a", "i"}:
        dem += 1
print(f"Số nguyên âm trong chuỗi {n} là: {dem}")

# Bài 4:
'''Bài 4: Viết chương trình kiểm tra tính hợp lệ của mật khẩu.
        - Mật khẩu hợp lệ khi có ít nhất 6 kí tự chứa
          ít nhất 1 chữ cái(chữ thường hoặc chữ hoa đều được)
          và chứa ít nhất 1 kí tự số
        - Cho người dụng nhập và để log in và so sánh, nếu đúng thì mở cửa,
          nếu sai quá năm lần thì nghỉ.'''
# 1
n = str(input("Mời bạn nhập mật khẩu: "))
x = bool
y = bool
for i in n:
    if i.isdigit():
        x = True
        break
    else:
        x = False
for i in n:
    if i.isalpha():
        y = True
        break
    else:
        y = False
while len(n) < 6 or x == False or y == False:
    n = input("Nhập lại mật khẩu: ")
else:
    print("Mật khẩu hợp lệ")
# 2
s = input("Mời nhập mật khẩu để đăng nhập hệ thống: ")
dem = 0
while s != n:
    dem += 1
    s = input(f"Mời nhập lại mật khẩu, bạn đã nhập sai {dem}/5 lần: ")
    if dem == 5:
        print("Bạn đã nhập sai quá 5 lần")
        break
else:
    print("Đăng nhập thành công")





# hàm nhập mảng
def nhap (m, n):
    for i in range(n):
        m.append(int(input(f"Nhap m[{i}] = ")))
    print()

# hàm xuất mảng
def xuat (m, n):
    for i in range (n):
        print(m[i], end = '\t')
    print ()

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
