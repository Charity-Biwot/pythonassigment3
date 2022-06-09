# keys = ["one", "two", "three"]
# values = [1, 2, 3, ]
#
# res_dict = dict(zip(keys, values))
# print(res_dict)

# x = ["three", "four", "five"]
# y = [3, 4, 5, ]
#
# num_dict = dict(zip(x, y))
# print(num_dict)

x = ["one", "two" "three"]
y = [1, 2, 3]

list_dict = dict()

for i in range(len(x)):
    list_dict.update({x[1]: y[i]})
    print(list_dict)