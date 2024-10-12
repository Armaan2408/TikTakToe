def checkwin(x, y):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for pattern in win_patterns:
        if all(x[i] == 1 for i in pattern):
            return 1
        if all(y[i] == 1 for i in pattern):
            return 2
    return None

def boards(x, y):
    z = [" "] * 9
    for i in range(len(x)):
        if x[i] == 1:
            z[i] = "X"
        if y[i] == 1:
            z[i] = "O"
    print(f"{z[0]} | {z[1]} | {z[2]}")
    print("--|---|--")
    print(f"{z[3]} | {z[4]} | {z[5]}")
    print("--|---|--")
    print(f"{z[6]} | {z[7]} | {z[8]}")

def val(x, y, turn):
    while True:
        try:
            if turn % 2 == 0:
                pos = int(input("X, enter position (1-9): ")) - 1
            else:
                pos = int(input("O, enter position (1-9): ")) - 1

            if pos not in range(9):
                print("Position must be between 1 and 9.")
                continue

            if x[pos] == 0 and y[pos] == 0:
                if turn % 2 == 0:
                    x[pos] = 1
                else:
                    y[pos] = 1
                return turn + 1
            else:
                print("Spot already taken. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def main():
    x = [0] * 9
    y = [0] * 9
    turn = 0
    print("---------------------------")
    boards(x, y)
    print("---------------------------")
    while True:
        turn = val(x, y, turn)
        print("---------------------------")
        boards(x, y)
        print("---------------------------")
        win = checkwin(x, y)

        if win == 1:
            print("Player X won!")
            boards(x, y)
            print("---------------------------")
            break
        elif win == 2:
            print("Player O won!")
            boards(x, y)
            print("---------------------------")
            break
        elif sum(x) + sum(y) == 9:
            print("It's a tie!")
            boards(x, y)
            print("---------------------------")
            break

if __name__ == "__main__":
    main()
