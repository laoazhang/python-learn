print("欢迎来到黑马动物园。")
height = int(input("请输入你的身高(cm)："))
vip_level = int(input("请输入你的vip等级(1-5)"))
if height < 120:
    print("您的身高未超出120cm，可以免费游玩。")
elif vip_level>3:
    print("vip级别大于3，可以免费。")
else:
    print("条件都不满足，需要买票。")
print("祝您游玩愉快。")
