# Matrix Addition

x = [ [2, -2], 
[5, 3]]
y = [ [3, 9], 
[7, 2]]
z = []

for index in range(len(x)):
    # print(x[index])
    # print(y[index])
    # print("index", index)
    a = []
    for index_2 in range(len(x[0])):
        # print(x[index][index_2])
        # # print("index_2", index_2)
        # print(y[index][index_2])
        a.append(x[index][index_2] + y[index][index_2])
        print(a)
    z.append(a)   
print(z)       
