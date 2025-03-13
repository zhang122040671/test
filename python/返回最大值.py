def max(nums):
    maxNum=0
    for num in nums:
        if num>maxNum:
            maxNum=num
    return maxNum
maxNum=max([34,32,45,67,23,84,32,96,13,94,44])
print(f"最大值是{maxNum}")


numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
       numbers.remove(num)

print(numbers)  # 输出 [1, 3, 5]，4没删干净

def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))

count=0
def increment():
    count=0
    count=count+1 
    print(count)
increment()
print(count)


a = [1, 2]
b = [1, 2]
print(a == b)  # True
print(a is b)  # False

class Hero:
    def __init__(self, name, role, health, attack_power):
        self.name = name
        self.role = role
        self.health = health
        self.attack_power = attack_power
        self.experience = 0  # 初始经验为0
 
    def use_skill(self, skill_name):
        print(f"{self.name} 使用了 {skill_name} 技能。")
 
    def gain_experience(self, experience):
        self.experience += experience
        print(f"{self.name} 获得了 {experience} 经验。")
 
    def level_up(self):
        if self.experience >= 100:  # 假设升级需要100经验
            self.experience -= 100
            print(f"{self.name} 升级了！")
        else:
            print(f"{self.name} 经验不足，无法升级。")
 
    def __str__(self):
        return f"英雄名称: {self.name}, 角色: {self.role}, 生命值: {self.health}, 攻击力: {self.attack_power}, 经验: {self.experience}"
 
# 创建英雄实例
hero = Hero("孙悟空", "战士", 500, 100)
 
# 使用技能
hero.use_skill("七十二变")
 
# 获得经验并尝试升级
hero.gain_experience(50)
hero.level_up()
hero.gain_experience(60)
hero.level_up()
 
# 打印英雄信息
print(hero)

