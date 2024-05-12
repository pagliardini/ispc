""" EJERCICIO 2: Un pintor de casas debe hacer un presupuesto para un cliente. Lo

que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El

cliente le indica que necesita conocer el costo de mano de obra para pintar una

pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro

cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para

pintar la pared. """

print("Sistema de cálculo de costo de por m2")
print("La unidad de medida es metros por lo cual es importante usar esta medida al ingresar los datos.")

alto = float(input("Por favor ingrese la altura de la pared: "))
ancho = float(input("Por favor ingrese el ancho de la pared: "))

m2 = ancho * alto

costoxm2 = float(input("Ingrese el costo por m2: "))

costo = costoxm2 * m2

print(f"El costo de mano de obra para pintar una pared de {alto} metros de alto y {ancho} metros de ancho,({m2} metros cuadrados) es de ${costo} pesos.")
