import math
def valor_seno(x,n_terminos):
    k = 0
    acum = 0
    while n_terminos!=0:
            q = 2*n_terminos-1
            numerador = x**q
            denominador = math.factorial(q)
            termino_total = numerador/denominador
            if k == k%2 == 1:
                termino_total = -1*termino_total
            acum += termino_total
            k+=1
            n_terminos = n_terminos - 1
            return acum
def num_primo(x):
    if x/2 == x//2!=1:
        return "el numero es divisible entre 2"
    elif x/3== x//3!=1:
        return " el numero es divisible entre 3"
    elif x/5 == x//5!= 1:
        return "el numero es divisible entre 5"
    elif x/7 == x//7!=1:
        return "el numero es divisible entre 7"
    else:
        return "el numero es primo"
def main():
   x= int(input(" si quiere saber si el numero que esribio es primo escriba 1, si desea hallar el seno de x con n terminos"
            " entonces escriba 2"))
   if x==1:
        q = int(input("digite el valor que quiere saber si es numero primo"))
        resultado = num_primo(q)
   if x == 2:
       a = float(input("digite el valor de x"))
       b = int(input("digite la cantidad de terminos que quiere que tenga la funcion"))
       resultado = valor_seno(a, b)
   print(resultado)
main()



