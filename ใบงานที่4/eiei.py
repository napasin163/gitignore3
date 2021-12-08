from collections import Counter

num = map(int, input().split())
a = dict(Counter(num))
print(f'1 = {a.get(1)}\n2 = {a.get(2)}\n3 = {a.get(3)}\n4 = {a.get(4)}\n5 = {a.get(5)}\n6 = {a.get(6)}\n7 = {a.get(7)}\n8 = {a.get(8)}\n9 = {a.get(9)}')
