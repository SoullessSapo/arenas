import numpy as np
def dia_nacimiento(dia, mes, año):
    cod_año = 0

    cod_mes = 0

    dia_semana = 0
    if año in range(1900, 1999):
        cod_año = 0
    elif año in range(2000, 2099):
        cod_año = 6
    else:
        print("sapo")
    if mes == 1:
        cod_mes = 0
        mes = "enero "
    elif mes == 2:
        cod_mes = 3
        mes = "febrero"
    elif mes == 3:
        cod_mes = 3
        mes = "marzo"
    elif mes == 4:
        cod_mes = 6
        mes = "abril"
    elif mes == 5:
        cod_mes = 1
        mes = "mayo"
    elif mes == 6:
        cod_mes = 4
        mes = "junio"
    elif mes == 7:
        cod_mes = 6
        mes = "julio"
    elif mes == 8:
        cod_mes = 2
        mes = "agosto"
    elif mes == 9:
        cod_mes = 5
        mes = "septiembre"
    elif mes == 10:
        cod_mes = 0
        mes = "octubre"
    elif mes == 11:
        cod_mes = 3
        mes = "noviembre"
    elif mes == 12:
        cod_mes = 5
        mes = "diciembre"
    den_1 = año / 4
    numerador = dia + cod_mes + año + den_1 + cod_año
    r = int(numerador%7)
    # sapo es el resultado de la operacion para saber el dia
    sapo = r
    sapo-=1

    if sapo%4 == 0 or sapo % 100 == 0:
        sapo = sapo-1
    if sapo not in range(0,6):
        sapo = 6+sapo
    if sapo == 0:
        dia_semana = "domingo"
    elif sapo == 1:
        dia_semana = "lunes"
    elif sapo == 2:
        dia_semana = "martes"
    elif sapo == 3:
        dia_semana = "miercoles"
    elif sapo == 4:
        dia_semana = "jueves"
    elif sapo == 5:
        dia_semana = "viernes"
    elif sapo == 6:
        dia_semana = "sabado"

    return "nacio el", dia_semana, "de", mes, "del año", año


def calendar(dia,mes,año):
    #repetir fucion anterior pero cambiando los resultado para saber en que dia empieza el horario
    x = dia
    y = año
    z = mes
    lista = []
    for i in range(0, 7):
        fila = [0 for i in range(7)]
        lista.append(fila)
    cod_año = 0
    cod_mes = 0
    dia_semana = 0
    if año in range(1900, 1999):
        cod_año = 0
    elif año in range(2000, 2099):
        cod_año = 6
    if mes == 1:
        cod_mes = 0
        mes = "enero "
        dias = 31
    elif mes == 2:
        cod_mes = 3
        if año%4 == 0 or año%100 == 0:
            dias = 29
        else:
            dias = 28
        mes = "febrero"
    elif mes == 3:
        cod_mes = 3
        dias = 31
        mes = "marzo"
    elif mes == 4:
        cod_mes = 6
        dias = 30
        mes = "abril"
    elif mes == 5:
        cod_mes = 1
        dias = 31
        mes = "mayo"
    elif mes == 6:
        cod_mes = 4
        dias = 30
        mes = "junio"
    elif mes == 7:
        cod_mes = 6
        mes = "julio"
        dias = 31
    elif mes == 8:
        cod_mes = 2
        mes = "agosto"
        dias = 31
    elif mes == 9:
        cod_mes = 5
        mes = "septiembre"
        dias = 30
    elif mes == 10:
        cod_mes = 0
        mes = "octubre"
        dias = 31
    elif mes == 11:
        cod_mes = 3
        mes = "noviembre"
        dias = 30
    elif mes == 12:
        cod_mes = 5
        dias = 31
        mes = "diciembre"
    den_1 = año / 4
    numerador = dia + cod_mes + año + den_1 + cod_año
    r = int(numerador%7)
    sapo = r
    #sapo es el resultado de la operacion para saber el dia
    sapo-=1

    if sapo%4 == 0 or sapo % 100 == 0:
        sapo = sapo-1
    if sapo not in range(0,6):
        sapo = 6+sapo
    if sapo == 0:
        x = 0
        lista[0][0] = ""
        lista[1][0] = 1
    elif sapo == 1:
        x = 1
        lista[0][1] = "l"
        lista[1][1] = 1
    elif sapo == 2:
        x = 2
        lista[0][2] = "m"
        lista[1][2] = 1
    elif sapo == 3:
        x = 3
        lista[0][3] = "mi"
        lista[1][3] = 1
    elif sapo == 4:
        x = 4
        lista[0][4] = "j"
        lista[1][4] = 1
    elif sapo == 5:
        x = 5
        lista[0][5] = "v"
        lista[1][5] = 1
    elif sapo == 6:
        x = 6
        lista[0][6] = "s"
        lista[1][6] = 1
    #comienzo de creacion de horario asignando los dias de la semana
    lista[0][0] = 'd'
    lista[0][1] = 'l'
    lista[0][2] = 'm'
    lista[0][3] = 'mi'
    lista[0][4] = 'j'
    lista[0][5] = 'vi'
    lista[0][6] = 's'
    # contadores para llenar los espacios
    cont = 2
    x = x+1
    dias = int(dias)
    #funciones para comenzar a crear
    for i in range(x,7):
        lista[1][i] = cont
        cont = cont +1
    r = int(cont)
    for i in range(2,7):
        for j in range(0,7):
            lista[i][j] = r
            if r<dias:
                r = r+1
            else:
                break
    #funcion quitar 0 de la lista
    for i in range(1,7):
        for j in range(0,7):
            if lista[i][j] == 0:
                lista[i][j] = " "
    # aqui use una libreria pero fue para que el calendario me quedaran centradas las columnas con los dias
    print(mes.center(25))
    e = np.array(lista)
    return '\n'.join([''.join(['{:4}'.format(item) for item in row])
                         for row in e])

def comprobar(año, mes, dia):
    v = 0
    if año in range(1900, 2099):
        if mes == 2:
            if año % 4 == 0 and año % 100:
                if dia in range(1, 29):
                    v == True
                else:
                    v == False
            else:
                if dia in range(1, 28):
                    v == True
                else:
                    v == False
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia in range(1, 31):
                v = True
            else:
                v = False
        elif mes == 2 or mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia in range(1, 30):
                v = True
            else:
                v = False
        return v


def main():
    v = False
    while v!=True:
        dia = int(input("ingrese el dia en el que nacio"))
        mes = int(input("Ingrese el mes en el que nacio"))
        año = int(input("ingrese el año en el que nacio"))
        v = comprobar(año,mes,dia)
        if v != True:
            print("digite el valor otra vez")

    resultado = int(input(" escriba 1 si quiere hacer saber el dia en el que nacio o escriba 2 para saber su calendario"))

    if resultado == 1:
        resultado = dia_nacimiento(dia, mes, año)
        print(resultado)
    else:
        resultado = calendar(año, mes, dia)
        print(resultado)

main()
