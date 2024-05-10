import random, colorama, time
from colorama import Fore, Back, Style

correct_lists = []

# colorful askII
print(Fore.RED)
print("  __  __           _                      _           _ ")
print(" |  \/  |         | |                    (_)         | |")
print(" | \  / | __ _ ___| |_ ___ _ __ _ __ ___  _ _ __   __| |")
print(" | |\/| |/ _` / __| __/ _ \ '__| '_ ` _ \| | '_ \ / _` |")
print(" | |  | | (_| \__ \ ||  __/ |  | | | | | | | | | | (_| |")
print(" |_|  |_|\__,_|___/\__\___|_|  |_| |_| |_|_|_| |_|\__,_|")
print(Style.RESET_ALL)

print("Make screen as large as possible")

time.sleep(1)

menu = 0
# menu
while (menu != 2):
    print(Fore.RED)
    print(
        " _ __ ___   ___ _ __  _   _ \n| '_ ` _ \ / _ \ '_ \| | | |\n| | | | | |  __/ | | | |_| |\n|_| |_| |_|\___|_| |_|\__,_|")
    print(Style.RESET_ALL)
    print("\n\n1)rules\n2)play")
    menu = int(input(":"))

    if (menu == 1):
        print(Fore.RED)
        print(
            "            _           \n           | |          \n _ __ _   _| | ___  ___ \n| '__| | | | |/ _ \/ __|\n| |  | |_| | |  __/\__ \ \n|_|   \__,_|_|\___||___/")

        print(Style.RESET_ALL)

        print(
            "\n\nThe computer has selected a secret combination of 3,4,5, or 6 colored\n numbers/pegs and you have to guess that combination in 10 or fewer tries to win.\nFor each guess a 'X' indicates that one of your numbers is the right\n number in the right position.\nAn 'O' indicates that one of your numbers is the right number in the wrong position.")
        print("\n")
        print("There is single player and two player modes.")
        print("\nIn single player there is:\n[N]ovice,[I]ntermediate,and [E]xpert")
        print("\nNovice has numbers 1-6 with no repeats")
        print("\nIntermediate has numbers 1-6 with repeats")
        print("\nExpert has numbers 1-8 with repeats")
        print("\n\nFor Two player the players chose a code of 4 numbers")
        print("Then take turns to guess eachothers code")

