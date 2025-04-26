#operqaopreadores logicos 

edad = int(15)
lic_con = True #bool

# AND: ambas coindiciones deben ser verdaderas
print('tiene mas de 18 y licencia?', edad > 18 and lic_con) # true
 
# OR: al menos una coindicion debe ser verdadera
print('tiene mas de 18 años o lincencia?', edad > 18 or lic_con)

# NOT invierte el valor logico
es_menor = edad < 18 
print('no es menor de edad?', not es_menor)
