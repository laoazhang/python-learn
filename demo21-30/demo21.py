str_demo = "itheima itcast boxuegu"
print(f"字符串{str_demo}中有：{str_demo.count('it')}个it字符")
print(f"字符串{str_demo}，被替换空格后，结果：{str_demo.replace(' ', '|')}")
print(f"字符串{str_demo.replace(' ', '|')}，按照|分割后，得到：{str_demo.replace(' ', '|').split('|')}")
