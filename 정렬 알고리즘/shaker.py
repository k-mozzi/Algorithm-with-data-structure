from typing import MutableSequence


def shaker_sort(a: MutableSequence) -> None:
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        for j in range(right, left, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last
        # 나열된 원소를 맨 뒤에서 맨 앞으로 스캔

        for j in range(left, right):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last
        # 나열된 원소를 맨 앞에서 맨 뒤로 스캔
        # ...생략...
