# coding: utf8


class Game:
    pos = ["\n", 1, 2, 3, 4, 5, 6, 7, 8, 9]
    jogador = "X"
    isGameOver = False

    def main(self):
        while self.isGameOver == False:
            self.board()        # Carrega e atualiza o tabuleiro;
            self.jogada()       # Gerencia as jogadas;
            self.gameOver()     # Verifica se o jogo acabou;
            self.novaRodada()   # Prepara o proximo jogador;

        print("Jogar Novamente? (S / N)", end=" ")
        newgame = input()

        if newgame in ["S", "s"]:
            self.isGameOver = False
            self.main()
        else:
            quit()

    def board(self):
        board = "{1}Jogador: {0} {1}".format(self.jogador, self.pos[0])
        board += "    {} | {} | {} {}".format(
            self.pos[1], self.pos[2], self.pos[3], self.pos[0])
        board += "   ---+---+--- {}".format(self.pos[0])
        board += "    {} | {} | {} {}".format(
            self.pos[4], self.pos[5], self.pos[6], self.pos[0])
        board += "   ---+---+--- {}".format(self.pos[0])
        board += "    {} | {} | {} {}".format(
            self.pos[7], self.pos[8], self.pos[9], self.pos[0])
        print(board)

    def jogada(self):
        jogada = input("Proxima jogada: ")

        novaJogada = str(self.pos[int(jogada)])

        if novaJogada == "X" or novaJogada == "O":
            self.main()
        else:
            self.pos[int(jogada)] = self.jogador

    def novaRodada(self):
        if self.jogador == "X":
            self.jogador = "O"
        else:
            self.jogador = "X"

    def gameOver(self):
        gameover = ""

        if all(a == self.jogador for a in self.pos[1:4]):
            gameover = "* O JOGADOR {} VENCEU! *".format(self.jogador)
            self.isGameOver = True
        elif all(a == self.jogador for a in self.pos[4:7]):
            gameover = "* O JOGADOR {} VENCEU! *".format(self.jogador)
            self.isGameOver = True
        elif all(a == self.jogador for a in self.pos[7:10]):
            gameover = "* O JOGADOR {} VENCEU! *".format(self.jogador)
            self.isGameOver = True

        print(gameover)


game = Game()
game.main()

"""
to-do
logica do jogo na classe gameover, dizendo jogador vencedor ou VELHA
opcao para jogar novamente ao fim de uma partida
"""
