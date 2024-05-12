# 1 Condicional parcial (solo el if) con expresión lógica simple

# Descripción: Verificar si un número es positivo.

numero = 10
if numero > 0:
    print("El número es positivo")

# 2 Condicional completo (if - else) con expresión lógica simple

# Descripción: Determinar si un número es par o impar.

numero2 = 9
if numero2 % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# 3 Condicional parcial (solo el if) con expresión lógica compuesta (and)

# Descripción: Verificar si un número está en el rango de 10 a 20.


numero3 = 15
if numero3 >= 10 and numero3 <= 20:
    print("El número está en el rango de 10 a 20")

# 4 Condicional completo (if - else) con expresión lógica compuesta (or)

# Descripción: Determinar si un número es múltiplo de 3 o de 5.

numero4 = 15
if numero4 % 3 == 0 or numero4 % 5 == 0:
    print("El número es múltiplo de 3 o de 5")
else:
    print("El número no es múltiplo de 3 ni de 5")

# Ejemplo de la despensa de barrio

# Descripción: Calcular el costo total de la compra de leche de un cliente, considerando descuentos por cantidad y promoción para jubilados.

unidades_compradas = 25
precio_unidad = 1000
descuento_cantidad = 0
descuento_jubilado = 0

if unidades_compradas > 24:
    descuento_cantidad = 0.15
elif unidades_compradas > 12:
    descuento_cantidad = 0.10

es_jubilado = True
if es_jubilado:
    descuento_jubilado = 0.10

precio_total = unidades_compradas * precio_unidad
descuento_total = precio_total * (descuento_cantidad + descuento_jubilado)
precio_final = precio_total - descuento_total

print(f"El cliente debe pagar: {precio_final} pesos")