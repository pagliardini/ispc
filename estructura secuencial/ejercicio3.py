""" EJERCICIO 3: Un hincha de fútbol desea conocer la cantidad de puntos que su

equipo lleva acumulados en el campeonato, para ello recibe cada semana la

información de la cantidad total de partidos, desde el inicio del campeonato, que

el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado

recibe un punto, por cada partido ganado tres puntos y por los perdidos cero

puntos. """


print("Sistema de cálculo de puntos de un equipo de fútbol")

partidos_perdidos = int(input("Partidos perdidos: "))
partidos_empatados = int(input("Partidos empatados: "))
partidos_ganados = int(input("Partidos ganados: "))

puntos = partidos_perdidos * 0 + partidos_empatados * 1 + partidos_ganados * 3

print(f"La cantidad de puntos acumulados es: {puntos}")
