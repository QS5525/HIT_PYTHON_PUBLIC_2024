def pascals(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

n = int(input("Nhập số nguyên dương N: "))
pascals_tamgiac = pascals(n)
print("Tam giác Pascal có", n, "hàng:")
for row in pascals_tamgiac:
    print(row)
