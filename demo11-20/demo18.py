mylist = [21, 25, 21, 23, 22, 20]
mylist.append(31)
mylist.extend([29, 33, 20])
num1 = mylist[0]
print(f"从列表中取出第一个元素，应该是21，实际上是", {num1})
num2 = mylist[-1]
print(f"从列表中取出第一个元素，应该是30，实际上是", {num2})
index = mylist.index(31)
print(f"元素31在列表的下标位置:{index}")
print(f"最后列表的内容为:{mylist}")
