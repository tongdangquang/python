''' + Numpy là viết tắt của Numerical Python.
    + Numpy là một thư viện viết tắt của python được sử dụng để làm việc với các mảng, ma trận.
    + Numpy nhằm mục đích cung cấp một đối tượng mảng nhanh hơn tới 50 lần so với danh sách python truyền thống.'''
import numpy as np
lst = [
    [12, 23, 4],
    [1, 6, 7],
    [44, 55, 77],
    [56, 9000, 26]
]
a = np.array(lst) # chuyển một list sang array (mảng)
print(a)

# các hàm cơ bản của numpy
print('số chiều của mảng:', a.ndim) # kiểm tra xem mảng này là mảng mấy chiều
print('size:', a.shape) # kiểu tra số hàng, cột, trả về (hàng, cột)
print('số phần tử',a.size) # số phần tử của array

# tạo array từ 1 list có sẵn
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = np.array(lst).reshape(3, 3) # đưa về array cỡ 3x3
print(a)

a = np.arange(0, 100, 1) # tạo array từ một dãy theo arange(begin, end, step)
a = np.linspace(1, 10, 5) # tạo array các phần tử cách đều nhau linspace(begin, end, số phần tử trong mảng)
a = np.full([3, 5], 6.9) # tạo array cỡ 3x5 với các phần tử đều là 6.9
a = np.zeros([3, 4], dtype = int) # tạo ra mảng chỉ có số 0
a = np.ones([3, 4], dtype = int) # tạo ra mảng chỉ có số 1

print(a[0, 1]) == print(a[0][1]) # xuất phần từ ở [dòng, cột]
print(a[0, :]) # xuất các phần tử ở dòng 0
print(a[:, -1]) # xuất các phần tử ở cột cuối
print(a[1:3, 1]) # xuất phần tử tử thuộc dòng 1 đến 3 nằm trong cột 1
a[1,1] = 100 # thay giá trị trong array

print(55 in a) # kiểm tra xem phần tử có nằm trong mảng hay không
# kiểm ra xem phần tử nằm ở vị trí nào trong mảng
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        if a[i, j] == 44:
            print(f"dòng {i} cột {j}")

# numpy kết hợp với random
import random
np.random.seed(0)  # này dùng để giữ nguyên câc phần tử 
a = np.random.random((4, 4)) # tạo array ngẫu nhiên
b = np.random.randint(0, 10, [4, 4]) # tạo ra một array với các phần tử từ 0-10 vã cỡ 4x4
print(b)
# nối array
x = np.array([[1, 2, 3, 4], 
              [3, 4, 2, 3]])
y = np.array([[1, 7, 6, 5],
              [5, 6, 3, 2]])
c = np.concatenate((x, x), axis = 0) # nhân đôi 1 array, nếu axis = 0 thì nối theo chiều dọc còn nếu axis = 1 thì nối theo chiều ngang
d = np.vstack((x, y)) # nối 2 array với nhau theo chiều dọc
e = np.hstack((x, y)) # nối 2 array với nhau theo chiều ngang
print(e)

# tách array (rất quan trọng)
f = np.array([0,1,2,3,4,5,6,7,8])
x1, x2, x3 = np.split(f, [3, 6])
print(x1)

# đại số tuyến tính với numpy
a = np.random.randint(0, 10, size=(3,3))
b = np.random.randint(0, 10, size=(3,3))
x = np.sort(a, axis=0) # sắp xếp thứ tự từ bé đến lớn theo cột
y = np.sort(a, axis=1) # sắp xếp thứ tự từ bé đến lớn theo hàng
c = a.dot(b) # nhân 2 ma trận với nhau
d = a @ b # cũng có thể dùng cách này để nhân 2 ma trận 
e = a.T # ma trận chuyển vị a
e = np.transpose(a) # cũng có thể chuyển vị theo cách này
e = np.linalg.det(a) # tính định thức ma trận
rank = np.linalg.matrix_rank(a) # tính hạng ma trận
f = np.linalg.inv(a) # tìm ma trận nghịch đảo
z = np.linalg.eig(a) # tính giá trọn riêng và vecto riêng
x = np.linalg.solve(a, b) # tìm nghiệm của hệ phương trình (giải phương trình ma trận)

# các phép tính với ma trận
a = np.array([[1,2,3]])
b = np.array([[4,3,7]])
c = a + b
d = a - b
e = a * b
f = a / b
print("A = {0}".format(a))
print("B = {0}".format(b))
print('A + B = {0}'.format(c))
print('A - B = {0}'.format(d))
print('A * B = {0}'.format(e))
print('A / B = {0}'.format(f))

''' Bài 1: viết chương trình tạo 1 array 2 chiều với viền là số 1 còn toàn bộ bên trong là số 0'''
import numpy as np
a = np.zeros((5, 5))
a[0, :] = 1 # dòng đầu
a[:, -1] = 1 # cột cuối
a[-1, :] = 1 # dòng cuối
a[:, 0] = 1 # cột đầu
#a[1:-1, 1:-1] = 0 # có thể dùng cái này nhưng phải đổi zeros() thành ones()
print(a)

'''Bài 2: viết chương trình toàn số 0 ở ngoài viền và bên trong toàn số 1'''
b = np.ones((5, 5))
b[0,:] = 0
b[:, 0] = 0
b[-1, :] = 0
b[:, -1] = 0
#b[1:-1, 1:-1] = 1 # có thể dùng cái này nhưng phải đổi ones() thành zeros()
print(b)

''' Bài 3: tạo 1 array bằng numpy với cột lẻ thì bằng 1, cột chẵn bằng 0'''
import numpy as np
a =  np.zeros((8, 8))
for i in range(a.shape[1]+1):
    if i % 2 != 0:
        a[0:8, i] = 1
print(a)


# ứng dụng
# kết hợp numpy, random và pandas để tạo ra một bảng giá
import pandas as pd
sales_amounts = np.random.randint(10, 20, size=(7, 3))
weekly_sales = pd.DataFrame(sales_amounts, index=['Thứ 2', 'Thứ 3', 'Thứ 4', 'Thứ 5', 'Thứ 6', 'Thứ 7', 'CN'],
columns=['Bánh Cáy', 'Bánh Rán', 'Bánh Đúc'])
prices = np.array([9, 3, 3])
butter_prices = pd.DataFrame(prices.reshape(1,3), index=['Giá'], columns=['Bánh Cáy', 'Bánh Rán', 'Bánh Đúc'])
total_prices = weekly_sales.dot(butter_prices.T)
weekly_sales["Thu về"] = total_prices
print(weekly_sales)