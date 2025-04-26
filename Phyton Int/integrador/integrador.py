name = input('Ingrese su nombre: \t')
last_name = input('Ingrese su apellido: \t')
age = input('Ingrese su edad: \t')
mail = input('Ingrese su email: \t')

age_int = int(age)
name_formateado = name[0].upper() + name[1:].lower()
last_name_formateado = last_name[0].upper() + last_name[1:].lower()

correo_valido = (' ' not in mail) and (mail.count('@') == 1)

if age.isdigit():
    age_int = int(age)
else:
    print("Edad inválida. Debe ser un número.")
    exit()


if age_int < 15:
    rango = "Niño/a"
elif 15 <= age_int <= 18:
    rango = "Adolescente"
else:
    rango = "Adulto/a"

if age_int >= 18 and name != '' and last_name != '' and mail != '' :
 print (f' Bienvenido! {name_formateado} {last_name}, Usted tiene {age_int}, su correo es {mail}')
else : print ('ERROR')
#