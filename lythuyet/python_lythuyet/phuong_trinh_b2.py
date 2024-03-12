# giải phương trình bậc 2 
def pt(a, b, c):
    if a == 0:
        print("Phương trình vô nghiệm!")
    else:
        dt = (b**2 - 4*a*c)
        if dt > 0:
            x1 = (-b + dt**0.5)/(2*a)
            x2 = (-b - dt**0.5)/(2*a)
            print(f"Phương trình có nghiệm x1 = {x1}; x2 = {x2}")
        elif dt == 0:
            x = -b/2*a
            print(f"Phương trình có nghiệm duy nhất x = {x}")
        else:
            print("Phương trình vô nghiệm!")
while True:
    a = int(input("Nhập số a = "))
    b = int(input("Nhập số b = "))
    c = int(input("Nhập số c = "))
    pt(a, b, c)
    d = input("Nhấn phím bất kì để tiếp tục hoặc nhấn e để kết thức chương trình: ")
    if d == "e" or d == "E":
        break