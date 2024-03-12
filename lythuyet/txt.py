# tình huống: có một bài tập nhập vào danh sách sinh viên:
dssv = []
# nhập danh sách từ bàn phím
while True:
    masv = input("Nhập mã sinh viên: ")
    if masv == '':
        break
    tensv = input("Họ tên sinh viên: ")
    lop = input("lớp: ")
    que = input('Quên quán: ')
    dssv.append([masv, tensv, lop, que])
print('Danh sách sinh viên vừa nhập: ')
print("\t".join(['Mã SV', 'Họ tên', 'Lớp', 'Quê quán']))
for i in dssv:
    print("\t".join(i))

