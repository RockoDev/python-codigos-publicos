import random

c = [['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'],['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z'],['0','1','2','3','4','5','6','7','8','9'],['-','.',',','_','@','#','$','%','&','/','(',')','=','?','¿','¡','!','<','>','{','}','[',']','+','*']]

def contrasena(n):
	r = ''
	for caracter in range(0, int(n)):
		r = r + random.choice(random.choice(c))
	return r

print(contrasena(input('Ingresa el numero de caracteres que quieres que tenga la contrseña:')))
input('Presiona enter para salir.')