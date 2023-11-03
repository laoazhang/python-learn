import random
num = random.randint(1, 100)
flag = True
count = 0
while flag:
    guess_num = int(input("请输入你猜测的数字："))
    count += 1
    if guess_num == num:
        print("猜中了")
        flag = False
    elif guess_num > num:
        print("猜大了")
    else:
        print("猜小了")
print(f"你总共猜测了{count}次")