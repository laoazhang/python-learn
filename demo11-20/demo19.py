num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

index = 0
num_new_list = []
while index < len(num_list):
    if num_list[index] % 2 == 0:
        num_new_list.append(num_list[index])
    index += 1
print(f"通过while循环，从列表：{num_list}中取出偶数，组成新列表：{num_new_list}")

num_new2_list = []
for num in num_list:
    if num % 2 == 0:
        num_new2_list.append(num)
print(f"通过for循环，从列表：{num_list}中取出偶数，组成新列表：{num_new2_list}")
