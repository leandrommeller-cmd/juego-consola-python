import random
from clases.enemigo import Enemigo
from clases.jugador import Jugador


def main():
    nombre_jugador = input("Bienvenido a la Aventura Espacial. Ingresa tu nombre: ")
    jugador = Jugador(nombre_jugador)

    enemigos = [
        Enemigo("alien", 50, 10),
        Enemigo("robot", 30, 5),
        Enemigo("monstruo", 70, 15),
    ]

    enemigos_derrotados = []

    print(f'{jugador.nombre}, comienza tu aventura!')

    while enemigos:
        enemigo_actual = random.choice(enemigos)
        if enemigo_actual in enemigos_derrotados:
            continue
        print(f"\nTe encuentras con un {enemigo_actual.nombre} en tu camino")

        while enemigo_actual.salud > 0:
            accion = input("¿Qué deseas hacer? (atacar/huir): ").lower()
            if accion == "atacar":
                dano_jugador = jugador.atacar()
                enemigo_actual.recibir_dano(dano_jugador)
                print(f"\nHas atacado al {enemigo_actual.nombre} y le has hecho {dano_jugador} de daño.")
                if enemigo_actual.salud > 0:
                    dano_enemigo = enemigo_actual.atacar()
                    jugador.recibir_dano(dano_enemigo)
                    print(f"Le quedan {enemigo_actual.salud} puntos de salud.")
                    print(f"El {enemigo_actual.nombre} te ha atacado y te ha hecho {dano_enemigo} de daño.")
                    print(f"Te quedan {jugador.salud} puntos de salud.")
            elif accion == "huir":
                print(f"\nHas decidido huir del {enemigo_actual.nombre}.")
                break

        if jugador.salud <= 0:
            print("Has perdido la partida. Inténtalo de nuevo.")
            break

        if enemigo_actual.salud <= 0:
            print(f"Has derrotado al {enemigo_actual.nombre}!")
            enemigos_derrotados.append(enemigo_actual)
            enemigos.remove(enemigo_actual)
            jugador.ganar_experiencia(20)

        continuar = input("¿Deseas continuar tu aventura? (si/no): ").lower()

        if continuar == "no":
            print("Gracias por haber jugado Batallas Galácticas. Hasta la próxima aventura!")
            break

    if not enemigos:
        print("Felicidades! Has derrotado a todos los enemigos y ganado la partida!")

if __name__ == '__main__':
    main()
