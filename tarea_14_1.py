def mezcla(x,y):
    i = 0
    nueva = []
    j = 0
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            nueva.append(x[i])
            i += 1
        elif y[j] < x[i]:
            nueva.append(y[j])
            j += 1
        else:
            nueva.append(x[i])
            i += 1
            nueva.append(y[j])
            j += 1
    if i < len(x):
        for k in range(i, len(x)):
            nueva.append(x[k])
    if j < len(y):
        for k in range(j, len(y)):
            nueva.append(y[k])
    return nueva
def merge(x):
    if len(x) == 1:
        return x
    else:
        mitad = len(x) // 2
        izq = x[0:mitad]
        der = x[mitad:len(x)]
        j = merge(izq)
        i = merge(der)
        nueva = mezcla(i,j)
        return nueva
def main():
    y = 1
    nueva = []
    while y != 0:
        y = int(input())
        if y == 0:
            break
        x = input().split()
        q = [int(t) for t in x]
        nueva.append(merge(q))
    for i in range(len(nueva)):
        print(*nueva[i])

main()