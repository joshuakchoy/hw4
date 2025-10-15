def cacti_number(plot: list) -> int:
    if not isinstance(plot, list):
        raise TypeError
    counter = 0
    col = len(plot)
    for y in range(0, col): 
        row = len(plot[y])
        for x in range(0, row): 
            if plot[y][x] == 0: 
                # check adjacent slots
                empty = x - 1 < 0 or plot[y][x - 1] == 0
                empty = empty and (x + 1 >= row or plot[y][x + 1] == 0)
                empty = empty and (y - 1 < 0 or plot[y - 1][x] == 0)
                empty = empty and (y + 1 >= col or plot[y + 1][x] == 0)
                if empty:
                    counter += 1
                    plot[y][x] = 1
    return counter