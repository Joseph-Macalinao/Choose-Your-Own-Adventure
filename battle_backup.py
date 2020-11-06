import random
from monsters import monster_naming
battle_intro = "You have entered combat "

def battle():
    player_health = 20
    enemy_health = random.randint(15, 20)
    heal_amount = random.randint(4, 6)
    attack_amount = random.randint(3, 6)
    enemy_attack = random.randint(1, 2)
    print("You have entered combat. Your enemy is a " + str(monster_naming()) + " and has " + str(enemy_health) + " health.")
    while enemy_health > 0:
        print("1. Attack\n2. Item")
        action = str(input())
        if action == "attack":
            print("You do " + str(attack_amount) + " damage.")
            enemy_health = enemy_health - attack_amount
            if enemy_health <= 0:
                end_of_battle_health = player_health
                print("Congrats. You have defeated your enemy.")

                print("You leave with " + str(end_of_battle_health) + " health.")
                from non_battle import out_of_battle
                out_of_battle()
            else:
                print("The enemy now has " + str(enemy_health) + " health.")
        else:
            print("Would you like to heal or enchant weapon?")
            item_choice = str(input())
            if item_choice == "heal":
                print("You healed for " + str(heal_amount) + " health.")
                player_health = player_health + heal_amount
                print("You now have " + str(player_health) + " health.")
            else:
                attack_amount = (attack_amount * 2)
                print("You now do " + str(attack_amount) + " " + "damage")

        print("The enemy did " + str(enemy_attack) + " damage to you.")
        player_health = player_health - enemy_attack
        print("You now have " + str(player_health) + " health.")


battle()
