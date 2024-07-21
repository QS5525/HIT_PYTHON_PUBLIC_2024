def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Tam giác đều"
        elif a == b or b == c or a == c:
            return "Tam giác cân"
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Tam giác vuông"
        elif a**2 + b**2 > c**2 and a**2 + c**2 > b**2 and b**2 + c**2 > a**2:
            return "Tam giác nhọn"
        else:
            return "Tam giác tù"
    else:
        return "Không phải là tam giác"

# Yêu cầu người dùng nhập 3 số
a = int(input("Nhập cạnh thứ nhất: "))
b = int(input("Nhập cạnh thứ hai: "))
c = int(input("Nhập cạnh thứ ba: "))
print("Kết quả:", check_triangle(a, b, c))
