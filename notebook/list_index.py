l = list('abcde')
print(l)
# ['a', 'b', 'c', 'd', 'e']

print(l.index('a'))
# 0

print(l.index('c'))
# 2

# print(l.index('x'))
# ValueError: 'x' is not in list

def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default

print(my_index(l, 'd'))
# 3

print(my_index(l, 'x'))
# False

print(my_index(l, 'x', -1))
# -1

l_dup = list('abcba')
print(l_dup)
# ['a', 'b', 'c', 'b', 'a']

print(l_dup.index('a'))
# 0

print(l_dup.index('b'))
# 1

print([i for i, x in enumerate(l_dup) if x == 'a'])
# [0, 4]

print([i for i, x in enumerate(l_dup) if x == 'b'])
# [1, 3]

print([i for i, x in enumerate(l_dup) if x == 'c'])
# [2]

print([i for i, x in enumerate(l_dup) if x == 'x'])
# []

def my_index_multi(l, x):
    return [i for i, _x in enumerate(l) if _x == x]

print(my_index_multi(l_dup, 'a'))
# [0, 4]

print(my_index_multi(l_dup, 'c'))
# [2]

print(my_index_multi(l_dup, 'x'))
# []

t = tuple('abcde')
print(t)
# ('a', 'b', 'c', 'd', 'e')

print(t.index('a'))
# 0

# print(t.index('x'))
# ValueError: tuple.index(x): x not in tuple

print(my_index(t, 'c'))
# 2

print(my_index(t, 'x'))
# False

t_dup = tuple('abcba')
print(t_dup)
# ('a', 'b', 'c', 'b', 'a')

print(my_index_multi(t_dup, 'a'))
# [0, 4]
