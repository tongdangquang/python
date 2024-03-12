# class MyNumbers:
#   def __iter__(self): # hàm lặp class
#     self.a = 1
#     return self 

#   def __next__(self): # hàm trả về và thuộc tính và tăng giá trị của thuộc tính
#     if self.a <= 5: # điều kiện để dừng vòng lặp
#         x = self.a
#         self.a += 1 # tăng thuộc tính
#         return x

# myclass = MyNumbers() # khởi tạo đối tượng
# myiter = iter(myclass) # in ra lần lượt các giá trị của thuộc tính
# myiter = iter(myclass)
# myiter = iter(myclass)
# myiter = iter(myclass)
# myiter = iter(myclass)
# myiter = iter(myclass)
# myiter = iter(myclass)


class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            result = self.current
            self.current += 1
            return result
        raise StopIteration

# Sử dụng trình lặp
my_iterator = MyIterator(1, 5)
for num in my_iterator:
    print(num)



# Trình lặp hỗ trợ khá nhiều kiểu cấu trúc dữ liệu như danh sách (list), bộ (tuple), chuỗi (string), tập hợp(set)
# Trình lặp dễ sử dụng và kết hợp với lệnh for...in...: trở nên dễ đọc hơn và giảm sự phức tạp khi duyệt qua các phần tử của tập hợp
class duyetchuoi:
    def __init__(self, chuoi) -> None:
        self.chuoi = chuoi
        self.index = 0

    # sử dụng phương thức __iter__, phương thức này có kiểu trả về là chính đối tượng của trình lặp (self)
    def __iter__(self):
        return self

    # sử dụng phương thức __next__
    # phương thức này trả về phần tử tiếp theo trong chuỗi. Nếu chuỗi không có phần tử nào nữa, nó sẽ ném một ngoại lệ "StopIteration" để báo hiệu rằng quá trình lặp kết thúc
    def __next__(self):
        if(self.index < len(self.chuoi)):
            result = self.chuoi[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

m = [1, 2, 3, 4, 5]
name = "Hello world"
my_iter = iter(m)

# sử dụng trình lặp
chuoi = duyetchuoi(name)
for char in chuoi:
    print(char, end = " ")

# lấy từng phần tử 1 của 1 list thông qua trình lặp
print(next(my_iter))
print(next(my_iter))