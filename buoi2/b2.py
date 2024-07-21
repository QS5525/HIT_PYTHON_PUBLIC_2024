def sum_of_divisors(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total

n = int(input("Nhập một số nguyên dương: "))
print("Tổng các ước số của", n, "là:", sum_of_divisors(n))
