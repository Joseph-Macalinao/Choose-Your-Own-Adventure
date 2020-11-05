
def intro():
    print("Hello Kind Traveler. What would you like to do?\nGo out\nStay in")
    intro_decision = str(input())
    if intro_decision == "go out":
        from non_battle import out_of_battle
        out_of_battle()
    else:
        print("Why did you even launch this program then you idiot?")
        return 0
intro()