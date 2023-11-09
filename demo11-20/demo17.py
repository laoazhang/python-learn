money = 5000000
name = input(f"请输入您的名称：")


def my_main():
    """
    主菜单函数
    :return:
    """
    print("--------------------主菜单--------------------")
    print(f"{name}，您好，欢迎来到黑马银行ATM，请选择操作：")
    print(f"查询余额\t[输入1]")
    print(f"存款\t\t[输入2]")
    print(f"取款\t\t[输入3]")
    print(f"退出\t\t[输入4]")


def selectBalance():
    """
        查询余额函数
        :return:
        """
    print("--------------------查询余额--------------------")
    print(f"{name},您好，您的余额剩余：{money}元")


def addBalance():
    """
        存款金额函数
        :return:
        """
    num = int(input("请输入存款金额："))
    print("--------------------存款--------------------")
    global money
    money += num
    print(f"{name},您好，您存款{num}元成功")
    print(f"{name},您好，您的余额剩余：{money}元")


def updateBalance():
    """
        取款金额函数
        :return:
        """
    num = int(input("请输入取款金额："))
    print("--------------------取款--------------------")
    global money
    money -= num
    print(f"{name},您好，您存款{num}元成功")
    print(f"{name},您好，您的余额剩余：{money}元")


my_main()
while True:
    chonse = int(input(f"请输入您的选择："))
    if chonse == 1:
        selectBalance()
        continue
    elif chonse == 2:
        addBalance()
        continue
    elif chonse == 3:
        updateBalance()
        continue
    elif chonse == 4:
        print("程序已退出！")
        break
    else:
        print("输入错误，程序已退出！")
        break
