def roll_call_dwarves(dwarfs):
    i = 1
    for dwarf in dwarfs:
        print(f"{i}. {dwarf}")
        i += 1

def summon_captain_planet(planeteer_calls):
    new_array = []
    i = 0
    while i < len(planeteer_calls):
        new_array.append(planeteer_calls[i].title() + "!")
        i += 1
    return(new_array)

def long_planeteer_calls(planeteer_calls):
    i = -1
    while i < len(planeteer_calls):
        if(len(planeteer_calls[i]) > 4):
            return True
        else:
            i += 1
    return False

def find_the_cheese(ingr):
    i = 0
    while i < len(ingr):
        if(ingr[i] == "cheddar"):
            return "cheddar"
        elif(ingr[i] == "gouda"):
            return "gouda"
        elif(ingr[i] == "camembert"):
            return "camembert"
        else:
            i += 1
    return None
print(find_the_cheese(["tomato soup", "cheddar", "oyster crackers", "gouda"]))