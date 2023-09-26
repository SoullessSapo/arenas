def hoyos(x,y):
    pos = []
    x[0] = int(x[0])
    x[1] = int(x[1])
    for i in range(x[0]):
        for j in range(x[1]):
            for r in range(i-1, i + 2):
                for t in range(j-1, j + 2):
                    if r >= 0 and r < x[0] and t >=0 and t<x[1]:
                        if i == r and j == t:
                            pass
                        else:
                            if y[i][j] >= y[r][t]:

    return pos
def main():
    x = input("?")
    x = x.split(",")
    y = []
    q = int(x[0])
    for i in range(q):
        r = input("??")
        r = r.split(",")
        y.append(r)
    res = hoyos(x,y)
    print(res)
main()