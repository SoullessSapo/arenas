
def aplanadora(x,y):
	lista = []
	x[0] = int(x[0])
	x[1] = int(x[1])
	#ciclo para poner todo aplanado osea en una sola lista
	for i in range(x[0]):
		for j in range(x[1]):
			lista.append(y[i][j])
	return lista
def triangulo_sup(x,y):
	m = x-1
	# m es para ayudar a indicar la diagonal secundaria
	for i in range(x//2-1,x):
		for j in range(x//2-1,x):
			#rango de estos hasat x//2 porque yo nada mas quiero tomar la parte de arriba de la matriz
			r = m-j
			w = m -i
			if x%2 == 1:
				if i != r and r <= x//2 and w<=x//2:
					#condiciones para sacar el triangulo superior de esta diagonal
					y[i][j] = 0
			elif x%2 == 0:
				if i != r and r <= x//2 and w<=x//2 and i != x//2 and j != x//2:
					#hice 2 casos porque para las matrics de tamaño pares me daba en la posicion x//2,x//2 un 0
					#asi que me toco restringir que pasara eso en las matrices con tamaño par
					y[i][j] = 0

	return y
def minas(x,y):
	pos = []
	x[0] = int(x[0])
	x[1] = int(x[1])
	for i in range(x[0]):
		fila = [0 for j in range(x[1])]
		pos.append(fila)
	for i in range(x[0]):
		for j in range(x[1]):
			cont = 0
			y[i][j] = int(y[i][j])
			for r in range(i - 1, i + 2):
				for t in range(j - 1, j + 2):
					if r >= 0 and r < x[0] and t >= 0 and t < x[1] and y[i][j] == ".":
						if i == r and j == t:
							pass
						else:
							y[r][t] = int(y[r][t])
							if y[r][t] == "*":
								cont += 1
					elif r >= 0 and r < x[0] and t >= 0 and t < x[1] and y[i][j] == "*":
						pos[i][j] = "*"
			if y[i][j] != "*":
				pos[i][j] = cont

def main():
	e = int(input("opcion 1,2,3"))
	if e == 1:
		n = 11
		lista = []
		tamaño = input("?")
		tamaño = tamaño.split(",")
		while n != 1:
			x = input("??")
			x = x.split(",")
			n = len(x)
			if n != 1:
				lista.append(x)
		res = aplanadora(tamaño,lista)
		print(*res,sep= ",")
	elif e == 2:
		n = 11
		lista = []
		x = int(input("?"))
		while n != 1:
			x = input("??")
			x = x.split(",")
			n = len(x)
			if n != 1:
				lista.append(x)

		res = triangulo_sup(x,lista)
		for i in range(x):
			print(*res[i],sep=",")
	elif e == 3:
		n = 11
		lista = []
		tamaño = input("?")
		tamaño = tamaño.split(",")
		for i in range(int(tamaño[0])):
			lista.append(input("?"))
		res = minas(tamaño,lista)
		for i in range(len(res)):
			print(*res[i],sep="")
	#funciones ingresar datos
main()























