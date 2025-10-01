import random


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.salud = 100
        self.nivel = 1
        self.experiencia = 0
    
    def atacar(self):
        return random.randint(10, 20) * self.nivel
    
    def recibir_dano(self, dano):
        self.salud -= dano
        if self.salud <= 0:
            print(f"Has sido derrotado. Game Over!")
        
    def ganar_experiencia(self, puntos):
        self.experiencia += puntos
        print(f"Has ganado {puntos} puntos de experiencia.")
        if self.experiencia >= 100:
            self.nivel += 1
            self.experiencia = 0
            print(f"Has subido al nivel {self.nivel}!")
        
    