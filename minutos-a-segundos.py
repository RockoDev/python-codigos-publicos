def segundos(t):
	a = t.split(':')
	r = 0
	if(len(a) == 3):
		h = int(a[0])
		m = int(a[1])
		s = int(a[2])
		r = r + (h*3600)
		r = r + (m*60)
		r = r + s
	elif(len(a) == 2):
		m = int(a[0])
		s = int(a[1])
		r = r + (m*60)
		r = r + s
	elif(len(a) == 1):
		s = int(a[0])
		r = s
	else:
		r = 0
	return r

i = input('Ingresa el tiempo:\n')
while(i != ''):
	print('Segundos: %s' % segundos(i))
	i = input('Ingresa otro tiempo:\n')