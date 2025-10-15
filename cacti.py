def cacti_number(func):
    def wrapper(plot):

        rows = len(plot)
        cols = len(plot[0])
        counter = 0

        temp = [row[:] for row in plot]

        for i in range(rows):
            for j in range(cols):
                if temp[i][j] == 0:
                    up = i == 0 or temp[i - 1][j] == 0
                    down = i == rows - 1 or temp[i + 1][j] == 0
                    left = j == 0 or temp[i][j - 1] == 0
                    right = j == cols - 1 or temp[i][j + 1] == 0

                    if up and down and left and right:
                        temp[i][j] = 1
                        counter += 1

        func(plot)
        return counter
    return wrapper
