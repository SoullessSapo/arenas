def castigo(x):
    r = 0
    lis = []
    while r not in lis:
        r = []
        q = ""
        w = ""
        for i in range(len(str(x))):
            r.append(str(x)[i])
        r.sort()
        for i in r:
            q = i + q
            w = w + i
        w = int(w)
        q = int(w)
        res = w - q
        lis.append(res)
        x = res
    return len(lis)
def main():
    x = int(input("?"))
    print(castigo(x))
main()






