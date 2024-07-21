def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

# Yêu cầu người dùng nhập số
number = int(input("Nhập một số nguyên dương: "))
print("Tổng các chữ số của số", number, "là:", sum_of_digits(number))
