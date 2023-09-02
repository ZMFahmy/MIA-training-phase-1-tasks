from villain import Villain


class Gru(Villain):
    def __init__(self):
        super().__init__()
        self._electric_pod = 5
        self._mega_magnet = 3
        self._kalman_missile = 1
        self._selective_permeability = 2
        self._special_effects = None

    def choose_weapon(self, n):
        if n == 1:  # freeze gun(infinite)
            if self.get_energy() < 50:
                return 0

            else:
                self.set_attack(11)
                self.decrement_energy(50)

        elif n == 2:  # electric pod
            if self.get_energy() < 88:
                return 0

            else:
                if self._electric_pod > 0:
                    self.set_attack(18)
                    self.decrement_energy(88)
                    self._electric_pod -= 1

                else:
                    return 1

        elif n == 3:  # mega magnet
            if self.get_energy() < 92:
                return 0

            else:
                if self._mega_magnet > 0:
                    self.set_attack(10)
                    self.decrement_energy(92)
                    self._mega_magnet -= 1
                    self._special_effects = "Mega Magnet"

                else:
                    return 1

        elif n == 4:  # kalman missile
            if self.get_energy() < 120:
                return 0

            else:
                if self._kalman_missile > 0:
                    self.set_attack(20)
                    self.decrement_energy(120)
                    self._kalman_missile -= 1
                    self._special_effects = "Kalman Missile"

                else:
                    return 1

    def choose_shield(self, n):
        if n == 1:  # energy projected barrier gun
            if self.get_energy() < 20:
                return 0

            else:
                self.set_shield(100 - 40)
                self.decrement_energy(20)

        elif n == 2:  # selective permeability
            if self.get_energy() < 50:
                return 0

            else:
                if self._selective_permeability > 0:
                    self.set_shield(100 - 90)
                    self.decrement_energy(50)
                    self._selective_permeability -= 1

                else:
                    return 1

    def play_round(self, enemy_attack):
        if enemy_attack > 0 and self._special_effects == "Mega Magnet":
            self.decrement_health(int(enemy_attack * 80 / 100 * self.get_shield() / 100))
            self._special_effects = None

        else:
            self.decrement_health(int(enemy_attack * self.get_shield() / 100))

        if self._special_effects == "Kalman Missile":
            self._special_effects = None

    def get_special_effect(self):
        return self._special_effects

    def get_inventory(self):  # used for drawing table
        return [self._electric_pod, self._mega_magnet, self._kalman_missile, self._selective_permeability]
