# a = int(input("Nhap a = "))
# chương trình kiểm tra xem 1 số có phải số hoàn thiện không
# b = 0
# for i in range (1, a):
#     if (a % i == 0):
#         b += i

# if (b == a):
#     print(f"{a} là số hoàn hảo!")
# else:
#     print(f"{a} không là số hoàn hảo!")


# chương trình liệt kê tất cả các số hoàn hảo trong một khoảng nhất định
a = int(input("Nhap a = "))
print (f"Những số hoàn hảo từ 1 đến {a}:", end = " ")
for i in range(1, a + 1):
    b = 0
    for j in range (1, i):
        if (i % j == 0):
            b += j
    
    if (b == i):
        print(i, end = " ")