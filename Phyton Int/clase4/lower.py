texto =          'PyThOn'
textoMinus = texto.lower()
textoMayus = texto.upper()
print(textoMinus)
print(textoMayus)

# .strip() nos elimina los espacios en blanco al principio y al final de la cadena
# .replace() nos reemplaza un texto ej: 
'''texto = "Hola Mundo"   
print(texto.replace("Mundo", "Python"))
# Salida: Hola Python
''' 
#.startswith()
'''
texto = "Hola Mundo"   
print(texto.startswith("Hola"))
# Salida: True
'''
#.find() Devuelve la posición de la primera aparición de una subcadena dentro de la cadena, o -1 si no la encuentra.
texto = "Hola Mundo"   
print(texto.find("Mundo"))
# Salida: 5