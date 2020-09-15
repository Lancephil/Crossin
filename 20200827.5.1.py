#1 计算100以内所有3的倍数的和（即：计算3、6、9 ... 96、99 的和）
global sum
sum=0
for i in range(1,101):
      if i % 3 == 0:
         sum += i  #注意缩进
print (sum)
