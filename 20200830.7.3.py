#3. 分割与连接字符串
word = 'I am Mr Crossin of Python'

# 将字符串 word 按照空格分割成一个列表
lst = word.split()
print(lst)

# 再将分割后的列表以逗号(,)重新拼接成字符串
word = ','.join(lst)
print(word)
