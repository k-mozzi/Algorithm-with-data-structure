name = input('이름을 입력하세요.: ')
print(f'안녕하세요? {name}님.')

if a > b:
    min2 = a
    max2 = b


if a < b: min2 = a
if a < b: min2 = a; max2 = b
if a < b: min2 = a; max2 = b;


n = int(input('정수를 입력하세요: '))

if n == 1:
    print('A')
elif n == 2:
    print('B')
elif n == 3:
    print('C')


# a if b else c를 평가한 값이 참이면 a를, 거짓이면 c를 반환한다.

a = x if x > y else y
# x와 y 중 큰 값을 a에 대입
print('c는 0입니다.' if c == 0 else 'c는 0이 아닙니다.')