print("\n\n[S]ingle player or [T]wo player?")
player = str(input(":")).lower()
# solo play
if (player == "s"):
    game_board_guess = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: []
    }

    reaction_x = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: []
    }

    reaction_o = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: []
    }

    number_color = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],

    }

    # play starts here :)

    print("\n\nwhat is your name?")
    name = str(input(":"))

    print("\n\nHow long do you want your code?")
    length = int(input("[3],[4],[5], or [6] digets long?\n"))

    for c in range(1, 11):
        for d in range(length):
            game_board_guess[c].append(0)
            number_color[c].append("")

    print("\n\nwhat difficulty do you want?\n[N]ovice\n[I]ntermediate\n[E]xpert ")
    difficulty = str(input(":")).lower()

    if (difficulty == "n"):
        number_choices = ["1", "2", "3", "4", "5", "6"]
        for c in range(length):
            randomx = random.choice(number_choices)
            correct_lists.append(randomx)
            number_choices.remove(randomx)
        number_choices = ["  1", "2", "3", "4", "5", "6"]

    if (difficulty == "i"):
        number_choices = ["1", "2", "3", "4", "5", "6"]
        for c in range(length):
            randomx = random.choice(number_choices)
            correct_lists.append(randomx)
        number_choices = ["  1", "2", "3", "4", "5", "6"]

    if (difficulty == "e"):
        number_choices = ["1", "2", "3", "4", "5", "6", "7", "8"]
        for c in range(length):
            randomx = random.choice(number_choices)
            correct_lists.append(randomx)

    for c in range(1, 11):

        if (length == 3):
            print("\n\n---------------------\n| Possible Answers  |\n  ", *number_choices)
            print("| ", Back.BLACK, "X", Style.RESET_ALL, " = Right Spot    | \n| ", Back.WHITE, "O", Style.RESET_ALL,
                  " = In Combination| ", "  \n---------------------", sep="")
            print("#1  | ", number_color[1][0], game_board_guess[1][0], Style.RESET_ALL, " | ", number_color[1][1],
                  game_board_guess[1][1], Style.RESET_ALL, " | ", number_color[1][2], game_board_guess[1][2],
                  Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[1], Back.WHITE, *reaction_o[1], Style.RESET_ALL,
                  sep="")
            print("---------------------\n#2  | ", number_color[2][0], game_board_guess[2][0], Style.RESET_ALL, " | ",
                  number_color[2][1], game_board_guess[2][1], Style.RESET_ALL, " | ", number_color[2][2],
                  game_board_guess[2][2], Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[2], Back.WHITE,
                  *reaction_o[2], Style.RESET_ALL, sep="")
            print("---------------------\n#3  | ", number_color[3][0], game_board_guess[3][0], Style.RESET_ALL, " | ",
                  number_color[3][1], game_board_guess[3][1], Style.RESET_ALL, " | ", number_color[3][2],
                  game_board_guess[3][2], Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[3], Back.WHITE,
                  *reaction_o[3], Style.RESET_ALL, sep="")
            print("---------------------\n#4  | ", number_color[4][0], game_board_guess[4][0], Style.RESET_ALL, " | ",
                  number_color[4][1], game_board_guess[4][1], Style.RESET_ALL, " | ", number_color[4][2],
                  game_board_guess[4][2], Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[4], Back.WHITE,
                  *reaction_o[4], Style.RESET_ALL, sep="")
            print("---------------------\n#5  | ", number_color[5][0], game_board_guess[5][0], Style.RESET_ALL, " | ",
                  number_color[5][1], game_board_guess[5][1], Style.RESET_ALL, " | ", number_color[5][2],
                  game_board_guess[5][2], Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[5], Back.WHITE,
                  *reaction_o[5], Style.RESET_ALL, sep="")
            print("---------------------\n#6  | ", number_color[6][0], game_board_guess[6][0], Style.RESET_ALL, " | ",
                  number_color[6][1], game_board_guess[6][1], Style.RESET_ALL, " | ", number_color[6][2],
                  game_board_guess[6][2], Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[6], Back.WHITE,
                  *reaction_o[6], Style.RESET_ALL, sep="")
            print("---------------------\n#7  | ", number_color[7][0], game_board_guess[7][0], Style.RESET_ALL, " | ",
                  number_color[7][1], game_board_guess[7][1], Style.RESET_ALL, " | ", number_color[7][2],
                  game_board_guess[7][2], Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[7], Back.WHITE,
                  *reaction_o[7], Style.RESET_ALL, sep="")
            print("---------------------\n#8  | ", number_color[8][0], game_board_guess[8][0], Style.RESET_ALL, " | ",
                  number_color[8][1], game_board_guess[8][1], Style.RESET_ALL, " | ", number_color[8][2],
                  game_board_guess[8][2], Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[8], Back.WHITE,
                  *reaction_o[8], Style.RESET_ALL, sep="")
            print("---------------------\n#9  | ", number_color[9][0], game_board_guess[9][0], Style.RESET_ALL, " | ",
                  number_color[9][1], game_board_guess[9][1], Style.RESET_ALL, " | ", number_color[9][2],
                  game_board_guess[9][2], Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[9], Back.WHITE,
                  *reaction_o[9], Style.RESET_ALL, sep="")
            print("---------------------\n#10 | ", number_color[10][0], game_board_guess[10][0], Style.RESET_ALL, " | ",
                  number_color[10][1], game_board_guess[10][1], Style.RESET_ALL, " | ", number_color[10][2],
                  game_board_guess[10][2], Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[10], Back.WHITE,
                  *reaction_o[10], Style.RESET_ALL, "\n---------------------", sep="")

        if (length == 4):
            print("\n\n---------------------\n| Possible Answers  |\n  ", *number_choices)
            print("| ", Back.BLACK, "X", Style.RESET_ALL, " = Right Spot    | \n| ", Back.WHITE, "O", Style.RESET_ALL,
                  " = In Combination| ", "  \n---------------------", sep="")
            print("#1  | ", number_color[1][0], game_board_guess[1][0], Style.RESET_ALL, " | ", number_color[1][1],
                  game_board_guess[1][1], Style.RESET_ALL, " | ", number_color[1][2], game_board_guess[1][2],
                  Style.RESET_ALL, " | ", number_color[1][3], game_board_guess[1][3], Style.RESET_ALL, " | ",
                  Back.BLACK, *reaction_x[1], Back.WHITE, *reaction_o[1], Style.RESET_ALL, sep="")
            print("---------------------\n#2  | ", number_color[2][0], game_board_guess[2][0], Style.RESET_ALL, " | ",
                  number_color[2][1], game_board_guess[2][1], Style.RESET_ALL, " | ", number_color[2][2],
                  game_board_guess[2][2], Style.RESET_ALL, " | ", number_color[2][3], game_board_guess[2][3],
                  Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[2], Back.WHITE, *reaction_o[2], Style.RESET_ALL,
                  sep="")
            print("---------------------\n#3  | ", number_color[3][0], game_board_guess[3][0], Style.RESET_ALL, " | ",
                  number_color[3][1], game_board_guess[3][1], Style.RESET_ALL, " | ", number_color[3][2],
                  game_board_guess[3][2], Style.RESET_ALL, " | ", number_color[3][3], game_board_guess[3][3],
                  Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[3], Back.WHITE, *reaction_o[3], Style.RESET_ALL,
                  sep="")
            print("---------------------\n#4  | ", number_color[4][0], game_board_guess[4][0], Style.RESET_ALL, " | ",
                  number_color[4][1], game_board_guess[4][1], Style.RESET_ALL, " | ", number_color[4][2],
                  game_board_guess[4][2], Style.RESET_ALL, " | ", number_color[4][3], game_board_guess[4][3],
                  Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[4], Back.WHITE, *reaction_o[4], Style.RESET_ALL,
                  sep="")
            print("---------------------\n#5  | ", number_color[5][0], game_board_guess[5][0], Style.RESET_ALL, " | ",
                  number_color[5][1], game_board_guess[5][1], Style.RESET_ALL, " | ", number_color[5][2],
                  game_board_guess[5][2], Style.RESET_ALL, " | ", number_color[5][3], game_board_guess[5][3],
                  Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[5], Back.WHITE, *reaction_o[5], Style.RESET_ALL,
                  sep="")
            print("---------------------\n#6  | ", number_color[6][0], game_board_guess[6][0], Style.RESET_ALL, " | ",
                  number_color[6][1], game_board_guess[6][1], Style.RESET_ALL, " | ", number_color[6][2],
                  game_board_guess[6][2], Style.RESET_ALL, " | ", number_color[6][3], game_board_guess[6][3],
                  Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[6], Back.WHITE, *reaction_o[6], Style.RESET_ALL,
                  sep="")
            print("---------------------\n#7  | ", number_color[7][0], game_board_guess[7][0], Style.RESET_ALL, " | ",
                  number_color[7][1], game_board_guess[7][1], Style.RESET_ALL, " | ", number_color[7][2],
                  game_board_guess[7][2], Style.RESET_ALL, " | ", number_color[7][3], game_board_guess[7][3],
                  Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[7], Back.WHITE, *reaction_o[7], Style.RESET_ALL,
                  sep="")
            print("---------------------\n#8  | ", number_color[8][0], game_board_guess[8][0], Style.RESET_ALL, " | ",
                  number_color[8][1], game_board_guess[8][1], Style.RESET_ALL, " | ", number_color[8][2],
                  game_board_guess[8][2], Style.RESET_ALL, " | ", number_color[8][3], game_board_guess[8][3],
                  Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[8], Back.WHITE, *reaction_o[8], Style.RESET_ALL,
                  sep="")
            print("---------------------\n#9  | ", number_color[9][0], game_board_guess[9][0], Style.RESET_ALL, " | ",
                  number_color[9][1], game_board_guess[9][1], Style.RESET_ALL, " | ", number_color[9][2],
                  game_board_guess[9][2], Style.RESET_ALL, " | ", number_color[9][3], game_board_guess[9][3],
                  Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[9], Back.WHITE, *reaction_o[9], Style.RESET_ALL,
                  sep="")
            print("---------------------\n#10 | ", number_color[10][0], game_board_guess[10][0], Style.RESET_ALL, " | ",
                  number_color[10][1], game_board_guess[10][1], Style.RESET_ALL, " | ", number_color[10][2],
                  game_board_guess[10][2], Style.RESET_ALL, " | ", number_color[10][3], game_board_guess[10][3],
                  Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[10], Back.WHITE, *reaction_o[10], Style.RESET_ALL,
                  "\n---------------------", sep="")

        if (length == 5):
            print("\n\n---------------------\n| Possible Answers  |\n  ", *number_choices)
            print("| ", Back.BLACK, "X", Style.RESET_ALL, " = Right Spot    | \n| ", Back.WHITE, "O", Style.RESET_ALL,
                  " = In Combination| ", "  \n-------------------------", sep="")
            print("#1  | ", number_color[1][0], game_board_guess[1][0], Style.RESET_ALL, " | ", number_color[1][1],
                  game_board_guess[1][1], Style.RESET_ALL, " | ", number_color[1][2], game_board_guess[1][2],
                  Style.RESET_ALL, " | ", number_color[1][3], game_board_guess[1][3], Style.RESET_ALL, " | ",
                  number_color[1][4], game_board_guess[1][4], Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[1],
                  Back.WHITE, *reaction_o[1], Style.RESET_ALL, sep="")
            print("-------------------------\n#2  | ", number_color[2][0], game_board_guess[2][0], Style.RESET_ALL,
                  " | ", number_color[2][1], game_board_guess[2][1], Style.RESET_ALL, " | ", number_color[2][2],
                  game_board_guess[2][2], Style.RESET_ALL, " | ", number_color[2][3], game_board_guess[2][3],
                  Style.RESET_ALL, " | ", number_color[2][4], game_board_guess[2][4], Style.RESET_ALL, " | ",
                  Back.BLACK, *reaction_x[2], Back.WHITE, *reaction_o[2], Style.RESET_ALL, sep="")
            print("-------------------------\n#3  | ", number_color[3][0], game_board_guess[3][0], Style.RESET_ALL,
                  " | ", number_color[3][1], game_board_guess[3][1], Style.RESET_ALL, " | ", number_color[3][2],
                  game_board_guess[3][2], Style.RESET_ALL, " | ", number_color[3][3], game_board_guess[3][3],
                  Style.RESET_ALL, " | ", number_color[3][4], game_board_guess[3][4], Style.RESET_ALL, " | ",
                  Back.BLACK, *reaction_x[3], Back.WHITE, *reaction_o[3], Style.RESET_ALL, sep="")
            print("-------------------------\n#4  | ", number_color[4][0], game_board_guess[4][0], Style.RESET_ALL,
                  " | ", number_color[4][1], game_board_guess[4][1], Style.RESET_ALL, " | ", number_color[4][2],
                  game_board_guess[4][2], Style.RESET_ALL, " | ", number_color[4][3], game_board_guess[4][3],
                  Style.RESET_ALL, " | ", number_color[4][4], game_board_guess[4][4], Style.RESET_ALL, " | ",
                  Back.BLACK, *reaction_x[4], Back.WHITE, *reaction_o[4], Style.RESET_ALL, sep="")
            print("-------------------------\n#5  | ", number_color[5][0], game_board_guess[5][0], Style.RESET_ALL,
                  " | ", number_color[5][1], game_board_guess[5][1], Style.RESET_ALL, " | ", number_color[5][2],
                  game_board_guess[5][2], Style.RESET_ALL, " | ", number_color[5][3], game_board_guess[5][3],
                  Style.RESET_ALL, " | ", number_color[5][4], game_board_guess[5][4], Style.RESET_ALL, " | ",
                  Back.BLACK, *reaction_x[5], Back.WHITE, *reaction_o[5], Style.RESET_ALL, sep="")
            print("-------------------------\n#6  | ", number_color[6][0], game_board_guess[6][0], Style.RESET_ALL,
                  " | ", number_color[6][1], game_board_guess[6][1], Style.RESET_ALL, " | ", number_color[6][2],
                  game_board_guess[6][2], Style.RESET_ALL, " | ", number_color[6][3], game_board_guess[6][3],
                  Style.RESET_ALL, " | ", number_color[6][4], game_board_guess[6][4], Style.RESET_ALL, " | ",
                  Back.BLACK, *reaction_x[6], Back.WHITE, *reaction_o[6], Style.RESET_ALL, sep="")
            print("-------------------------\n#7  | ", number_color[7][0], game_board_guess[7][0], Style.RESET_ALL,
                  " | ", number_color[7][1], game_board_guess[7][1], Style.RESET_ALL, " | ", number_color[7][2],
                  game_board_guess[7][2], Style.RESET_ALL, " | ", number_color[7][3], game_board_guess[7][3],
                  Style.RESET_ALL, " | ", number_color[7][4], game_board_guess[7][4], Style.RESET_ALL, " | ",
                  Back.BLACK, *reaction_x[7], Back.WHITE, *reaction_o[7], Style.RESET_ALL, sep="")
            print("-------------------------\n#8  | ", number_color[8][0], game_board_guess[8][0], Style.RESET_ALL,
                  " | ", number_color[8][1], game_board_guess[8][1], Style.RESET_ALL, " | ", number_color[8][2],
                  game_board_guess[8][2], Style.RESET_ALL, " | ", number_color[8][3], game_board_guess[8][3],
                  Style.RESET_ALL, " | ", number_color[8][4], game_board_guess[8][4], Style.RESET_ALL, " | ",
                  Back.BLACK, *reaction_x[8], Back.WHITE, *reaction_o[8], Style.RESET_ALL, sep="")
            print("-------------------------\n#9  | ", number_color[9][0], game_board_guess[9][0], Style.RESET_ALL,
                  " | ", number_color[9][1], game_board_guess[9][1], Style.RESET_ALL, " | ", number_color[9][2],
                  game_board_guess[9][2], Style.RESET_ALL, " | ", number_color[9][3], game_board_guess[9][3],
                  Style.RESET_ALL, " | ", number_color[9][4], game_board_guess[9][4], Style.RESET_ALL, " | ",
                  Back.BLACK, *reaction_x[9], Back.WHITE, *reaction_o[9], Style.RESET_ALL, sep="")
            print("-------------------------\n#10 | ", number_color[10][0], game_board_guess[10][0], Style.RESET_ALL,
                  " | ", number_color[10][1], game_board_guess[10][1], Style.RESET_ALL, " | ", number_color[10][2],
                  game_board_guess[10][2], Style.RESET_ALL, " | ", number_color[10][3], game_board_guess[10][3],
                  Style.RESET_ALL, " | ", number_color[10][4], game_board_guess[10][4], Style.RESET_ALL, " | ",
                  Back.BLACK, *reaction_x[10], Back.WHITE, *reaction_o[10], Style.RESET_ALL,
                  "\n-------------------------", sep="")

        if (length == 6):
            print("\n\n---------------------\n| Possible Answers  |\n  ", *number_choices)
            print("| ", Back.BLACK, "X", Style.RESET_ALL, " = Right Spot    | \n| ", Back.WHITE, "O", Style.RESET_ALL,
                  " = In Combination| ", "  \n-----------------------------", sep="")
            print("#1  | ", number_color[1][0], game_board_guess[1][0], Style.RESET_ALL, " | ", number_color[1][1],
                  game_board_guess[1][1], Style.RESET_ALL, " | ", number_color[1][2], game_board_guess[1][2],
                  Style.RESET_ALL, " | ", number_color[1][3], game_board_guess[1][3], Style.RESET_ALL, " | ",
                  number_color[1][4], game_board_guess[1][4], Style.RESET_ALL, " | ", number_color[1][5],
                  game_board_guess[1][5], Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[1], Back.WHITE,
                  *reaction_o[1], Style.RESET_ALL, sep="")
            print("-----------------------------\n#2  | ", number_color[2][0], game_board_guess[2][0], Style.RESET_ALL,
                  " | ", number_color[2][1], game_board_guess[2][1], Style.RESET_ALL, " | ", number_color[2][2],
                  game_board_guess[2][2], Style.RESET_ALL, " | ", number_color[2][3], game_board_guess[2][3],
                  Style.RESET_ALL, " | ", number_color[2][4], game_board_guess[2][4], Style.RESET_ALL, " | ",
                  number_color[2][5], game_board_guess[2][5], Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[2],
                  Back.WHITE, *reaction_o[2], Style.RESET_ALL, sep="")
            print("-----------------------------\n#3  | ", number_color[3][0], game_board_guess[3][0], Style.RESET_ALL,
                  " | ", number_color[3][1], game_board_guess[3][1], Style.RESET_ALL, " | ", number_color[3][2],
                  game_board_guess[3][2], Style.RESET_ALL, " | ", number_color[3][3], game_board_guess[3][3],
                  Style.RESET_ALL, " | ", number_color[3][4], game_board_guess[3][4], Style.RESET_ALL, " | ",
                  number_color[3][5], game_board_guess[3][5], Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[3],
                  Back.WHITE, *reaction_o[3], Style.RESET_ALL, sep="")
            print("-----------------------------\n#4  | ", number_color[4][0], game_board_guess[4][0], Style.RESET_ALL,
                  " | ", number_color[4][1], game_board_guess[4][1], Style.RESET_ALL, " | ", number_color[4][2],
                  game_board_guess[4][2], Style.RESET_ALL, " | ", number_color[4][3], game_board_guess[4][3],
                  Style.RESET_ALL, " | ", number_color[4][4], game_board_guess[4][4], Style.RESET_ALL, " | ",
                  number_color[4][5], game_board_guess[4][5], Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[4],
                  Back.WHITE, *reaction_o[4], Style.RESET_ALL, sep="")
            print("-----------------------------\n#5  | ", number_color[5][0], game_board_guess[5][0], Style.RESET_ALL,
                  " | ", number_color[5][1], game_board_guess[5][1], Style.RESET_ALL, " | ", number_color[5][2],
                  game_board_guess[5][2], Style.RESET_ALL, " | ", number_color[5][3], game_board_guess[5][3],
                  Style.RESET_ALL, " | ", number_color[5][4], game_board_guess[5][4], Style.RESET_ALL, " | ",
                  number_color[5][5], game_board_guess[5][5], Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[5],
                  Back.WHITE, *reaction_o[5], Style.RESET_ALL, sep="")
            print("-----------------------------\n#6  | ", number_color[6][0], game_board_guess[6][0], Style.RESET_ALL,
                  " | ", number_color[6][1], game_board_guess[6][1], Style.RESET_ALL, " | ", number_color[6][2],
                  game_board_guess[6][2], Style.RESET_ALL, " | ", number_color[6][3], game_board_guess[6][3],
                  Style.RESET_ALL, " | ", number_color[6][4], game_board_guess[6][4], Style.RESET_ALL, " | ",
                  number_color[6][5], game_board_guess[6][5], Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[6],
                  Back.WHITE, *reaction_o[6], Style.RESET_ALL, sep="")
            print("-----------------------------\n#7  | ", number_color[7][0], game_board_guess[7][0], Style.RESET_ALL,
                  " | ", number_color[7][1], game_board_guess[7][1], Style.RESET_ALL, " | ", number_color[7][2],
                  game_board_guess[7][2], Style.RESET_ALL, " | ", number_color[7][3], game_board_guess[7][3],
                  Style.RESET_ALL, " | ", number_color[7][4], game_board_guess[7][4], Style.RESET_ALL, " | ",
                  number_color[7][5], game_board_guess[7][5], Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[7],
                  Back.WHITE, *reaction_o[7], Style.RESET_ALL, sep="")
            print("-----------------------------\n#8  | ", number_color[8][0], game_board_guess[8][0], Style.RESET_ALL,
                  " | ", number_color[8][1], game_board_guess[8][1], Style.RESET_ALL, " | ", number_color[8][2],
                  game_board_guess[8][2], Style.RESET_ALL, " | ", number_color[8][3], game_board_guess[8][3],
                  Style.RESET_ALL, " | ", number_color[8][4], game_board_guess[8][4], Style.RESET_ALL, " | ",
                  number_color[8][5], game_board_guess[8][5], Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[8],
                  Back.WHITE, *reaction_o[8], Style.RESET_ALL, sep="")
            print("-----------------------------\n#9  | ", number_color[9][0], game_board_guess[9][0], Style.RESET_ALL,
                  " | ", number_color[9][1], game_board_guess[9][1], Style.RESET_ALL, " | ", number_color[9][2],
                  game_board_guess[9][2], Style.RESET_ALL, " | ", number_color[9][3], game_board_guess[9][3],
                  Style.RESET_ALL, " | ", number_color[9][4], game_board_guess[9][4], Style.RESET_ALL, " | ",
                  number_color[9][5], game_board_guess[9][5], Style.RESET_ALL, " | ", Back.BLACK, *reaction_x[9],
                  Back.WHITE, *reaction_o[9], Style.RESET_ALL, sep="")
            print("-----------------------------\n#10 | ", number_color[10][0], game_board_guess[10][0],
                  Style.RESET_ALL, " | ", number_color[10][1], game_board_guess[10][1], Style.RESET_ALL, " | ",
                  number_color[10][2], game_board_guess[10][2], Style.RESET_ALL, " | ", number_color[10][3],
                  game_board_guess[10][3], Style.RESET_ALL, " | ", number_color[10][4], game_board_guess[10][4],
                  Style.RESET_ALL, " | ", number_color[10][5], game_board_guess[10][5], Style.RESET_ALL, " | ",
                  Back.BLACK, *reaction_x[10], Back.WHITE, *reaction_o[10], Style.RESET_ALL,
                  "\n-----------------------------", sep="")

        print("\n\nplease give me a Combination of", length, "numbers")

        guess = str(input(":"))
        game_board_guess[c] = list(guess)
        correct_lists_copy = list(correct_lists)

        # the X's and O's
        for d in range(0, length):
            if (game_board_guess[c][d] == correct_lists_copy[d]):
                reaction_x[c].append("X")
                correct_lists_copy[d] = "X"

        for d in range(0, length):
            if (game_board_guess[c][d] in correct_lists_copy):
                reaction_o[c].append("O")
                correct_lists_copy[correct_lists_copy.index(game_board_guess[c][d])] = "O"

        # color
        for d in range(0, length):
            if (game_board_guess[c][d] == "1"):
                number_color[c][d] = Fore.YELLOW

            if (game_board_guess[c][d] == "2"):
                number_color[c][d] = Fore.BLUE

            if (game_board_guess[c][d] == "3"):
                number_color[c][d] = Fore.GREEN

            if (game_board_guess[c][d] == "4"):
                number_color[c][d] = Fore.CYAN

            if (game_board_guess[c][d] == "5"):
                number_color[c][d] = Fore.RED

            if (game_board_guess[c][d] == "6"):
                number_color[c][d] = Back.RED

            if (game_board_guess[c][d] == "7"):
                number_color[c][d] = Back.MAGENTA

            if (game_board_guess[c][d] == "8"):
                number_color[c][d] = Back.BLUE

        if (game_board_guess[c] == correct_lists):
            break

    if (game_board_guess[c] == correct_lists):
        print("\n\nCongrats ", name, " you were correct the answer was indeed ", *correct_lists, "!!!", sep="")

    if (game_board_guess[c] != correct_lists):
        print("\n\nSorry ", name, " you were not correct the answer was  ", *correct_lists, "!!!", sep="")

