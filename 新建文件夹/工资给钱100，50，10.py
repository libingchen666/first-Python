for i in range(10):
    x=int(input('请输入您的月工资:'))
    if x<100:
        print('您的工资不符合实际')
    else:
        a=x//100
        y=x-100*a
        if y>50:
            b=1
            z=y-50
            c=z//10
            d=z-10*c
        elif y<50:
            b=0
            z=y
            c=z//10
            d=z-10*c
    print('需给您100元：',a,'张')
    print('需给您50元：',b,'张')
    print('需给您10元：',c,'张')
    print('需给您1元：',d,'张')
    print('共需给您钞票：',a+b+c+d,'张')
