def rotacion(x):
    r = x[0]
    #x[0] es el numero el cual se va a rotar
    q = int(x[2])
    #x[2] es la cantidad de numeros que se va coger de izquierda o derecha
    res = "q"

    if x[1] == "derecha":
        #caso en el que x[1] de derecha
        for i in range(1,q+1):
            #rango para poner primero los que se van a rotar
            if i == 1:
                res = r[len(r)-i]
            else:
                res = r[len(r) - i] +res
            #rango para poner los demas numeros siguientes al que se roto
        for i in range(len(r)-q):
            # rango para poner los demas numeros siguientes al que se roto
            res = res + r[i]

    elif x[1] == "izquierda":
        for i in range(q+1,len(r)):
            # rango para rotar los numeros pedidos
            if i == q+1:
                res = r[i]
            else:
                res = res + r[i]
        for i in range(q+1):
            #rango para poner el resto de los numeros 
            res = res + r[i]
    return res
def main():
    x = input("?")
    x = x.split()
    res = rotacion(x)
    print(*res, sep = "")
main()