snake = {17:7, 54:34, 62:19, 64:60, 87:36, 92:73, 95:75, 98:79}

def snakes(x):
    if x in snake.keys():
        final_val = snake[x]
        return final_val
    return x

