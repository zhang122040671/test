score=int(input("请输入你的分数查看你的段位："))
if score<10:
    print("加油哟，你还在青铜段位!")
elif score<50:
    print("恭喜你升级到了白银段位!")
elif score<80:
    print("恭喜你升级到了黄金段位!")
else:
    print("真棒，你已经是王者了!")
