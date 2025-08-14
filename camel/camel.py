s= input("camelCase: ")
a = ""
#separa el string en letras
for i in s:
    #verifica si la letra es may o no
    if i == i.upper():
     #si es may, la modifica a minuscula y le agrega un sufijo "_"
        i = "_" + i.lower()
        #suma la letra a una variable para reconstruir el str
    a += i
print("snake_case: " + a)

