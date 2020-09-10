#高级猜数字
import requests

# 读取（新增）历史记录（增加容错）
try:
    with open('game_many_user.txt', 'r', encoding='utf-8') as f:
        txt = f.readlines()
except:
    txt = ''
#print(txt)

# 游戏前历史记录检查

#姓名录入
player_name = str(input('请输入姓名:'+'\n'))
new_player = []
data = []
names = []
new_data = []
sig_time = 0

#信息切片
for i in txt:#用户数据进行分割
    player_info = i.split()
    data.append(player_info)
for j in data:
    names.append(j[0])
#print(names)

#判断是否存在用户
if player_name in names:
    print('检测到您的游戏记录')
    for line in data:
        if line[0] == player_name:
            new_player = line
        else:
            new_data.insert(0,line)
else:
    print('未检测到您的游戏记录，已为您添加用户信息')
    new_data = data
    new_player = [player_name,0,0,0]

# 加载玩家数据：
round = int(new_player[1])
pre_average = float(new_player[2])
lest = int(new_player[3])
times = round * pre_average
#输出记录
print(' 玩家:%s ,游戏轮数:%d轮,平均猜测:%.2f次，最少猜测:%d次'%(
        new_player[0],round,pre_average,lest)
    )

#游戏部分
print('下面开始游戏辣!O(∩_∩)O')

#通过端口获得随机值
url = 'https://python666.cn/cls/number/guess/'
r = requests.get(url)
num = int(r.json())
#print(num)

#猜数游戏本体
print('请输入一个1-100的整数:')
while True:
    try:
        guess_number = int(input())
        if guess_number not in range(0,101):
            print('数字范围有误,请重新输入')
        elif guess_number > num:
            print('猜大了，请重猜')
            sig_time += 1
        elif guess_number < num:
            print('猜小了，请重猜')
            sig_time += 1
        else:
            print('猜对辣！真厉害')
            sig_time += 1
            break
    except ValueError:
        print('输入内容不符合要求哦')
        continue

#更新最小次数
if sig_time < lest:
    lest = sig_time
if lest == 0:
    lest = sig_time
print('您本局猜测共%s次' %sig_time)
print('您的最新记录')

#更新玩家数据
round += 1
times += sig_time
average = times/round
update_player = [new_player[0],str(round),str('%.2f'%average),str(lest)]
print(' 玩家:%s ,游戏轮数:%d轮,平均猜测:%.2f次，最少猜测:%d次'%(
        new_player[0],round,average,lest)
    )

# 输出（更新）记录
new_data.insert(0,update_player)
with open('game_many_user.txt', 'w', encoding='utf-8') as r:
    for i in new_data:
        for j in i:
            r.write(j+' ')
        r.write('\n')