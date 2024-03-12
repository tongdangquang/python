# hàm đối sổ là hàm có thể gắn biến, hàm không đối số là hàm không thể gắp biến
'''+ Khái niệm: Hàm là một khối lệnh đặc biệt, nó được đặt tên 
   và có thể gọi để sử dụng ở các nơi khác nhau trong chương trình.
   + Ý nghĩa, bản chất: hàm chính là khối lệnh có thể tái sử dụng'''

# Hàm có đối số (có return)
def tong (ds):
    sum = 0  # biến cục bộ
    for i in ds:
        sum += i
    return sum
ds1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ds2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 21]
sum1 = tong(ds1)
sum2 = tong(ds2)
print('Tổng của danh sách 1 là:', sum1)
print('Tổng của danh sách 2 là:', sum2)
'''khi viết chương trình đến đây, bây giờ ta có thể nhập bất kì giá trị (ds) 
 nào để tính toán mà không câng phải viết là 1 chương trình tương tự như vậy'''

# Hàm không đối số (không có return)
def xuatchuoi(chuoi):
    print(chuoi)
chuoi = input("Nhập 1 chuỗi: ")
b = xuatchuoi(chuoi)

# biến toàn cục (Global variable) là biến nằm ngoài hàm def
# biến cục bộ (Local variable) là biến nằm trong hàm def

'''Đệ quy là cách dùng hàm để tự gọi lại chính nó.
   Để giả bằng đệ quy cần 2 điều kiện:
    + Điểm dừng của bài toán
    + Quy luật của bài toán'''
'''Bài 1: Tính n! = n*(n - 1)*(n - 2)*(n - 3)*...*3*2*1 (Nếu biết (n - 1)! thì sẽ tính được n!)'''
n = int(input("Nhập số n = "))
def giaithua(a):
    if a == 0:
        return 1
    else:
        return a*giaithua(a - 1)
b = giaithua(n)
print(b)
