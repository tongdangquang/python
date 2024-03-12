import time
a = time.time() # trả về số giây, tính từ 0:0:00 ngày 01/01/1970 theo giờ utc, gọi là epoch (thời điểm bắt đầu)
b = time.ctime() # chuyển số giây tính từ epoch (0h00 ngày 01/01/1970) sang thành chuỗi ngày tháng năm ứng với số giây đó
c = time.sleep(5) # delay chương trình thực thi theo số giây, ví dụ như cho 5s, hết 5s đóng chương trình
d = time.localtime() # trả về ngày tháng năm của hiện tại theo giờ địa phương

d.tm_year # trả về năm
d.tm_mon # trả về tháng
d.tm_mday # trả về ngày
d.tm_hour # trả về giờ
d.tm_min # trả về phút
d.tm_sec # trả về giây
time_string = time.strftime("%d/%m/%y, %H:%M:%S", d) # hàm trả về ngày tháng năm theo dạng chuỗi string

'''Bài tập: Nhập tên và tuổi của mình để chương trình in ra năm mình tròn 100 tuổi.'''
a = input("Họ và tên: ")
b = int(input("Tuổi: "))
c = time.localtime()
d = c.tm_year + (100 - b)
print(f"Năm {d}, {a} sẽ tròn 100 tuổi")