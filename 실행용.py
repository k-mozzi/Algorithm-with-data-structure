min = int(input('최솟값을 입력하세요.: '))
max = int(input('최댓값을 입력하세요.: '))
true_lst = []
false_lst = []

while True:
    while -999 not in false_lst:
        temp = int(input('온도를 입력하세요.: '))
        if min < temp < max:
            true_lst.append(temp)
        else:
            false_lst.append(temp)
    false_lst.remove(-999)
    print('true_lst:', true_lst)
    print('false_lst:', false_lst)
    if len(false_lst) >= 1:
        print('bad')
        break
    else:
        print('good')
        break
