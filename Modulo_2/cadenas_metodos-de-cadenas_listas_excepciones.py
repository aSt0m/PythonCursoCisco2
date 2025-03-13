

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
# Cifrado César.
# text = input("Ingresa tu mensaje: ")
# cipher = ''
# for char in text:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) + 1
#     if code > ord('Z'):
#         code = ord('A')
#     cipher += chr(code)

# print(cipher)
    

# Se ha escrito utilizando los siguientes supuestos:

# Solo acepta letras latinas (nota: los Romanos no usaban espacios en blanco ni dígitos).
# Todas las letras del mensaje están en mayúsculas (nota: los Romanos solo conocían las mayúsculas).
# Veamos el código:

# La línea 02: pide al usuario que ingrese un mensaje (sin cifrar) de una línea.
# La línea 03: prepara una cadena para el mensaje cifrado (esta vacía por ahora).
# La línea 04: inicia la iteración a través del mensaje.
# La línea 05: si el carácter actual no es alfabético...
# La línea 06: ...ignorala.
# La línea 07: convierta la letra a mayúsculas (es preferible hacerlo a ciegas, en lugar de verificar si es necesario o no).
# La línea 08: obtén el código de la letra e increméntalo en uno.
# La línea 09: si el código resultante ha "dejado" el alfabeto latino (si es mayor que el código de la Z)...
# La línea 10: ... cámbialo al código de la A.
# La línea 11: agrega el carácter recibido al final del mensaje cifrado.
# La línea 13: imprime el cifrado.
# El código, con este mensaje:

# AVE CAESAR

print("-" * 8, "Cifrado Cesar inverso", "-" * 8)

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

# line = input("Ingresa una línea de números, sepáralos con espacios: ")
# strings = line.split()
# total = 0
# try:
#     for substr in strings:
#         total += float(substr)
#     print("El total es:", total)
# except:
#     print(substr, "no es un numero.")




print("-" * 8 ,"Validor IBAN", "-" * 8)

# El cuarto programa implementa (en una forma ligeramente simplificada) un algoritmo utilizado por los bancos Europeos para especificar los números de cuenta. El estándar llamado IBAN (Número de cuenta bancaria internacional) proporciona un método simple y bastante confiable para validar los números de cuenta contra errores tipográficos simples que pueden ocurrir durante la reescritura del número, por ejemplo, de documentos en papel, como facturas o facturas en las computadoras.

# Puedes encontrar más detalles aquí: https://en.wikipedia.org/wiki/International_Bank_Account_Number.

# Un número de cuenta compatible con IBAN consta de:

# Un código de país de dos letras tomado del estándar ISO 3166-1 (por ejemplo, FR para Francia, GB para Gran Bretaña DE para Alemania, y así sucesivamente).
# Dos dígitos de verificación utilizados para realizar las verificaciones de validez: pruebas rápidas y simples, pero no totalmente confiables, que muestran si un número es inválido (distorsionado por un error tipográfico) o válido.
# El número de cuenta real (hasta 30 caracteres alfanuméricos; la longitud de esa parte depende del país).
# El estándar dice que la validación requiere los siguientes pasos (según Wikipedia):

# (Paso 1) Verificar que la longitud total del IBAN sea correcta según el país (este programa no lo hará, pero puedes modificar el código para cumplir con este requisito si lo deseas; pero debes enseñar al código a conocer todas las longitudes utilizadas en Europa).
# (Paso 2) Mueve los cuatro caracteres iniciales al final de la cadena (es decir, el código del país y los dígitos de verificación).
# (Paso 3) Reemplaza cada letra en la cadena con dos dígitos, expandiendo así la cadena, donde A = 10, B = 11 ... Z = 35.
# (Paso 4) Interpreta la cadena como un entero decimal y calcula el residuo de ese número dividiéndolo entre 97. Si el residuo es 1, pasa la prueba de verificación de dígitos y el IBAN puede ser válido.
# Observa el código en el editor. Analicémoslo:




# Validador IBAN.

# iban = input("Ingresa un IBAN, por favor: ")
# iban = iban.replace(' ','')

# if not iban.isalnum():
#     print("Has introducido caracteres no válidos.")
# elif len(iban) < 15:
#     print("El IBAN ingresado es demasiado corto.")
# elif len(iban) > 31:
#     print("El IBAN ingresado es demasiado largo.")
# else:
#     iban = (iban[4:] + iban[0:4]).upper()
#     iban2 = ''
#     for ch in iban:
#         if ch.isdigit():
#             iban2 += ch
#         else:
#             iban2 += str(10 + ord(ch) - ord('A'))
#     iban = int(iban2)
#     if iban % 97 == 1:
#         print("El IBAN ingresado es válido.")
#     else:
#         print("El IBAN ingresado no es válido.")


# Línea 03: pide al usuario que ingrese el IBAN (el número puede contener espacios, ya que mejoran significativamente la legibilidad del número...
# Línea 04: ... pero remueve los espacios de inmediato).
# Línea 06: el IBAN ingresado debe constar solo de dígitos y letras, de lo contrario...
# Línea 07: ... muestra un mensaje.
# Línea 08: el IBAN no debe tener menos de 15 caracteres (esta es la variante más corta, utilizada en Noruega).
# Línea 09: si es más corto, se informa al usuario.
# Línea 10: además, el IBAN no puede tener más de 31 caracteres (esta es la variante más larga, utilizada en Malta).
# Línea 11: si es más largo, se le informa al usuario.
# Línea 12: se comienza con el procesamiento.
# Línea 13: se mueven los cuatro caracteres iniciales al final del número y se convierten todas las letras a mayúsculas (paso 02 del algoritmo).
# Línea 14: esta es la variable utilizada para completar el número, creada al reemplazar las letras con dígitos (de acuerdo con el paso 03 del algoritmo).
# Línea 15: iterar a través del IBAN.
# Línea 16: si el carácter es un dígito...
# Línea 17: solo se copia.
# Línea 18: de lo contrario...
# Línea 19: ... conviértelo en dos dígitos (observa cómo se hace aquí).
# Línea 20: la forma convertida del IBAN está lista: ahora se convierte en un número entero.
# Línea 21: ¿el residuo de la división de iban2 entre 97 es igual a 1?
# Línea 22: si es así, entonces el número es correcto.
# Línea 23: de lo contrario...
# Línea 24: ... el número no es válido.
# Agreguemos algunos datos de prueba (todos estos números son válidos; puedes invalidarlos cambiando cualquier carácter).

# Inglés: GB72 HBZU 7006 7212 1253 00
# Francés: FR76 30003 03620 00020216907 50
# Alemán: DE02100100100152517108
# Si eres residente de la UE, puedes usar tu propio número de cuenta para hacer pruebas.