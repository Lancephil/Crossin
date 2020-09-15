#3. 使用 while 计算100以内所有3的倍数的和（即：计算3、6、9 ... 96、99 的和）
count = 0
sum3 = 0
while count <101:
      count += 1
      if count % 3 == 0:
            sum3 += count
print(sum3)
