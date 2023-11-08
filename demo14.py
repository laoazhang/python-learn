import random

i = 1
wages = 10000
for i in range(1, 21):
    fraction = random.randint(1, 10)
    if fraction < 5:
        print(f"员工{i},绩效分{fraction},不发工资，下一位。")
        continue
    else:
        wages -= 1000
        print(f"向员工{i}发工资1000元，账户余额还剩余{wages}元")
        if wages == 0:
            print(f"工资发完了，下个月领取吧。")
            break
