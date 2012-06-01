def convertidor(texto):
	resultado = texto.upper()
	for valor in [['A','4'],['B','8'],['E','3'],['G','6'],['I','1'],['O','0'],['S','5'],['T','7'],['Z','2']]:
		resultado = resultado.replace(valor[0],valor[1])
	return resultado

texto = input('Ingresa el texto:\n')
while(texto != ''):
	print('Resultado: %s' % convertidor(texto))
	texto = input('Ingresa otro texto:\n')