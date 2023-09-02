# Parent class from which both Gru and Vector classes will inherit

class Villain:
    def __init__(self):
        self._health = 100
        self._energy = 500
        self._attack = 0
        self._shield = 100

    def choose_weapon(self, n):  # abstract class
        pass

    def choose_shield(self, n):  # abstract class
        pass

    def get_health(self):
        return self._health

    def get_energy(self):
        return self._energy

    def get_attack(self):
        return self._attack

    def get_shield(self):
        return self._shield

    def set_attack(self, attack):
        self._attack = attack

    def set_shield(self, shield):
        self._shield = shield

    def decrement_health(self, loss):
        self._health -= loss

    def decrement_energy(self, loss):
        self._energy -= loss

    def restart_stats(self):
        self._attack = 0
        self._shield = 100
