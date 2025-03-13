

"""
Este archivo contiene los ejercicios de las seccion 1 del modulo 2 del curso de python nivel intermedio
"""
print("-" * 8, "Metodos de cadena", "-" * 8)

# s1 = "¿Dónde están las nieves de antaño?"
# s2 = s1.split()
# print(s2)
# print(s2[-2])

print("------- Operaciones con cadenas --------")
print("")


# chr(ord(x)) == x
# ord(chr(x)) == x





print("-" * 8, "Cadenas en acción", "-" * 8)

print("-" * 8, "Display 7 segmentos", "-" * 8)

# digits = [ '1111110',  	# 0
# 	   '0110000',	# 1
# 	   '1101101',	# 2
# 	   '1111001',	# 3
# 	   '0110011',	# 4
# 	   '1011011',	# 5
# 	   '1011111',	# 6
# 	   '1110000',	# 7
# 	   '1111111',	# 8
# 	   '1111011',	# 9
# 	   ]

# def print_number(num):
# 	global digits
# 	digs = str(num)
# 	lines = [ '' for lin in range(5) ]
# 	for d in digs:
# 		segs = [ [' ',' ',' '] for lin in range(5) ]
# 		ptrn = digits[ord(d) - ord('0')]
# 		if ptrn[0] == '1':
# 			segs[0][0] = segs[0][1] = segs[0][2] = '#'
# 		if ptrn[1] == '1':
# 			segs[0][2] = segs[1][2] = segs[2][2] = '#'
# 		if ptrn[2] == '1':
# 			segs[2][2] = segs[3][2] = segs[4][2] = '#'
# 		if ptrn[3] == '1':
# 			segs[4][0] = segs[4][1] = segs[4][2] = '#'
# 		if ptrn[4] == '1':
# 			segs[2][0] = segs[3][0] = segs[4][0] = '#'
# 		if ptrn[5] == '1':
# 			segs[0][0] = segs[1][0] = segs[2][0] = '#'
# 		if ptrn[6] == '1':
# 			segs[2][0] = segs[2][1] = segs[2][2] = '#'
# 		for lin in range(5):
# 			lines[lin] += ''.join(segs[lin]) + ' '
# 	for lin in lines:
# 		print(lin)


# print_number(int(input("Ingresa el número que deseas mostrar: ")))


print("-" * 8, "Cifrado Cesar", "-" * 8)
# Cifrado César - descifrando un mensaje.
# cipher = input('Ingresa tu criptograma: ')
# text = ''
# for char in cipher:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) - 1
#     if code < ord('A'):
#         code = ord('Z')
#     text += chr(code)

# print(text)



print("-" * 8 ,"Procesador de Números.", "-" * 8)

line = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except:
    print(substr, "no es un numero.")