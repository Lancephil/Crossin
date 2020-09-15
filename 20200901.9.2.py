#2. 生成10个随机数，输出里面最大的数
import random
lst = []
for i in range(1,11):
      num= random.randint(0,1000)
      lst.append(num)
print(lst)
print('max is:', max(lst))



