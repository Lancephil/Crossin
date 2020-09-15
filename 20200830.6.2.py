# 输出 1 到 10，但不输出 4 和 5
count = 0
while count <11:
    count += 1
    if count ==4 or count == 5:
        continue
    print(count)
