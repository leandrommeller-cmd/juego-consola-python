import random


class Enemigo:
    def __init__(self, nombre, salud, dano):
        self.nombre = nombre
        self.salud = salud
        self.dano = dano

    def atacar(self):
        return random.randint(5, 15)

    def recibir_dano(self, dano):
        self.salud -= dano
        if self.salud <= 0:
            return True
        return False
