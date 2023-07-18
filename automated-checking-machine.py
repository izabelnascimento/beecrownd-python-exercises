x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]


def compativel(x, y):
    i = 0
    for i in range(5):
        if x[i] == y[i]:
            return False
    return True


if compativel(x, y):
    print("Y")
else:
    print("N")
