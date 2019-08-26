
list = range(2,100)

list_result = []
for i in list:
    num = 0
    for j in range(1,i+1):
        if i % j == 0:
            num = num +1
        else:
            pass

    if num == 2 :
        list_result.append(i)
        continue;

pass
print(list_result)