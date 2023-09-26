from sys import stdin

class DisjointSets:
    def __init__(self, data=[]):
        self.data = []
        for e in data:
            self.makeSet(e)
    # Encontrar el conjunto al cual pertenece el elemento e
    def findSet(self, e):
        for conjunto in self.data:
            if e in conjunto:
                return conjunto
        return None
    # Crear un conjunto dado un elemento cáracteristico,
    # siempre que no exista un conjunto con ese elemento en la estructura
    def makeSet(self, e):
        conjunto = self.findSet(e)
        if conjunto is None:
            self.data.append(set([e]))
            return self.data[-1]
        return conjunto
    def union(self, a, b):
        st1 = self.makeSet(a)
        st2 = self.makeSet(b)
        if st1 != st2:
            st3 = st1.union(st2)
            self.data.remove(st1)
            self.data.remove(st2)
            self.data.append(st3)
    def __str__(self):
        return str(self.data)

def processCommand(dj, command):
    p1, com, p2 = command
    if com == "c":
        dj.union(int(p1), int(p2))
    else:
        return dj.findSet(int(p1)) == dj.findSet(int(p2))

def main():
    cas = int(stdin.readline().strip())
    stdin.readline().strip()
    for caso in range(cas):
        q_suc, q_err = 0,0
        n_comp = int(stdin.readline().strip())
        dj = DisjointSets([x for x in range(1,n_comp+1)])
        line = stdin.readline().strip()
        while line:
            command = line.split()
            result = processCommand(dj, command)
            if result is not None:
                q_suc, q_err = q_suc + (result == True), q_err + (result == False)
            line = stdin.readline().strip()
        print(q_suc, q_err)
        print()
main()