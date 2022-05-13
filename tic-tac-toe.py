from random import randint # <- importa randint de random

# funcao que exibe o tabuleiro
def ExibeTabuleiro():
    print(" ----------- ") # <- printa a parte de cima do tabuleiro
    
    # linha por linha, 3 vezes:
    for lin in range(3):
        print("| ", end='') # <- printa as divisorias do tabuleiro na linha

        # coluna por coluna, 3 vezes:
        for col in range(3):
            print(T[lin][col], "| ", end='') # <- printa os 'X' e 'O' no tabuleiro
        print("") # <- pula linha

        # se não for a ultima linha:
        if lin < 2:
            print("|---+---+---|") # <- printa as interseccoes
        else:
            print(" ----------- ") # <- printa a parte de baixo do tabuleiro        
          
T = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] # <- lista que contem os valores 'X' e 'O' do tabuleiro e suas posicoes
lado = [[0,1],[1,0],[1,2],[2,1]] # <- lista que contem as posicoes correspondentes aos lados do tabuleiro
ExibeTabuleiro() # <- chama a funcao para exibir o tabuleiro
posicao = 0 # <- int que representa a posicao escolhida pelo jogador
peca = "X" # <- string que representa a peca atual (X ou O)
j = 0 # <- int que representa o numero de jogadas
ganho = [[0,1,2],[3,4,5],[6,7,8], # <- lista que contem as combinacoes de posicao que correspondem a uma vitoria
         [0,3,6],[1,4,7],[2,5,8],
         [0,4,8],[2,4,6]]
end = False # <- boleano que encerra o jogo

while posicao != 9:
    while True:

        # se end for verdadeiro, encerra o jogo
        if end:
            break
        # se o numero de jogadas for 9, todas as posicoes estao preenchidas, logo, empatou
        if j == 9:
            print("Deu Velha")
            break

        # se o numero de jogadas for positivo, é a vez do jogador
        if j % 2 == 0:
            posicao = int(input("Digite a jogada para X: ")) # <- posicao vai ser um numero de 0 a 8 que representa a posicao desejada a se preencher no tabuleiro

            # a posicao deve ser um numero valido (maior que 0 e menor que 8), se nao:
            if posicao >8 or posicao <0:
                print("Posicao invalida!")
                continue
            lin = int(posicao / 3) # <- a linha corresponde ao numero escolhido / 3
            col = posicao % 3 # <- a coluna corresponde ao resto do numero escolhido / 3

            # caso a posicao nao esteja ocupada:
            if T[lin][col]==" ":
                T[lin][col] = 'X' # <- preenche a posicao com um X
                j=j+1 # <- adiciona 1 ao numero de jogadas
            else:
                print("Campo ja preenchido, Digite um valido") # <- pede para que digite um novo numero
                continue

            peca = "X" # <- informa que a peca que esta sendo usada eh 'X'
            
        # vez do computador
        else:

            # se a posicao do meio estiver ocupada e for a primeira jogada:
            if T[1][1] != ' ' and j == 1:
                guess = randint(0, 3) # <- escolha um numero aleatorio entre 4
                T[lado[guess][0]][lado[guess][1]] = 'O' # <- coloca o 'O' na posicao aleatoria escolhida baseada no indice dos elementos da lista 'lado', em um dos lados do tabuleiro

            # se a posicao do meio estiver vazia e for a primeira jogada:
            elif T[1][1] == ' ' and j == 1:
                T[1][1] = 'O' # coloca o 'O' no meio do tabuleiro
                
            else:
                
            # testa cada uma das 3 possiveis quase vitorias para cada opcao de vitoria na lista ganho:    
            # [ X | X |   ] , [   | X | X ] e [ X |   | X ], respectivamente
                for i in range(8):     
                    if T[int(ganho[i][0] / 3)][ganho[i][0] % 3] == T[int(ganho[i][1] / 3)][ganho[i][1] % 3] != ' ' and T[int(ganho[i][2] / 3)][ganho[i][2] % 3] == ' ': 
                      T[int(ganho[i][2] / 3)][ganho[i][2] % 3] = "O" # preenche na posicao que falta, para bloquear
                      break
                    
                    elif T[int(ganho[i][1] / 3)][ganho[i][1] % 3] == T[int(ganho[i][2] / 3)][ganho[i][2] % 3] != ' ' and T[int(ganho[i][0] / 3)][ganho[i][0] % 3] == ' ':
                      T[int(ganho[i][0] / 3)][ganho[i][0] % 3] = "O"
                      break                      
                      
                    elif T[int(ganho[i][0] / 3)][ganho[i][0] % 3] == T[int(ganho[i][2] / 3)][ganho[i][2] % 3] != ' ' and T[int(ganho[i][1] / 3)][ganho[i][1] % 3] == ' ':
                      T[int(ganho[i][1] / 3)][ganho[i][1] % 3] = "O"
                      break

                else:
                    for i in range(9):
                        if T[int(i / 3)][i % 3] == 'O':
                            
                            # * colocar perto de um que ja tenha na tabela
                            # * checar onde tem vitorias possiveis
                            # * checar se a posicao ja esta ocupada

                            #     ----------- 
                            # /0 |   | O |   | 
                            #    |---+---+---|
                            # /1 |   | X |   | 
                            #    |---+---+---|
                            # /2 |   |   |   | 
                            #     ----------- 
                            #     %0  %1  %2

                            #     [0 , 1 , 2]
                            #     [0 , 3 , 6]
                            #     [0 , 4 , 8]

                            break

            peca = "O"            
            j += 1 # <-  adiciona 1 ao numero de jogadas
            ExibeTabuleiro() # <- chama a funcao para exibir o tabuleiro
            
        for i in ganho:
            for x in i:
                l = int(x/3)
                c = x%3
                if T[l][c] != peca:
                    break
            else:
                ExibeTabuleiro() # <- chama a funcao para exibir o tabuleiro
                print("Jogador %s venceu a partida"% peca)
                vitoria=True
                end = True
                break
                
    break
