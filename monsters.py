def monster_naming():
    import random
    monster = random.randint(1, 5)
    if monster == 1:
        return "Goblin"
    elif monster == 2:
        return "Orc"
    elif monster == 3:
        return "Thief"
    elif monster == 4:
        return "Ogre"
    elif monster == 5:
        return "Wolf"
    else:
        return "Unknown"
