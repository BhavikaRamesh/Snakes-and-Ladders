from snakes import *
from ladders import *
def snake_ladder(player_name, current_value, dice_value):
    MAX_VAL = 100
    old_value = current_value
    current_value = current_value + dice_value
    if current_value > MAX_VAL:
        print("You need " + str(MAX_VAL - old_value) + "to win this game.Keep trying.")
        return old_value
    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snake:
        final_value = snakes(current_value)
        print("\n" + player_name + " moved from " + str(current_value) + " to " + str(final_value))
    elif current_value in step:
        final_value = ladders(current_value)
        print("\n" + player_name + " moved from " + str(current_value) + " to " + str(final_value))
    else:
        final_value = current_value
    return final_value


