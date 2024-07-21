
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

print("a + b =", a + b)

print("a - b =", a - b)

print("a * b =", a * b)

print("a // b =", a // b)

print("a ** b =", a ** b)

print("a % b =", a % b)

if a > b:
    print("a lớn hơn b")
elif a < b:
    print("a nhỏ hơn b")
else:
    print("a bằng b")

print("a AND b =", a & b)

print("a OR b =", a | b)

print("a XOR b =", a ^ b)

print("NOT a == b =", not a == b)

print("a dịch phải 1 đơn vị =", a >> 1)

print("a dịch trái 1 đơn vị =", a << 1)
