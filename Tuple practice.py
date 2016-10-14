
tuplex = 5, 10, 15, 20, 25
print(tuplex)

tuplex = 5,
print(tuplex)


listx = [5, 10, 7, 4, 15, 3]
print(listx)

tuplex = tuple(listx)
print(tuplex)

tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str =  ''.join(tup)
print(str)


tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

_slice = tuplex[3:5]

print(_slice)

_slice = tuplex[:6]
print(_slice)

_slice = tuplex[5:]
print(_slice)

_slice = tuplex[:]
print(_slice)

_slice = tuplex[-8:-4]
print(_slice)

tuplex = tuple("HELLO WORLD")
print(tuplex)


_slice = tuplex[2:9:2]
print(_slice)

_slice = tuplex[::4]
print(_slice)

_slice = tuplex[9:2:-4]
print(_slice)

tuplex = ((2, "w"),(3, "r"))
print(dict((y, x) for x, y in tuplex))



