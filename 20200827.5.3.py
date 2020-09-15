#3 输出九九乘法口诀表
for i in range(1, 10):
    for j in range (1,i+1):
        print('%d x %d = %d' % (i ,j, i*j))
