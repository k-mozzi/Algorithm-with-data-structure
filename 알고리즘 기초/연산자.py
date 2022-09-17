n = int(input('몇 개를 출력할까요?: '))

result = []
for i in range(n):
    if i % 2:
        result.append('-')
    else:
        result.append('+')

a = ''.join(result)

print(a)
