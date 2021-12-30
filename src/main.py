starting_grid = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def display_grid(grid):
    for x in range(len(grid)):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - - - ")

        for y in range(len(grid[0])):
            if y % 3 == 0 and y != 0:
                print(" | ", end="")

            if y == 8:
                print(grid[x][y])
            else:
                print(str(grid[x][y]) + " ", end="")



def locate_blank(grid):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 0:
                return (x, y)  # row, col

    return None
