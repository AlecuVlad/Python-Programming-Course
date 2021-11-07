import numpy as np


def print_table(mat):
    for line in mat:
        print('|'.join(map(str, line)))


def check_game_done(mat):
    for line in mat:
        if line.count('0') == len(line):
            print("Computer won!")
            return True

        if line.count('X') == len(line):
            print("Player won!")
            return True

    cpy = np.array(mat)
    for column in cpy.T:
        if np.all(column == 'X'):
            print("Player won!")
            return True
        if np.all(column == '0'):
            print("Computer won!")
            return True

    principal_diag = []
    second_diag = []
    for i in range(0, 3):
        principal_diag.append(mat[i][i])
        second_diag.append(mat[i][2 - i])

    if principal_diag.count('0') == 3 or second_diag.count('0') == 3:
        print("Computer won!")
        return True

    if principal_diag.count('X') == 3 or second_diag.count('X') == 3:
        print("Player won!")
        return True

    return False


def engine(counter, table):
    while counter != 0:
        if counter % 2 == 1:
            user_input = input("Alege o casuta: ")
            if user_input < '1' or user_input > '9' or len(user_input) != 1:
                print("Pozitie invalida!")
            else:
                position = int(user_input)
                if table[(position - 1) // 3][(position - 1) % 3] == ' ':
                    table[(position - 1) // 3][(position - 1) % 3] = 'X'
                    counter -= 1
                else:
                    print("Pozitie deja ocupata!")
        else:
            print("Alege calculatorul:")
            if table[1][1] == ' ':
                table[1][1] = '0'
            elif table[0][0] == ' ':
                table[0][0] = '0'
            elif table[0][2] == ' ':
                table[0][2] = '0'
            elif table[2][0] == ' ':
                table[2][0] = '0'
            elif table[2][2] == ' ':
                table[2][2] = '0'
            elif table[0][1] == ' ':
                table[0][1] = '0'
            elif table[1][0] == ' ':
                table[1][0] = '0'
            elif table[1][2] == ' ':
                table[1][2] = '0'
            elif table[2][1] == ' ':
                table[2][1] = '0'
            counter -= 1

        print_table(table)
        if check_game_done(table):
            return "ended"

    return "tie"


table = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

if engine(9, table) == 'tie':
    print("Tie!")
    print_table(table)
