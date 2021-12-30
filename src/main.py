grid = [
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

def solve_grid(grid):
    locate = locate_blank(grid)
    if not locate:
        return True
    else:
        row, column = locate
    for x in range(1, 10):
        if validate_grid(grid, x, (row, column)):
            grid[row][column] = x

            if solve_grid(grid):
                return True

            grid[row][column] = 0

    return False



def validate_grid(grid, number, position):
    # Check row
    for x in range(len(grid[0])):
        if grid[position[0]][x] == number and position[1] != x:
            return False

    # Check column
    for y in range(len(grid)):
        if grid[x][position[1]] == number and position[0] != y:
            return False

    # Check box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for x in range(box_y * 3, box_y * 3 + 3):
        for y in range(box_x * 3, box_x * 3 + 3):
            if grid[x][y] == number and (x, y) != position:
                return False

    return True

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

display_grid(grid)
solve_grid(grid)
print("")
print("")
print("")
display_grid(grid)