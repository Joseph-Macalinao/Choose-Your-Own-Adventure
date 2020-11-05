def store():
    print("Welcome to the store. How can I help you?\nWeapons\nArmor\nPotions")
    store_choice = str(input())
    if store_choice == "weapons":
        print("What weapon would you like:\nBattle Axe\nFlail\nGiant Club")
        weapon_choice = str(input())
        print("You now have a " + weapon_choice)

store()