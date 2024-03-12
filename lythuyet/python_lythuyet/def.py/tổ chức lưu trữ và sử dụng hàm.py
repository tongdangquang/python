# Cách thứ 1:
# Bước 1: Tạo 1 tệp Tong.py để lưu trũ hàm (hay còn gọi là module)
def tong_ds(ds):
    sum = 0
    for i in ds:
        sum += i
    return sum
# Bước 2: Tạo 1 tệp khác để sử dụng hàm (chương trình chính)
'''import Tong 
ds_le = [1, 3, 5, 7, 9]
ds_chan = [2, 4, 6, 8, 10]
sum1 = Tong.tong_ds(ds_le)
sum2 = Tong.tong_ds(ds_chan)
print("Tổng của danh sách lẻ = ", sum1)
print("Tổng của danh sách chẵn = ", sum2)'''
# Cách thứ 2:
# Bước 1: Tạo các hàm và lưu trong một tệp riêng biệt ví dụ như tệp Tong.py dưới đây(tệp này còn gọi là module)
def tong_ds(ds):
    sum = 0
    for i in ds:
        sum += i
    return sum
# Bước 2: Tạo ra tệp khác để sử dụng hàm (chương trình chính)
'''+ Sử dụng các module đó vào tệp khác(chương tình chính) bằng lệnh:
    Dạng 1: from tên_module import tên_hàm
    Dạng 2: from tên_module import tên_hàm_1, tên_hàm_2, tên_hàm_3,...
    Dạng 3: from tên_module import * (nghĩa là import tất cả các hàm vào chương trình)
   + Sử dụng hàm theo cú pháp: tên_hàm'''
'''from Tong import *
ds_le = [1, 3, 5, 7, 9]
ds_chan = [2, 4, 6, 8, 10]
sum1 = tong_ds(ds_le)
sum2 = tong_ds(ds_chan)
print("Tổng của danh sách lẻ = ", sum1)
print("Tổng của danh sách chẵn = ", sum2)'''

# cách thứ 3: Sử dụng bí danh
# Bước 1: Tạo các hàm và lưu trong một tệp riêng biệt (tệp này gọi là module)
def tong_ds(ds):
    sum = 0
    for i in ds:
        sum += 0
    return sum
# Bước 2: Sử dụng các module đó vào chương trình chính bằng lệnh import có sử dụng bí danh
#         from tên_module import tên_hàm as tên_bí_danh
'''from Tong import tong_ds as hàm_tổng
ds_le = [1, 3, 5, 7, 9]
ds_chan = [2, 4, 6, 8, 10]
sum1 = hàm_tổng(ds_le)
sum2 = hàm_tổng(ds_chan)
# Bước 3: Sử dụng hàm, gọi hàm theo cú pháp tên_bí_danh
print("Tổng của danh sách lẻ = ", sum1)
print("Tổng của danh sách chẵn = ", sum2)'''