def superdigit(n,k):
    def ayuda(n):
        total = 0
        for num in n:
            total += int(num)
        total = str(total)
        if len(total) == 1:
            return total
        else:
            return ayuda(total)
    p = str(ayuda(n)*k)
    return ayuda(p)
def main():
    line = stdin.readline().strip()
    while line:
        lis = line.split()
        X,N = int(lis[0]),int(lis[1])
        print(superdigit(X,N))
        line = stdin.readline().strip()
main()
