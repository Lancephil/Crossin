# BMI(Body Mass Index)计算器

Hei = float(input('请输入身高：'))
Wei = float(input('请输入体重：'))

BMI =  Wei/(Hei*Hei)

if BMI < 18.5:
      print('您的BMI指数为：'"%.2f"% BMI,'，您的体重偏轻。')
elif 18.5 <= BMI < 24:
            print('您的BMI指数为：'"%.2f"%BMI,'，您的体重正常。')
elif BMI > 24:
      print('您的BMI指数为：'"%.2f"%BMI,'，您的体重偏重。')      
else:
      print('请输入真实的值。')  
