numbers = range(-5,5)

less_zero = filter(lambda x : x < 0, numbers)

for x in less_zero:
    print(x)

age = 10

flag = '成年' if age >= 18 else '未成年'
print(flag)