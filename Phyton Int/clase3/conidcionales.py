''' 
Solicito al cliente nombrre, apellido, eddad, correo.
Almacewno esos datos en variables
los muestro organizados en formas de una tarjeta de presentacion en la pantalla
'''
'''
Algoritmos: pasos logicos (diagrama de flujo, pseudocodigo y codigo fuente)
lenguaje Python

Datos entra a una Variable
Variable: caja, contenedor o espacio de memoria

Tipos de datos
numeros(int, float), string (cadena de texto), bool (true or false, 1 o 0)


'''

#declarar las variables con un operador de asignacion
nombre = None
apellido = None
edad = None
email = None

#solicito ingreso de datos // INPUT siempre retorna una cadena 
nombre = input('Ingrese su nombre\t') 
apellido = input('ingrese su apellido\t')
edad = int(input('ingrese su edad\t')) #el input siempre retorna una cadena
# edad mas alla del numero que ingrese, siempre sera un tipo de dato str
email = input ('ingrese su mail\t')
  
#Imprimir los datos ingresados en la terminal / consola / pantalla

print('su nombre es \t ', nombre, apellido)
print(f'Usted tiene \t', {edad}, 'years old')
print(f'su mail es \t', {email})

#falta el procesamiento 
'yo podria comparar la edad'
''' 
Si condicion (edad es mayor o igual a 18) entonces
  Salgo por el verdadero (true)
  imprimo registro existoso
Sino
  salgo por el falso (false)
  imprimo debe ser mayor de 18
'''

# Antes de comparar debo convertir el tipo de dato de edad a int



if edad >= 18 : #comparo edad (str) con 18 (int)
    #bloque de codigo si se cumple la coindicion = true
    print('Registro existoso') #intentacion
else :
  #bloque de codigo si no se cumple la coindicion = false
  print('segui participando cuando seas mayor')


# ejemplo practico con condiciones combinadas

usuario = 'admin'
password = '123'

# verificamos si usuario y password coinciden

login_correcto = (usuario =='admin') and (password == '123')
print ('login correcto?', login_correcto) #true