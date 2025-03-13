import random
iswin=False
while iswin==False:
    num=random.randint(1,3)
    if num==1:
        finger="石头"
    elif num==2:
        finger="剪刀"
    elif num==3:
        finger="布"
    text=input("输入 石头、剪刀、布：")
    blist=["石头","剪刀","布"]
    if (text not in blist):
        print("输入错误，请重新输入！")
    elif text==finger:
        print("计算机出了:%s,平局！"%finger)
    elif (text=="剪刀" and finger=="布") or (text=="石头"and finger=="剪刀")or(text=="布"and finger=="石头"):
        print("计算机出了:%s，你赢了"%finger)
        
    else:
        print("计算机出了：%s，你输了"%finger)
        iswin=True

