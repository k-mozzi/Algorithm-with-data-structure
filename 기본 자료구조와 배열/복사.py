import copy


x = [[1, 2, 3], [4, 5, 6]]
y = x.copy()  # 얕은 복사
x[0][1] = 9
print(x)
print(y)


a = [[1, 2, 3], [4, 5, 6]]
b = copy.deepcopy(a)  # 깊은 복사
a[0][1] = 9
print(a)
print(b)
