import random
import sys

# Definición de personajes usando diccionarios
definir_personajes = [
    {'nombre': 'Guerrero', 'hp': 120, 'atk_min': 15, 'atk_max': 25},
    {'nombre': 'Arquero',  'hp': 100, 'atk_min': 10, 'atk_max': 30},
    {'nombre': 'Mago',     'hp': 80,  'atk_min': 20, 'atk_max': 35}
]

while True:
    # Pantalla de inicio con pixel art
    print(r"""
  ____                          _   _                 
 |  _ \ ___  _   _ _ __   ___  | |_| |__   ___ _ __   
 | |_) / _ \| | | | '_ \ / _ \ | __| '_ \ / _ \ '__|  
 |  __/ (_) | |_| | | | |  __/ | |_| | | |  __/ |     
 |_|   \___/ \__,_|_| |_|\___|  \__|_| |_|\___|_|     

       [1] JUGAR    [2] PERSONAJES    [3] SALIR
""")
    opcion = input("Selecciona una opción (1-3): ")

    if opcion == '1':
        # Iniciar juego
        # Selección de personaje del jugador
        print("\n--- Elige tu personaje ---")
        for i, p in enumerate(definir_personajes, 1):
            print(f"{i}. {p['nombre']} (HP: {p['hp']}, Ataque: {p['atk_min']}-{p['atk_max']})")
        while True:
            elec = input("> ")
            if elec in ['1', '2', '3']:
                jugador = definir_personajes[int(elec) - 1].copy()
                break
            print("Opción inválida, elige 1, 2 o 3.")

        # Selección de enemigo distinto
        enemigos = [p for p in definir_personajes if p['nombre'] != jugador['nombre']]
        enemigo = random.choice(enemigos).copy()

        player_hp = jugador['hp']
        enemy_hp = enemigo['hp']

        print(f"\n¡Has elegido a {jugador['nombre']}! Prepárate para el combate contra el {enemigo['nombre']}!\n")

        # Bucle principal de combate
        while player_hp > 0 and enemy_hp > 0:
            print(f"Tu vida ({jugador['nombre']}): {player_hp}")
            print(f"Vida enemigo ({enemigo['nombre']}): {enemy_hp}\n")

            defend = False
            print("1. Atacar    2. Defender")
            accion = input("> ")
            if accion == '1':
                dano = random.randint(jugador['atk_min'], jugador['atk_max'])
                enemy_hp -= dano
                print(f"Atacaste e hiciste {dano} de daño!\n")
            elif accion == '2':
                defend = True
                print("Te defiendes y reduces el próximo daño recibido.\n")
            else:
                print("Turno perdido por opción inválida!\n")

            if enemy_hp > 0:
                enemy_defend = False
                acc_en = random.choice(['ataque', 'ataque', 'defensa'])
                if acc_en == 'ataque':
                    dano = random.randint(enemigo['atk_min'], enemigo['atk_max'])
                    if defend:
                        dano //= 2
                    player_hp -= dano
                    print(f"El enemigo ataca e inflige {dano} de daño!\n")
                else:
                    enemy_defend = True
                    print("El enemigo se defiende y reducirá su próximo daño.\n")

        # Resultado final
        if player_hp <= 0:
            print("*** ¡Has sido derrotado! Game Over. ***")
        else:
            print("*** ¡Felicidades! Has vencido al enemigo. ***")

        input("\nPresiona Enter para volver al menú...")

    elif opcion == '2':
        # Mostrar personajes disponibles
        print("\n--- Lista de Personajes Jugables ---")
        for p in definir_personajes:
            print(f"- {p['nombre']} (HP: {p['hp']}, Ataque: {p['atk_min']}-{p['atk_max']})")
        input("\nPresiona Enter para volver al menú...")

    elif opcion == '3':
        # Salir del juego
        print("\nGracias por jugar. ¡Hasta la próxima!")
        sys.exit()

    else:
        print("Opción inválida, elige 1, 2 o 3.\n")
        continue
