"""Pedir que el usuario ingrese (input) nombre de 
personas y mostrarlos hasta que el valor de lo que ingresa sea “fin”"""



nombre = str(input("Ingrese el nombre de la persona: "))

while nombre != "fin":
    print(nombre)
    nombre = str(input("Ingrese el nombre de la persona: "))
        