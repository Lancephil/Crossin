#2.统计下这段文字里，不同单词出现的次数
word = 'Beautiful is better than ugly Explicit is better than implicit Simple is better than complex Complex is better than complicated Flat is better than nested Sparse is better than dense'
lst= word.split()
dic= {}
for k in lst:
      if k in dic:
            dic[k]+=1
      else:
            dic[k]=1
print(dic)


