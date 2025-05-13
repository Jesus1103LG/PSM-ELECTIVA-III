import random
import sys

# Clases de personajes usando POO
class Personaje:
    def __init__(self, nombre, hp, atk_min, atk_max):
        self.nombre = nombre
        self.hp = hp
        self.atk_min = atk_min
        self.atk_max = atk_max
        self.defendiendo = False

    def atacar(self, objetivo):
        daño = random.randint(self.atk_min, self.atk_max)
        if objetivo.defendiendo:
            daño //= 2
        objetivo.hp -= daño
        print(f"{self.nombre} ataca a {objetivo.nombre} e inflige {daño} de daño!")
        objetivo.defendiendo = False

    def defender(self):
        self.defendiendo = True
        print(f"{self.nombre} se defiende y reducirá el próximo daño recibido.")

    def esta_vivo(self):
        return self.hp > 0

class Guerrero(Personaje):
    def __init__(self):
        super().__init__("Guerrero", hp=120, atk_min=15, atk_max=25)

class Arquero(Personaje):
    def __init__(self):
        super().__init__("Arquero", hp=100, atk_min=10, atk_max=30)

class Mago(Personaje):
    def __init__(self):
        super().__init__("Mago", hp=80, atk_min=20, atk_max=35)

# Lista de clases disponibles
clases = [Guerrero, Arquero, Mago]

# Funciones de juego
def mostrar_menu():
    print(r"""
  ___      _   __  __ _           
 / _ \ ___| |_|  \/  (_)_ __ ___  
| | | / __| __| |\/| | | '__/ _ \ 
| |_| \__ \ |_| |  | | | | |  __/ 
 \___/|___/\__|_|  |_|_|_|  \___| 
                                      
             ArkMine               

    [1] JUGAR    [2] PERSONAJES    [3] SALIR
""")

def seleccionar_personaje():
    print("\n--- Elige tu personaje ---")
    for idx, cls in enumerate(clases, 1):
        temp = cls()
        print(f"{idx}. {temp.nombre} (HP: {temp.hp}, Ataque: {temp.atk_min}-{temp.atk_max})")
    while True:
        elec = input("> ")
        if elec in [str(i) for i in range(1, len(clases)+1)]:
            return clases[int(elec)-1]()
        print("Opción inválida, elige un número válido.")

def mostrar_personajes():
    print("\n--- Lista de Personajes Jugables ---")
    for cls in clases:
        temp = cls()
        print(f"- {temp.nombre} (HP: {temp.hp}, Ataque: {temp.atk_min}-{temp.atk_max})")
    input("\nPresiona Enter para volver al menú...")

def iniciar_combate(jugador, enemigo):
    print(f"\n¡Has elegido a {jugador.nombre}! Prepárate para el combate contra {enemigo.nombre}!\n")
    while jugador.esta_vivo() and enemigo.esta_vivo():
        print(f"{jugador.nombre} HP: {jugador.hp} | {enemigo.nombre} HP: {enemigo.hp}\n")
        print("1. Atacar    2. Defender")
        accion = input("> ")
        if accion == '1':
            jugador.atacar(enemigo)
        elif accion == '2':
            jugador.defender()
        else:
            print("Turno perdido por opción inválida!")
        if enemigo.esta_vivo():
            # Acción del enemigo
            if random.choice(['ataque','ataque','defensa']) == 'ataque':
                enemigo.atacar(jugador)
            else:
                enemigo.defender()
        print()
    # Resultado
    if not jugador.esta_vivo():
        print("*** ¡Has sido derrotado! Game Over. ***)")
    else:
        print("*** ¡Felicidades! Has vencido al enemigo. ***)")
    input("\nPresiona Enter para volver al menú...")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-3): ")
    if opcion == '1':
        jugador = seleccionar_personaje()
        enemigo = random.choice([cls() for cls in clases if cls != type(jugador)])
        iniciar_combate(jugador, enemigo)
    elif opcion == '2':
        mostrar_personajes()
    elif opcion == '3':
        print("\nGracias por jugar. ¡Hasta la próxima!")
        sys.exit()
    else:
        print("Opción inválida, elige 1, 2 o 3.\n")
