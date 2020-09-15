#3. 将第六课（while循环）练习1的猜数字小游戏中的数字用一个1-100之间的随机数来改写，并在猜中后输出猜了几轮猜中答案
import random
count =1
num = random.randint(1,101)
a = int(input('请猜一个数：\n'))
while a != num:
      if a > num:
            a= int(input('猜大辣！再猜一个叭：\n'))
            count +=1
      else:
            a= int(input('猜小辣！再猜一个叭：\n'))
            count +=1
print('Bingo 猜对辣！')
print('您一共猜了',count,'次！')
