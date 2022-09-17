n = int(input('몇 개 출력하시겠습니까?: '))
m = int(input('몇 개마다 줄바꿈 하시겠습니까?: '))

for _ in range(n // m):
    print('*' * m)

rest = n % m
if rest:
    print('*' * rest)
