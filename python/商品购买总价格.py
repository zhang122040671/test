# 定义商品价格字典
prices = {
    "苹果": 2.5,
    "香蕉": 1.5,
    "橙子": 3.0,
    "葡萄": 4.0
}
 
# 初始化总价格为0
total_price = 0
 
# 询问用户想要购买的商品及其数量
while True:
    item = input("请输入你想要购买的商品名称（输入'结束'以结束购买）: ").strip()
    if item.lower() == '结束':
        break
    if item in prices:
        quantity = int(input(f"请输入你想要购买的{item}数量: "))
        total_price += prices[item] * quantity
        print(f"已添加{quantity}个{item}到购物车。")
    else:
        print("抱歉，没有找到该商品，请检查后重试。")
 
# 输出总价格
print(f"你的购物车总价格为：{total_price:.2f}元")


