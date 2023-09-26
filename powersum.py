from sys import stdin

def powersum(X,N):
    def ayuda(total,potencia,num):
        valor = total - num**potencia
        if valor == 0:
            return 1
        elif valor < 0:
            return 0
        else:
            return ayuda(valor,potencia,num+1) + ayuda(total,potencia,num+1)
    return ayuda(X,N,1)



def main():
    line = stdin.readline().strip()
    while line:
        X,N = map(int,line.split())
        print(powersum(X,N))
        line = stdin.readline().strip()
main()