# two player
if (player == "t"):
    print("\n\nare you playing 1-[6] or 1-[8]")
    difficulty = str(input(":")).lower()

    if (difficulty == "6"):
        number_choices = ["  1", "2", "3", "4", "5", "6"]
        code_choices = "From 1 to 6"

    if (difficulty == "8"):
        number_choices = ["1", "2", "3", "4", "5", "6", "7", "8"]
        code_choices = "From 1 to 8"

    print("\n\nWho will be player 1? (please give me your name)")
    player_1 = str(input(":"))

    print("\n\nWho will be player 2? (please give me your name)")
    player_2 = str(input(":"))

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(player_1, "What is your digit code?", code_choices)
    player_2_code = list(str(input(":")))

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(player_2, "What is your 4 digit code?", code_choices)
    player_1_code = list(str(input(":")))

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    game_board_guess_1 = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: []
    }

    reaction_x_1 = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: []
    }

    reaction_o_1 = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: []
    }

    number_color_1 = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],

    }

    game_board_guess_2 = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: []
    }

    reaction_x_2 = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: []
    }

    reaction_o_2 = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: []
    }

    number_color_2 = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],

    }

    for c in range(1, 11):
        for d in range(4):
            game_board_guess_1[c].append(0)
            number_color_1[c].append("")

    for c in range(1, 11):
        for d in range(4):
            game_board_guess_2[c].append(0)
            number_color_2[c].append("")

    for c in range(1, 11):

        # player 1
        print("\n\n---------------------\n| Possible Answers  |\n  ", *number_choices, "\n", Back.RED, player_1,
              Style.RESET_ALL)
        print("| ", Back.BLACK, "X", Style.RESET_ALL, " = Right Spot    | \n| ", Back.WHITE, "O", Style.RESET_ALL,
              " = In Combination| ", "  \n---------------------", sep="")
        print("#1  | ", number_color_1[1][0], game_board_guess_1[1][0], Style.RESET_ALL, " | ", number_color_1[1][1],
              game_board_guess_1[1][1], Style.RESET_ALL, " | ", number_color_1[1][2], game_board_guess_1[1][2],
              Style.RESET_ALL, " | ", number_color_1[1][3], game_board_guess_1[1][3], Style.RESET_ALL, " | ",
              Back.BLACK, *reaction_x_1[1], Back.WHITE, *reaction_o_1[1], Style.RESET_ALL, sep="")
        print("---------------------\n#2  | ", number_color_1[2][0], game_board_guess_1[2][0], Style.RESET_ALL, " | ",
              number_color_1[2][1], game_board_guess_1[2][1], Style.RESET_ALL, " | ", number_color_1[2][2],
              game_board_guess_1[2][2], Style.RESET_ALL, " | ", number_color_1[2][3], game_board_guess_1[2][3],
              Style.RESET_ALL, " | ", Back.BLACK, *reaction_x_1[2], Back.WHITE, *reaction_o_1[2], Style.RESET_ALL,
              sep="")
        print("---------------------\n#3  | ", number_color_1[3][0], game_board_guess_1[3][0], Style.RESET_ALL, " | ",
              number_color_1[3][1], game_board_guess_1[3][1], Style.RESET_ALL, " | ", number_color_1[3][2],
              game_board_guess_1[3][2], Style.RESET_ALL, " | ", number_color_1[3][3], game_board_guess_1[3][3],
              Style.RESET_ALL, " | ", Back.BLACK, *reaction_x_1[3], Back.WHITE, *reaction_o_1[3], Style.RESET_ALL,
              sep="")
        print("---------------------\n#4  | ", number_color_1[4][0], game_board_guess_1[4][0], Style.RESET_ALL, " | ",
              number_color_1[4][1], game_board_guess_1[4][1], Style.RESET_ALL, " | ", number_color_1[4][2],
              game_board_guess_1[4][2], Style.RESET_ALL, " | ", number_color_1[4][3], game_board_guess_1[4][3],
              Style.RESET_ALL, " | ", Back.BLACK, *reaction_x_1[4], Back.WHITE, *reaction_o_1[4], Style.RESET_ALL,
              sep="")
        print("---------------------\n#5  | ", number_color_1[5][0], game_board_guess_1[5][0], Style.RESET_ALL, " | ",
              number_color_1[5][1], game_board_guess_1[5][1], Style.RESET_ALL, " | ", number_color_1[5][2],
              game_board_guess_1[5][2], Style.RESET_ALL, " | ", number_color_1[5][3], game_board_guess_1[5][3],
              Style.RESET_ALL, " | ", Back.BLACK, *reaction_x_1[5], Back.WHITE, *reaction_o_1[5], Style.RESET_ALL,
              sep="")
        print("---------------------\n#6  | ", number_color_1[6][0], game_board_guess_1[6][0], Style.RESET_ALL, " | ",
              number_color_1[6][1], game_board_guess_1[6][1], Style.RESET_ALL, " | ", number_color_1[6][2],
              game_board_guess_1[6][2], Style.RESET_ALL, " | ", number_color_1[6][3], game_board_guess_1[6][3],
              Style.RESET_ALL, " | ", Back.BLACK, *reaction_x_1[6], Back.WHITE, *reaction_o_1[6], Style.RESET_ALL,
              sep="")
        print("---------------------\n#7  | ", number_color_1[7][0], game_board_guess_1[7][0], Style.RESET_ALL, " | ",
              number_color_1[7][1], game_board_guess_1[7][1], Style.RESET_ALL, " | ", number_color_1[7][2],
              game_board_guess_1[7][2], Style.RESET_ALL, " | ", number_color_1[7][3], game_board_guess_1[7][3],
              Style.RESET_ALL, " | ", Back.BLACK, *reaction_x_1[7], Back.WHITE, *reaction_o_1[7], Style.RESET_ALL,
              sep="")
        print("---------------------\n#8  | ", number_color_1[8][0], game_board_guess_1[8][0], Style.RESET_ALL, " | ",
              number_color_1[8][1], game_board_guess_1[8][1], Style.RESET_ALL, " | ", number_color_1[8][2],
              game_board_guess_1[8][2], Style.RESET_ALL, " | ", number_color_1[8][3], game_board_guess_1[8][3],
              Style.RESET_ALL, " | ", Back.BLACK, *reaction_x_1[8], Back.WHITE, *reaction_o_1[8], Style.RESET_ALL,
              sep="")
        print("---------------------\n#9  | ", number_color_1[9][0], game_board_guess_1[9][0], Style.RESET_ALL, " | ",
              number_color_1[9][1], game_board_guess_1[9][1], Style.RESET_ALL, " | ", number_color_1[9][2],
              game_board_guess_1[9][2], Style.RESET_ALL, " | ", number_color_1[9][3], game_board_guess_1[9][3],
              Style.RESET_ALL, " | ", Back.BLACK, *reaction_x_1[9], Back.WHITE, *reaction_o_1[9], Style.RESET_ALL,
              sep="")
        print("---------------------\n#10 | ", number_color_1[10][0], game_board_guess_1[10][0], Style.RESET_ALL, " | ",
              number_color_1[10][1], game_board_guess_1[10][1], Style.RESET_ALL, " | ", number_color_1[10][2],
              game_board_guess_1[10][2], Style.RESET_ALL, " | ", number_color_1[10][3], game_board_guess_1[10][3],
              Style.RESET_ALL, " | ", Back.BLACK, *reaction_x_1[10], Back.WHITE, *reaction_o_1[10], Style.RESET_ALL,
              "\n---------------------", sep="")

        print("\n\nplease give me a Combination of 4 numbers")

        guess = str(input(":"))
        game_board_guess_1[c] = list(guess)
        player_1_code_copy = list(player_1_code)

        # the X's and O's
        for d in range(0, 4):
            if (game_board_guess_1[c][d] == player_1_code_copy[d]):
                reaction_x_1[c].append("X")
                player_1_code_copy[d] = "X"

        for d in range(0, 4):
            if (game_board_guess_1[c][d] in player_1_code_copy):
                reaction_o_1[c].append("O")
                player_1_code_copy[player_1_code_copy.index(game_board_guess_1[c][d])] = "O"

        # color

        for d in range(0, 4):
            if (game_board_guess_1[c][d] == "1"):
                number_color_1[c][d] = Fore.YELLOW

            if (game_board_guess_1[c][d] == "2"):
                number_color_1[c][d] = Fore.BLUE

            if (game_board_guess_1[c][d] == "3"):
                number_color_1[c][d] = Fore.GREEN

            if (game_board_guess_1[c][d] == "4"):
                number_color_1[c][d] = Fore.CYAN

            if (game_board_guess_1[c][d] == "5"):
                number_color_1[c][d] = Fore.RED

            if (game_board_guess_1[c][d] == "6"):
                number_color_1[c][d] = Back.RED

            if (game_board_guess_1[c][d] == "7"):
                number_color_1[c][d] = Back.MAGENTA

            if (game_board_guess_1[c][d] == "8"):
                number_color_1[c][d] = Back.BLUE

        if (game_board_guess_1[c] == player_1_code):
            break

        # player 2
        print("\n\n---------------------\n| Possible Answers  |\n  ", *number_choices, "\n", Fore.RED, player_2,
              Style.RESET_ALL)
        print("| ", Back.BLACK, "X", Style.RESET_ALL, " = Right Spot    | \n| ", Back.WHITE, "O", Style.RESET_ALL,
              " = In Combination| ", "  \n---------------------", sep="")
        print("#1  | ", number_color_2[1][0], game_board_guess_2[1][0], Style.RESET_ALL, " | ", number_color_2[1][1],
              game_board_guess_2[1][1], Style.RESET_ALL, " | ", number_color_2[1][2], game_board_guess_2[1][2],
              Style.RESET_ALL, " | ", number_color_2[1][3], game_board_guess_2[1][3], Style.RESET_ALL, " | ",
              Back.BLACK, *reaction_x_2[1], Back.WHITE, *reaction_o_2[1], Style.RESET_ALL, sep="")
        print("---------------------\n#2  | ", number_color_2[2][0], game_board_guess_2[2][0], Style.RESET_ALL, " | ",
              number_color_2[2][1], game_board_guess_2[2][1], Style.RESET_ALL, " | ", number_color_2[2][2],
              game_board_guess_2[2][2], Style.RESET_ALL, " | ", number_color_2[2][3], game_board_guess_2[2][3],
              Style.RESET_ALL, " | ", Back.BLACK, *reaction_x_2[2], Back.WHITE, *reaction_o_2[2], Style.RESET_ALL,
              sep="")
        print("---------------------\n#3  | ", number_color_2[3][0], game_board_guess_2[3][0], Style.RESET_ALL, " | ",
              number_color_2[3][1], game_board_guess_2[3][1], Style.RESET_ALL, " | ", number_color_2[3][2],
              game_board_guess_2[3][2], Style.RESET_ALL, " | ", number_color_2[3][3], game_board_guess_2[3][3],
              Style.RESET_ALL, " | ", Back.BLACK, *reaction_x_2[3], Back.WHITE, *reaction_o_2[3], Style.RESET_ALL,
              sep="")
        print("---------------------\n#4  | ", number_color_2[4][0], game_board_guess_2[4][0], Style.RESET_ALL, " | ",
              number_color_2[4][1], game_board_guess_2[4][1], Style.RESET_ALL, " | ", number_color_2[4][2],
              game_board_guess_2[4][2], Style.RESET_ALL, " | ", number_color_2[4][3], game_board_guess_2[4][3],
              Style.RESET_ALL, " | ", Back.BLACK, *reaction_x_2[4], Back.WHITE, *reaction_o_2[4], Style.RESET_ALL,
              sep="")
        print("---------------------\n#5  | ", number_color_2[5][0], game_board_guess_2[5][0], Style.RESET_ALL, " | ",
              number_color_2[5][1], game_board_guess_2[5][1], Style.RESET_ALL, " | ", number_color_2[5][2],
              game_board_guess_2[5][2], Style.RESET_ALL, " | ", number_color_2[5][3], game_board_guess_2[5][3],
              Style.RESET_ALL, " | ", Back.BLACK, *reaction_x_2[5], Back.WHITE, *reaction_o_2[5], Style.RESET_ALL,
              sep="")
        print("---------------------\n#6  | ", number_color_2[6][0], game_board_guess_2[6][0], Style.RESET_ALL, " | ",
              number_color_2[6][1], game_board_guess_2[6][1], Style.RESET_ALL, " | ", number_color_2[6][2],
              game_board_guess_2[6][2], Style.RESET_ALL, " | ", number_color_2[6][3], game_board_guess_2[6][3],
              Style.RESET_ALL, " | ", Back.BLACK, *reaction_x_2[6], Back.WHITE, *reaction_o_2[6], Style.RESET_ALL,
              sep="")
        print("---------------------\n#7  | ", number_color_2[7][0], game_board_guess_2[7][0], Style.RESET_ALL, " | ",
              number_color_2[7][1], game_board_guess_2[7][1], Style.RESET_ALL, " | ", number_color_2[7][2],
              game_board_guess_2[7][2], Style.RESET_ALL, " | ", number_color_2[7][3], game_board_guess_2[7][3],
              Style.RESET_ALL, " | ", Back.BLACK, *reaction_x_2[7], Back.WHITE, *reaction_o_2[7], Style.RESET_ALL,
              sep="")
        print("---------------------\n#8  | ", number_color_2[8][0], game_board_guess_2[8][0], Style.RESET_ALL, " | ",
              number_color_2[8][1], game_board_guess_2[8][1], Style.RESET_ALL, " | ", number_color_2[8][2],
              game_board_guess_2[8][2], Style.RESET_ALL, " | ", number_color_2[8][3], game_board_guess_2[8][3],
              Style.RESET_ALL, " | ", Back.BLACK, *reaction_x_2[8], Back.WHITE, *reaction_o_2[8], Style.RESET_ALL,
              sep="")
        print("---------------------\n#9  | ", number_color_2[9][0], game_board_guess_2[9][0], Style.RESET_ALL, " | ",
              number_color_2[9][1], game_board_guess_2[9][1], Style.RESET_ALL, " | ", number_color_2[9][2],
              game_board_guess_2[9][2], Style.RESET_ALL, " | ", number_color_2[9][3], game_board_guess_2[9][3],
              Style.RESET_ALL, " | ", Back.BLACK, *reaction_x_2[9], Back.WHITE, *reaction_o_2[9], Style.RESET_ALL,
              sep="")
        print("---------------------\n#10 | ", number_color_2[10][0], game_board_guess_2[10][0], Style.RESET_ALL, " | ",
              number_color_2[10][1], game_board_guess_2[10][1], Style.RESET_ALL, " | ", number_color_2[10][2],
              game_board_guess_2[10][2], Style.RESET_ALL, " | ", number_color_2[10][3], game_board_guess_2[10][3],
              Style.RESET_ALL, " | ", Back.BLACK, *reaction_x_2[10], Back.WHITE, *reaction_o_2[10], Style.RESET_ALL,
              "\n---------------------", sep="")

        print("\n\nplease give me a Combination of 4 numbers")

        guess = str(input(":"))
        game_board_guess_2[c] = list(guess)
        player_2_code_copy = list(player_2_code)

        # the X's and O's
        for d in range(0, 4):
            if (game_board_guess_2[c][d] == player_2_code_copy[d]):
                reaction_x_2[c].append("X")
                player_2_code_copy[d] = "X"

        for d in range(0, 4):
            if (game_board_guess_2[c][d] in player_2_code_copy):
                reaction_o_2[c].append("O")
                player_2_code_copy[player_2_code_copy.index(game_board_guess_2[c][d])] = "O"

        # color

        for d in range(0, 4):
            if (game_board_guess_2[c][d] == "1"):
                number_color_2[c][d] = Fore.YELLOW

            if (game_board_guess_2[c][d] == "2"):
                number_color_2[c][d] = Fore.BLUE

            if (game_board_guess_2[c][d] == "3"):
                number_color_2[c][d] = Fore.GREEN

            if (game_board_guess_2[c][d] == "4"):
                number_color_2[c][d] = Fore.CYAN

            if (game_board_guess_2[c][d] == "5"):
                number_color_2[c][d] = Fore.RED

            if (game_board_guess_2[c][d] == "6"):
                number_color_2[c][d] = Back.RED

            if (game_board_guess_2[c][d] == "7"):
                number_color_2[c][d] = Back.MAGENTA

            if (game_board_guess_2[c][d] == "8"):
                number_color_2[c][d] = Back.BLUE

        if (game_board_guess_2[c] == player_2_code):
            break

    if (game_board_guess_2[c] == player_2_code):
        print("\n\ncongrats", player_2, "you win")

    if (game_board_guess_1[c] == player_1_code):
        print("\n\ncongrats", player_1, "you win")
