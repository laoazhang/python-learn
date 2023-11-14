my_str = "万过薪月，员序程马黑来，nohtyP学"

result1 = my_str[::-1][9:14]
print(result1)

result2 = my_str[5:10][::-1]
print(result2)

result3 = my_str.split("，")[1].replace("来","")[::-1]
print(result3)