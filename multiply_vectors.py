# Multiply Vectors

lst_1 = [2, 4, 5, 5, 9, 7] 
lst_2 = [2, 3, 6, 5, 4, 7]
# lst_4 = [4, 12, 30]
# lst_3 = [lst_1[0] * lst_2[0], lst_1[1] * lst_2[1], lst_1[2] * lst_2[2]         ]
lst_3 = []

for i in range(len(lst_1)):
    # print(i)
    lst_3.append(lst_1[i] * lst_2[i])
print(lst_3)
