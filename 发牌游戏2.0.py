from random import *
a=['♥','♠','♦','♣']
b=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
c=['大王','小王']
score1,score2,score3,h1,h2,h3=0,0,0,0,0,0
z1,z2,z3=[],[],[]       
z=list(range(1,11))*4+[0.5]*14      

for i in a:             #创建扑克牌
    for j in b:
        c.append(i+j)
        
def value(score,Z):  #随机选牌、计算牌的分数、将其从牌库中删除、返回牌分数以及目前牌的情况
    global c,z1,z2,z3,score1,score2,score3,z
    str_num= [str(i) for i in range(2, 10)]
    f=choice(c)
    c=list(set(c)-set(f))
    Z.append(f)
    if f[-1] in str_num:
        e=eval(f[-1])
    elif f[-1] == 'A':
        e=1
    elif f[-1] == '0':
        e=10
    elif f[-1] in ['J','Q','K','王']:
        e=0.5
    z.remove(e)
    if Z == z1:score+=e
    elif Z==z2:score+=e
    elif Z==z3:score+=e
    return score,Z

def pick(score):     #计算当前分数下可能自爆的事件总数
    global z
    sum=[]
    for i in range(len(z)):
        if z[i]>11-score:
            sum+=[z[i]]
    return len(sum)

def First(st):    #进行初始抓牌
    global f1,f2,f3,score1,score2,score3,p1,p2,p3
    f1=value(score1,z1)
    f2=value(score2,z2)
    f3=value(score3,z3)
    score1,score2,score3=f1[0],f2[0],f3[0]
    p1=pick(score1)/len(z)
    p2=pick(score2)/len(z)
    p3=pick(score3)/len(z)
    if st=='PVE':
        print('初始抓牌： player{}\n\t  robot1{}\n\t  robot2{}'.format(f1,f2,f3))
    if st=='PVP':
        print('初始抓牌： player {}\n\t  player2{}\n\t  player3{}'.format(f1,f2,f3))
def player():   #玩家1
    global score1,z1,h1,f1,p1
    x=input('player\n请选择是否抽牌（Y/N）：')
    if x=='Y':
        f1=value(score1,z1)
        score1=f1[0]
        p1=pick(score1)/len(z)
        print("抽牌结果是：",f1)
        if score1>11:
            h1=1
            p1=1
            print('你已经自爆')
    elif x=="N":
        h1=1
        p1=1
        print('player放弃抽牌')
def player2():  #玩家2
    global score2,f2,h2
    x=input('player2\n请选择是否抽牌（Y/N）：')
    if x=='Y':
        f2=value(score2,z2)
        score2=f2[0]
        print("抽牌结果是：",f2)
        if score2>11:
            h2=1
            print('你已经自爆') 
    elif x=='N':
        h2=1
        print('player2放弃抽牌')    
def player3():  #玩家3
    global score3,f3,h3
    x=input('player3\n请选择是否抽牌（Y/N）：')
    if x=='Y':
        f3=value(score3,z3)
        score3=f3[0]
        print("抽牌结果是：",f3)
        if score3>11:
            h3=1
            print('你已经自爆')
    elif x=='N':
        h3=1
        print('player3放弃抽牌') 
    
def robot1():   #机器人1
    global score2,z,z2,h2,f2,p1,p2,p3
    p2=pick(score2)/len(z)
    if p2<0.5 or p2<p1 and p2<p3 :
        f2=value(score2,z2)
        score2=f2[0]
        print("robot1\n轮到机器人1抽牌,抽牌结果是：",f2)
        if score2>11:
            h2=1
            p2=1
            print("机器人1已经自爆")
    else:
        h2=1
        p2=1
        print("机器人1放弃抓牌")
        
def robot2():   #机器人2
    global score3,z,z3,h3,f3,p1,p2,p3
    p3=pick(score3)/len(z)
    if  p3<0.5 or p3<p1 and p3<p2:
        f3=value(score3,z3)
        score3=f3[0]
        print("robot2\n轮到机器人2抽牌,抽牌结果是：",f3)
        if score3>11:
            h3=1
            p3=1
            print("机器人2已经自爆")
    else:
        h3=1
        p3=1
        print("机器人2放弃抓牌")   

def calculate(score1,score2,score3):    #将玩家的分数进行核算,大于11清零，小于11保留
    max=0
    a=[score1,score2,score3]
    for i in range(3):
        if a[i]>11:
            a[i]=0
    return a

st=input('请选择模式（PVP/PVE）：')
if st=='PVE':
    First(st)
    while(h1+h2+h3<3):
        if h1==0 : player()
        if h2==0 : robot1()
        if h3==0 : robot2()
        print('发牌情况：player{}\n\t robot1{}\n\t robot2{}'.format(f1,f2,f3))
    g={score1:'player',score2:'robot1',score3:'robot2'}
    y=calculate(score1,score2,score3)
    print("Game Over")
    print("抽牌情况\nplayer {}\nrobot1 {}\nrobot2 {}".format(z1,z2,z3))
    print("总得分\nplayer：{}分\trobot1：{}分\t robot2：{}分\n".format(y[0],y[1],y[2]))
if st=='PVP':
    First(st)
    while(h1+h2+h3<3):
        if h1==0 : player()
        if h2==0 : player2()
        if h3==0 : player3()
        print('发牌情况：player {}\n\t player2{}\n\t player3{}'.format(f1,f2,f3))
    g={score1:'player',score2:'player2',score3:'robot2'}
    y=calculate(score1,score2,score3)
    print("Game Over")
    print("抽牌情况\nplayer  {}\nplayer2 {}\nplayer3 {}".format(z1,z2,z3))
    print("总得分\nplayer：{}分\tplayer2：{}分\t player3：{}分\n".format(y[0],y[1],y[2]))

    









        
        
        
