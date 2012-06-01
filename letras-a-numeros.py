def convertidor(texto):
	resultado = texto.upper()
	for valor in [['A','4'],['B','8'],['E','3'],['G','6'],['I','1'],['O','0'],['S','5'],['T','7'],['Z','2']]:
		resultado = resultado.replace(valor[0],valor[1])
	return resultado

print('Resultado: %s' % convertidor(input('Ingresa el texto:\n')))

while(input('¿Deseas ingresar otro texto? (Si: 1/ No: 0): ') == '1'):
	print('Resultado: %s' % convertidor(input('Ingresa el texto:\n')))