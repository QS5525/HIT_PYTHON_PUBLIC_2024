def bit_length(a):
    return a.bit_length()

a = int(input("Nhập số nguyên a: "))
print("Số lượng các bits cần thiết để biểu diễn số", a, "ở dạng nhị phân là:", bit_length(a))



x = "awesome"

print("Python is", x)

print(f"Python is {x}")

print("Python is {}".format(x))



import sys

print("Phiên bản Python hiện tại là:", sys.version)

