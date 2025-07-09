z = complex(0, 0)
i = int(0)
f = float(0)
l = [0, 0]
t = (0, 0)

items = [z, i, f, l, t]


def f(i):
    match i:
        case int():
            print("is int", i)
        case float():
            print("is float", i)
        case complex():
            print("is complex", i)
        case list():
            print("list-y", i)
        case tuple():
            print("list-y", i)


for a in items:
    f(a)
