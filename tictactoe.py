# coding: utf8


def printBoard():  # Exibe o tabuleiro no terminal;
    print("")
    print("  {} | {} | {} ".format(board[1], board[2], board[3]))
    print(" ---+---+--- ")
    print("  {} | {} | {} ".format(board[4], board[5], board[6]))
    print(" ---+---+--- ")
    print("  {} | {} | {} ".format(board[7], board[8], board[9]))
    print("")


def isPosFree(pos):  # Verifica se a posicao selecionada esta disponivel;
    return board[pos] in range(1, 10)


def isBoardFull(board):  # Verifica se o tabuleiro esta cheio;
    countX = board.count("X")
    countO = board.count("O")
    countAll = countX + countO

    if countAll > 8:
        return True
    else:
        return False


def placeLetter(letter, pos):  # Insere a letra no tabuleiro;
    board[pos] = letter


def playerMove(letter):  # Gerencia cada jogada;
    while True:
        move = input("Selecione uma posição para jogar (1-9): ")

        if move == "q":
            quit()

        try:
            move = int(move)
            if move > 0 and move < 10:
                if isPosFree(move):
                    placeLetter(letter, move)
                    break
                else:
                    print(">>> Espaço ocupado !!! \n")
            else:
                print(">>> Posição inválida! \n")
        except:
            print(">>> Favor informar um número! \n")


def checkWinner(letter):  # Verifica se houve um vencedor;
    isGameOver = False

    if (board[1] == letter and board[2] == letter and board[3] == letter):
        isGameOver = True
    elif (board[4] == letter and board[5] == letter and board[6] == letter):
        isGameOver = True
    elif (board[7] == letter and board[8] == letter and board[9] == letter):
        isGameOver = True
    elif (board[1] == letter and board[4] == letter and board[7] == letter):
        isGameOver = True
    elif (board[2] == letter and board[5] == letter and board[8] == letter):
        isGameOver = True
    elif (board[3] == letter and board[6] == letter and board[9] == letter):
        isGameOver = True
    elif (board[1] == letter and board[5] == letter and board[9] == letter):
        isGameOver = True
    elif (board[3] == letter and board[5] == letter and board[7] == letter):
        isGameOver = True

    return isGameOver


def getLetter(count):  # Gerencia o jogador atual;
    if count % 2 == 0:
        letter = "X"
    else:
        letter = "O"

    return letter


def main():  # main
    print("\n     --- TIC TAC TOE ---     ")
    printBoard()

    global board
    count = 0

    while True:
        if isBoardFull(board):
            print(">>> Empate! \n")
            break
        else:
            letter = getLetter(count)
            playerMove(letter)
            printBoard()

            if not(checkWinner(letter)):
                count += 1
            else:
                print(">>> O jogador {} venceu! \n".format(letter))
                break


while True:
    board = [x for x in range(0, 10)]
    main()
    newgame = input("Jogar Novamente? (S / N): ")
    if newgame in ["N", "n", "q"]:
        quit()
