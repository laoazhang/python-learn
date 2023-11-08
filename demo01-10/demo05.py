import random

num = random.randint(1, 10)
if int(input("请第一次输入数字：")) > num:
    print("猜大了。")
else:
    print("猜小了。")
    if int(input("请再次输入数字：")) > num:
        print("猜大了。")
    else:
        print("猜小了。")
        if int(input("最后一次输入数字：")) > num:
            print("猜大了。")
        else:
            print("猜小了。")