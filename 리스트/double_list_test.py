from enum import Enum
from double_list import DoubleLinkedList

Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '주목노드바로뒤삽입',
                     '머리노드삭제', '꼬리노드삭제', '주목노드출력',
                     '주목노드이동', '주목노드역순이동', '주목노드삭제',
                     '모든노드삭제', '검색', '멤버십판단', '모든노드출력',
                     '모든노드역순출력', '모든노드스캔', '모든노드역순스캔', '종료'])


def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)


lst = DoubleLinkedList()

while True:
    menu = select_menu()

    if menu == Menu.머리에노드삽입:
        lst.add_first(int(input('머리 노드에 넣을 값을 입력하세요.: ')))

    elif menu == Menu.꼬리에노드삽입:
        lst.add_last(int(input('꼬리 노드에 넣을 값을 입력하세요.: ')))

    elif menu == Menu.주목노드바로뒤삽입:
        lst.add(int(input('주목 노드 바로 뒤에 넣을 값을 입력하세요.: ')))

    elif menu == Menu.머리노드삭제:
        lst.remove_first()

    elif menu == Menu.꼬리노드삭제:
        lst.remove_last()

    elif menu == Menu.주목노드출력:
        lst.print_current_node()

    elif menu == Menu.주목노드이동:
        lst.next()

    elif menu == Menu.주목노드역순이동:
        lst.prev()

    elif menu == Menu.주목노드삭제:
        lst.remove_current_node()

    elif menu == Menu.모든노드삭제:
        lst.clear()

    elif menu == Menu.검색:
        pos = lst.search(int(input('검색할 값을 입력하세요.: ')))
        if pos >= 0:
            print(f'이 키를 갖는 데이터는 {pos + 1}번째에 있습니다.')
        else:
            print('해당 데이터가 없습니다.')

    elif menu == Menu.멤버십판단:
        print('그 값의 데잉터는 포함되어'
              + (' 있습니다.' if int(input('판단할 값을 입력하세요.: ')) in lst
                 else '있지 않습니다.'))

    elif menu == Menu.모든노드출력:
        lst.print()

    elif menu == Menu.모든노드역순출력:
        lst.print_reverse()

    elif menu == Menu.모든노드스캔:
        for e in lst:
            print(e)

    elif menu == Menu.모든노드역순스캔:
        for e in reversed(lst):
            print(e)

    else:
        break
