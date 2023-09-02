from gru import Gru
from vector import Vector

# creating objects of gamers classes
first_player = Gru()
second_player = Vector()
game_running = True


def draw_table():  # draws game interface every round
    gru_inventory = first_player.get_inventory()
    vector_inventory = second_player.get_inventory()

    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print(f"| Gru                                  Health: {first_player.get_health()}    Energy: {first_player.get_energy()} ||| Vector                                      Health: {second_player.get_health()}    Energy: {second_player.get_energy()} |")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("| Weapon                            Damage    Energy    Resources ||| Weapon                                   Damage    Energy    Resources |")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("|1.Freeze Gun                         11        50         inf    ||| 1.Laser Blasters                           8         40          inf   |")
    print(f"|2.Electric Prod                      18        88          {gru_inventory[0]}     ||| 2.Plasma Grenades                          13        56           {vector_inventory[0]}    |")
    print(f"|3.Mega Magnet                        10        92          {gru_inventory[1]}     ||| 3.Sonic Resonance Cannon                   13        56           {vector_inventory[1]}    |")
    print(f"|4.Kalman Missile                     20        120         {gru_inventory[2]}     |||                                                                        |")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("| Shield                             Save     Energy    Resources ||| Shield                                   Save     Energy    Resources  |")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("|5.Energy Projected Barrier Gun      40%        20         inf    ||| 4.Energy Net Trap                         32%        15         inf    |")
    print(f"|6.Selective Permeability            90%        50          {gru_inventory[3]}     ||| 5.Quantum Deflector                       80%        15          {vector_inventory[2]}     |")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")


while game_running:

    draw_table()
    print("\n")

    first_player_choice = int(input("Enter Gru's choice: "))
    second_player_choice = int(input("Enter Vector's choice: "))

    if first_player_choice < 5:
        first_player.choose_weapon(first_player_choice)

    else:
        first_player.choose_shield(first_player_choice - 4)

    if second_player_choice < 5:
        second_player.choose_weapon(second_player_choice)

    else:
        second_player.choose_shield(second_player_choice - 3)

    first_player_attack = first_player.get_attack()
    first_player_special_effect = first_player.get_special_effect()
    second_player_attack = second_player.get_attack()

    first_player.play_round(second_player_attack)
    second_player.play_round(first_player_attack, first_player_special_effect)

    # at the end of every round, the attack and shield of each player is restarted
    first_player.restart_stats()
    second_player.restart_stats()

    # game will stop when one of the players' health ends
    if first_player.get_health() <= 0 or second_player.get_health() <= 0:
        game_running = False

if first_player.get_health() <= 0:
    print("Vector Won !!!")

else:
    print("Gru Won !!!")
