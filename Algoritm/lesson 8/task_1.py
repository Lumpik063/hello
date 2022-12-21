from collections import Counter, deque


class Node:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def haffman_tree(my_string):
    count_s = Counter(my_string)
    sorted_s = deque(sorted(count_s.items(), key=lambda item: item[1]))
    while len(sorted_s) > 1:
        weight = sorted_s[0][1] + sorted_s[1][1]
        node = Node(left=sorted_s.popleft()[0], right=sorted_s.popleft()[0])
        for i, item in enumerate(sorted_s):
            if weight > item[1]:
                continue
            else:
                sorted_s.insert(i, (node, weight))
                break
        else:
            sorted_s.append((node, weight))
    return sorted_s[0][0]


def haffman_code(tree, path=''):
    if not isinstance(tree, Node):
        code_table[tree] = path
    else:
        haffman_code(tree.left, path=f'{path}0')
        haffman_code(tree.right, path=f'{path}1')


code_table = dict()

user_string = input('Для кодировки введите данные: ')
haffman_code(haffman_tree(user_string))

for i in user_string:
    print(code_table[i], end=' ')