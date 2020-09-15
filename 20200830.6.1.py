#1. 第四课里，我们用 if 改进猜数字小游戏后，功能已经基本实现了。但是有没有办法能让玩家一直猜，直到猜中为止？试着用 while 循环完成这个任务
import random
num = random.randint(1,101)
a = int(input('请猜一个数：\n'))
while a != num:
      if a > num:
            a= int(input('猜大辣！在猜一个叭：\n'))
      else:
            a= int(input('猜小辣！在猜一个叭：\n'))
print('Bingo 猜对辣！')
