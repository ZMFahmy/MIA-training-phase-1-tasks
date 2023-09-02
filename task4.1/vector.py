from villain import Villain


class Vector(Villain):
    def __init__(self):
        super().__init__()
        self._plasma_grenades = 8
        self._sonic_resonance_cannon = 3
        self._quantum_deflector = 3

    def choose_weapon(self, n):
        if n == 1:  # laser blasters(infinite)
            if self.get_energy() < 40:
                return 0

            else:
                self.set_attack(8)
                self.decrement_energy(40)

        elif n == 2:  # plasma grenades
            if self.get_energy() < 56:
                return 0

            else:
                if self._plasma_grenades > 0:
                    self.set_attack(13)
                    self.decrement_energy(56)
                    self._plasma_grenades -= 1

                else:
                    return 1

        elif n == 3:  # sonic resonance canon
            if self.get_energy() < 100:
                return 0

            else:
                if self._sonic_resonance_cannon > 0:
                    self.set_attack(22)
                    self.decrement_energy(100)
                    self._sonic_resonance_cannon -= 1

                else:
                    return 1

    def choose_shield(self, n):
        if n == 1:  # energy net trap
            if self.get_energy() < 15:
                return 0

            else:
                self.set_shield(100 - 32)
                self.decrement_energy(15)

        elif n == 2:  # quantum deflector
            if self.get_energy() < 40:
                return 0

            else:
                if self._quantum_deflector > 0:
                    self.set_shield(100 - 80)
                    self.decrement_energy(40)
                    self._quantum_deflector -= 1

                else:
                    return 1

    def play_round(self, enemy_attack, enemy_special_effects):
        if enemy_special_effects == "Kalman Missile":
            self.decrement_health(enemy_attack)

        else:
            self.decrement_health(int(enemy_attack * self.get_shield() / 100))

    def get_inventory(self):  # used for drawing table
        return [self._plasma_grenades, self._sonic_resonance_cannon, self._quantum_deflector]
