"""
Este programa te dice cuentas, cuales y cuantas veces se repite una letra ya sea mayuscula o minuscula, 
numeros en un string que entra como parametro.
"""
def duplicate_count(cadena):
    # Your code goes here
	cadena = cadena.lower()
	caracteres = []
	for i in range (len(cadena)):
		repeticiones = 0
		for j in range(len(cadena)):
			if cadena[i] == cadena[j]:
				print(cadena[i], cadena[j])
				repeticiones += 1
				variable = cadena[i] 
		if not(variable, repeticiones) in caracteres:
			caracteres.append((variable, repeticiones))
	i = 0
	while i < len(caracteres):
		if caracteres[i][1] < 2:
			caracteres.pop(i)
			i = 0
		else:
			i += 1
	return (len(caracteres), caracteres)
# bloque principal

print(duplicate_count('ABBA'))
