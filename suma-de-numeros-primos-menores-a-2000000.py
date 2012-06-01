nps = []
l = 2000000
s = 0
for n in range(1, l):
	nnp = 0
	for nd in range(1, n + 1):
		if(n % nd == 0):
			nnp += 1
	if(nnp == 2):
		nps.append(n)
		print('%d - (%d%%)' % (n, round((n/l)*100)))
for np in nps:
	s = s + np
print('Completado.\n\nResultado de la suma de todos los números primos menores a %d: %d.\nNúmeros primos detectados: %d\n' % (l, s, len(nps)))
input('Presiona enter para salir.')