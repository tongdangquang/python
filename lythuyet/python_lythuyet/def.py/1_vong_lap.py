# Vòng lặp while
'''Bài 1: Viết chương trình nhập vào số n từ bàn phím,
          n phải nằm trong khoảng từ 1 đến 99.'''
n = int(input("Nhập một số từ 1 đến 99: "))
while n < 1 or n > 99:
    n = int(input("Nhập lại n, n chỉ đươc nằm trong khoảng 1 đến 99: "))
print(f"Số bạn vừa nhập là: {n}")

''' Bài 2: Nhập vào họ tên học sinh, môn thi, điểm. In ra màn hình nếu điểm môn dự thi từ 7 trở lên thì đủ điều kiện. 
           Lặp lại với học sinh khác cho đến khi goc kí tự "N" để kết thúc.'''
while True:
    a = str(input("Nhập tên học sinh: "))
    b = str(input("Nhập môn thi: "))
    c = float(input("Nhập điểm: "))
    print(f"Học sinh {a} dự thi môn {b} có số điểm là {c}")
    if c >= 7:
        print(f"Học sinh {a} qua môn {b}")
    else:
        print(f"Học sinh {a} không qua môn {b}")
    c = input("Hãy nhấn n đển thoát hoặc nhất phím bất kì để tiếp tục")
    if c == "n" or c == "N":
        break
    else:
        continue 

# Bài kiểm tra số hoàn hảo.
'''Tìm tất cả các số hoàn thiện trong phạm vi từ 1 đến 1000'''
a = int(input("Nhập khoảng giới hạn: "))
for number in range(1, a, 1):
    s = 0
    for i in range(1, number, 1):
        if number % i == 0:
            s += i
    if s == number:
        print("Số là số hoàn hảo: ", s)
        
# Tính tổng s = 1! + 2! + 3! + ... + n!
n = int(input("Nhập n = "))
a = 1
b = 0
for i in range(1, n + 1, 1):
    a = a * i
    b = b + a
print(f"Tổng các giai thừa từ 1 đến {n} = {b}")

# Vẽ hình chữ N bằng vòng lặp for (vòng lặp lồng nhau)
n = int(input("Nhập chiều cao = "))
for y in range(n + 1):
    for x in range(n + 1):
        if x == 0 or x == n or x == y:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()

# viết chương trình in ra các số nguyên tố từ 1 đến n
number = int(input("nhập số: "))
count = 2
while count <= number:
    is_prime = True
    for i in range(2, int(count**(0.5)) + 1):
        if count % i == 0:
            is_prime = False
            break
    if is_prime:
        print(count)
    count += 1