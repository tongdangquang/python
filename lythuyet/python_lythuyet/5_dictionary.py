# cú pháp: dict = {"key 1":"value 1", "key 2":"value 2",...}

dic1 = {"name":"tống đăng quang", "trường": "HaUI", "tuổi": 19, "chiều cao": 1.70}
dic2 = {"tống đăng quang":{"họ":"tống", "tên":"quang", "học tại":"đại học công nghiệp hà nội"}} # dict chồng dict
print(dic1['name']) # xuất value theo key
print(dic2['tống đăng quang']) # access value theo key
dic1["chiều cao"] = 1.75 # gọi key ra và thay đổi value
dic1['cân nặng']  = 50 # thêm phần tử cho dict (thêm vào cuối dict)
del dic1['cân nặng'] # xóa dict và chương trình sẽ báo lỗi
del dic1 # xóa tất cả dict
len(dic1) # số phần tử của dict
dic3 = dic1.copy() # sao chép dict
dic3 = dict(dic1) # cũng có thể sao chép như thế này
dic3.clear() # xóa tất cả phần tử và trả về dict rỗng (clear khác với del)

dict.fromkeys() # tạo dict, sử dụng phần tử trong list là key và có giá trị khởi tạo tương ứng
# vi dụ minh họa cho dict.fromkeys()
keys = {'u', 'e', 'o', 'a', 'i'}
value = 'nguyên âm'
dic4 = dict.fromkeys(keys, value)
print(dic4)

dic3.get() # trả về giá trị tương ứng với key, nếu không có giá trị đó, trả về sẽ là mặc định
# ví dụ minh họa cho dict.get()
print("Name: ", dic1.get('name')) # trường hợp không cung cấp value
print("Name: ", dic1.get('nam', 'quang')) # trường hợp có cấp value, khi mà không tông tại key "nam"

dic3.items() # trả về các phần tử dưới dạng list
dic3.keys() # gọi tất cả các keys và trả về dưới dạng list
dic3.values() # trả về tất cả các value dưới dạng list
print('name' in dic3) # nếu key có trong dict thì trả về True, và không có thì trả về False
dic3.pop('name') # xuất ra value của key đồng thời xóa value đó khỏi dict
dic3.popitem() # xuất ra phần tử cuối cùng của dict, đông thời xóa khỏi dict
dic3.update(dic2) # update dict nọ vào dict kia
dic3.update({'year': 2023}) # thêm một cặp dict
dic3.setdefault("nam", 'tống quang') # tương tự hàm get(), giống cả 2 trường hợp luôn
# xuất dict thành một string, ở đây x là tất cả keys còn y là tất cả values
dic = {'hello': 'world', 'tống': 'quang', 'thpt': 'quỳnh côi'}
for x, y in dic.items():
	print(x, y, end = ' ')

'''BÀi 1: Viết chương trình sử dụng dict chứa 10 user nảm và password.
    CHương trình yêu cầu nhập user name và password.
    1. Nếu user name không có trong dict, chương trình báo user name không tồn tại.
    2. Nếu user name đúng mà password sai thì báo password sai.
    3. Nếu user name và password đều đúng thì báo bạn đã login thành công.'''

dic = {'user1': '123456',
'user2': '1123456',
'user3': '123456', 
'user4': '123456', 
'user5': '123456', 
'user6': '123456', 
'user7': '123456', 
'user8': '123456', 
'user9': '123456', 
'user10': '123456'}
user = input("Nhập user: ")
pw = input("Nhập pass: ")
if user not in dic.keys():
    print("User không tồn tại!")
else:
    if pw == dic[user]:
        print("Đăng nhập thành công!")
    else:
        print("Sai pass!")

# Bài 2: Tìm dữ liệu trong dict
mybooks=[
{"Title": "Android App Development", "Author": "Thanh Tran", "Publisher": "VNU", "Price": "25000","Published_Year": "2017"},
{"Title": "Python", "Author": "Thanh Tran", "Publisher": "VNU", "Price": "23000", "Published_Year": "2019"},
{"Title": "JavaScript", "Author": "Pham Dieu", "Publisher": "SSS", "Price": "38000","Published_Year": "2018"},
{"Title": "HTML5", "Author": "Man Nhi", "Publisher": "HCM", "Price": "33000", "Published_Year": "2012"},
{"Title": "Compiler", "Author": "Thanh Tran", "Publisher": "VNU", "Price": "24000","Published_Year": "2011"},
{"Title": "C language", "Author": "Man Nhi", "Publisher": "SSS", "Price": "29000","Published_Year": "2010"},
{"Title": "Programming Linguistics", "Author": "Pham Dieu", "Publisher": "HCM","Price": "41000", "Published_Year": "2009"},
{"Title": "C# language", "Author": "Thanh Tran", "Publisher": "VNU", "Price": "42000","Published_Year": "2013"},
{"Title": "App Inventor", "Author": "Man Nhi", "Publisher": "LD", "Price": "30000","Published_Year": "2015"},
]
check = False
while check == False:
    chon = input("""Chọn để tìm kiếm: 
    1. Title
    2. Athor
    3. Publisher
    4. Price
    select(1, 2, 3, 4): """)
    if chon == '1':
        kwd = 'Title'
        break
    elif chon == '2':
        kwd = 'Author'
        break
    elif chon == '3':
        kwd = 'Publisher'
        break
    elif chon == '4':
        kwd = 'Price'
        break
    else:
        print("Invail input")
        check = False
kw = input("nhập key word vào để tìm kiếm: ")
for dong in mybooks:
    if kw == (dong[kwd]):
        print("Title = ", dong['Title'])
        print("Author = ", dong['Author'])
        print("Publisher = ", dong['Publisher'])
        print("Price = ", dong['Price'])