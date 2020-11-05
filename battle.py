import random
battle_intro = "You have entered combat"

def battle():
    print(battle_intro)
    player_health = 20
    enemy_health = random.randint(10, 20)
    heal_amount = random.randint(3, 4)
    attack_amount = random.randint(3, 6)
    print("Your enemy has " + str(enemy_health) + " health.")

    while enemy_health > 0:
        if enemy_health > 0:
            print("1. Attack\n2. Item")
            action = str(input())
            if action == "attack":
                print("You do " + str(attack_amount) + " damage.")
                enemy_health = enemy_health - attack_amount
                print("The enemy now has " + str(enemy_health) + " health.")


            else:
                print("Would you like to heal or enchant weapon?")
                item_choice = str(input())
                if item_choice == "heal":
                    print("You healed for " + str(heal_amount) + " health.")
                    new_player_health = player_health + heal_amount
                    print("You now have " + str(new_player_health) + " health.")
                else:
                    print("You now do double damage")

                    attack_amount = (attack_amount * 2)
        else:
            print("Congrats. You have defeated your enemy.")





battle()