from array_stack import ArrayStack

# Declare global variable at top level
MAZE = [
    ["1", "1", "1", "1", "1", "1"],
    ["e", "0", "0", "0", "0", "1"],
    ["1", "0", "1", "0", "1", "1"],
    ["1", "1", "1", "0", "0", "x"],
    ["1", "1", "1", "0", "1", "1"],
    ["1", "1", "1", "1", "1", "1"],
]
MAZE_LENGTH = len(MAZE[0])
MAZE_DEPT = len(MAZE)


def is_valid_pos(x, y) -> bool:
    if 0 <= x < MAZE_LENGTH and 0 <= y < MAZE_DEPT:
        if MAZE[y][x] == "0" or MAZE[y][x] == "x":
            return True
    return False


def find_start():
    for j in range(MAZE_LENGTH):
        for k in range(MAZE_DEPT):
            if MAZE[k][j] == "e":
                print(f"Starting point: {j, k}")
                return (j, k)


def dept_first_search() -> bool:
    print("Depth first search.")
    stack = ArrayStack(36)
    starting_point = find_start()
    stack.push(starting_point)

    while not stack.is_empty():
        curr_pos = stack.pop()
        print(curr_pos, end=" -> ")
        (x, y) = curr_pos

        if MAZE[y][x] == "x":
            return True

        MAZE[y][x] = "."
        # Move right
        if is_valid_pos(x + 1, y):
            stack.push((x + 1, y))
        # left
        if is_valid_pos(x - 1, y):
            stack.push((x - 1, y))
        # down
        if is_valid_pos(x, y + 1):
            stack.push((x, y + 1))
        # up
        if is_valid_pos(x, y - 1):
            stack.push((x, y - 1))

        print("Current stack: ", end="")
        print(stack)
    return False


if __name__ == "__main__":
    result = dept_first_search()
    if result:
        print("Success!")
    else:
        print("Failed.")
