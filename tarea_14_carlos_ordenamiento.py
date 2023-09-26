def mezcla(x,y):
    #X y Y son 2 listas ordenadas [4,5,6][1,2,3] == [1,2,3,4,5,6] / [2,4,7] , [1,3,5] == [1,2,3,4,5,7]
    #[1,5,7,8,9,10] , [3,6]/ [1,3,5,6]
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
            nueva.append(y[j])
            j+= 1
            i += 1
    if i == len(x):
        for i in range(j,len(y)):
            nueva.append(y[i])
    else:
        for i in range(i,len(x)):
            nueva.append(x[i])
    return nueva
def partir(x):
    # [3,2,5,6,4,7]
    #[3,2,5],[6,4,7]
    #[3,2],[5],[6,4],[7]
    #[3][2][5][6][4][7]
    #[2,3],[5],[4,6],[7]
    #[2,3,5],[4,6,7]
    #[2,3,4,5,6,7]
    if len(x) == 1:
        return x
    else:
        mitad = len(x) // 2
        izq = x[0:mitad]
        der = x[mitad:len(x)]
        j = partir(izq)
        i = partir(der)
        nueva = mezcla(i,j)
        return nueva
def main():
    x = [x for x in input("?").split(",")]
    print(partir(x))
main()