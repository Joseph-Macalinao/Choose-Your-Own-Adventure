import random


def out_of_battle():
    print("You are now walking down a road. What do you do? \n1. Continue to walk \n2. Rest\n3. Go Home\n4. Store")
    what_happens_action = str(input())
    if what_happens_action == "1":
        what_happens = random.randint(1, 5)
        if what_happens == 1:
            print("You continue to walk.")
            out_of_battle()
        else:
            print("You see a figure coming closer to you.")
            from battle_backup import battle
            battle()
    elif what_happens_action == "2":
        print("You rested. You now have full health.")
        out_of_battle()
    elif what_happens_action =="3":
        print("You went home. Do you go back out")
        decision = str(input())
        if decision == "yes":
            out_of_battle()
        else:
            print("You go to sleep.")
            from game_part_1 import intro
            intro()
    elif what_happens_action =="4":
        from store import store
        store()
    else:
        out_of_battle()

out_of_battle()
