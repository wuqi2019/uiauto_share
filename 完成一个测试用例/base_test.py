# 斐波那契数列(后一位=前两位之和)
# 又叫黄金分割数列，前/后 越来越接近0.618
# list1 = []
# for i in range(20):
#     if i <= 1:
#         list1.append(1)
#     else:
#         list1.append(list1[-2]+list1[-1])
# print(list1)


import random
dict1 = {'A': [], 'B': [], 'C': [], 'D': []}
for i in range(20):
    re = random.randint(1, 100)
    if re >= 90:
        dict1['A'].append(re)
    elif re >= 80:
        dict1['B'].append(re)
print(dict1)