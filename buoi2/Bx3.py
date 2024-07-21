def sum_1(n):
    total = 0
    for i in range(1, 2*n + 2):
        if i % 2 == 0:
            total -= i
        else:
            total += i
    return total

n = int(input("Nhập số nguyên dương n: "))
print("Tổng S(n) =", sum_1(n))

def sum_2(n):
    total = 0.0
    for i in range(1, n + 1):
        total += 1 / i
    return total

n = int(input("Nhập số nguyên dương n: "))
print("Tổng S(n) =", sum_2(n))

import cmath

def solve(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta > 0:
        x1 = (-b + cmath.sqrt(delta)) / (2*a)
        x2 = (-b - cmath.sqrt(delta)) / (2*a)
        return f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
    elif delta == 0:
        x = -b / (2*a)
        return f"Phương trình có nghiệm kép: x = {x}"
    else:
        x1 = (-b + cmath.sqrt(delta)) / (2*a)
        x2 = (-b - cmath.sqrt(delta)) / (2*a)
        return f"Phương trình có hai nghiệm phức: x1 = {x1}, x2 = {x2}"

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
print(solve(a, b, c))
