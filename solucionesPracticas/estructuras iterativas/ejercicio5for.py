numero = int(input("Ingrese un número entre 1 y 10: "))

if 1 <= numero <= 10:
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")
else:
    print("Número fuera de rango (1-10)")
