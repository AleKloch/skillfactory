def game():
    print(" ")
    print("Узнаем кто тут сильный?")
    print("Поиграем в крестики-нолики")
    print(" ")
    print("формат ввода координат X и Y, где")
    print("-X- номер строки")
    print("-Y- номер столба")
def show():
    print()
    print("   | 0 | 1 | 2 |")
    print("_______________")
    for i, row in enumerate(field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print("_______________")
    print()
def ask():
    while True:
        cords = input("Ваш ход, Маэстро :-)").split()
        if len(cords) != 2:
            print("Введи 2 числа!")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числовые значения!")
            continue

        x, y = int(x), int(y)

        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == " ":
                return x, y
            else:
                print("Это место занято, Ковбой!")
                continue
        else:
            print("Координаты вне диапазона")
            continue
def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)),
                ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cords in win_cord:
        symbols = []
        for a in cords:
            symbols.append(field[a[0]][a[1]])
        if symbols == ["0","0","0"]:
            print("Выйграл нолик!")
            return True
        if symbols == ["x","x","x"]:
            print("Выйграл крестик!")
            return True
    return False
game()
field = [[" "]*3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "x"
    else:
        field[x][y] = "0"

    if check_win():
        show()
        print("Поздравляю, Ковбой!")
        break

    if count == 9:
        show()
        print("Ничья. Играй жестче!")
        break





