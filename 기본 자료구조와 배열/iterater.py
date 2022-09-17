it = iter(range(3))
print(next(it))
print(next(it))
print(next(it))
# iter() 는 그 객체에 대한 이터레이터(반복자)를 반환한다.
# next() 함수에 이터레이터를 전달하면 원소를 순차적으로 꺼낸다.
# 꺼낼 원소가 더 이상 없을 땐 StopIteration 으로 예외를 발생시킨다.
