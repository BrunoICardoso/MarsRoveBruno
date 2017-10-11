from Planet import Mars
from Explorer import Scanner

# No Main faço deixo toda formação  de verificação na classe Scanner
# e alimentação da classe MARS


def main():

    scan = Scanner()
    mars = None
    loop = True
    rover = None

    print("=======================================================================")
    print("Bem vindo a exploração de marte com robô Rover, na primeira parte irá\n"
          "definir uma área para Rover andar em marte, na segunda parte irá\n"
          "por uma posição inicial do rover aonde ele deve pousar, na terceira\n"
          "parte irá movimentar o Rover por Marte")
    print("=======================================================================")

    # Primeiro estagio para largura do planet
    while True:

        commands = input("Entre com dois números sejam maior que zero, com espaço por exemplo: (1 1 )\n -> ")

        if scan.Check_Exit_Input(commands):
            loop = False
            break

        commands = commands.split()
        if scan.Check_Size2_Input(commands) and scan.Check_Coordinate(int(commands[0]), int(commands[1])):
            mars = Mars(int(commands[0]), int(commands[1]))
            break

        else:
            print("Entrada incorreta!!\nPor favor inseri dois elementos numéricos\n")

    print("\n--------------------------------------\n")

    # Verificação de try com else onde a verificação da classe rover se der alguma eventual erro.
    while loop:
        try:

            while True:

                commands = input("Digite a posição inicial do rover. Por favor lembre-se de manter dentro dos limites de Marte! \n ->  ")

                if scan.Check_Exit_Input(commands):
                    loop = False
                    break

                if scan.Check_Size3_Input(commands.split()) and scan.Park_Rover(commands.split(), mars)[1]:

                    rover = scan.Park_Rover(commands.split(), mars)[0]

                    print("\n--------------------------------------\n")
                    break

                else:
                    print("Por favor digiter apenas dois numeros e a direção, por exemplo '1  1'")

        except Exception as e:

            print("Ocorreu um erro para adicionar rover:{}".format(e))

        else:

            if scan.Check_Exit_Input(commands):
                break

            while True:

                commands = input("Digite uma seqüência de operações (M,L,R) por exemplo 'MLRRRL' \n -> ")

                if scan.Check_Exit_Input(commands):
                    loop = False
                    break

                if scan.Check_Sequence_Operations(commands):

                    scan.Rover_Explore(rover, mars,commands)
                    break

            else:
                print("Entrada incorreta!!\nPor favor inseri dois elementos numéricos com a direção certa")
    # Saida do resultado

    print("--------------- Output ---------------")

    if mars:
        for rover in mars.busy:
            print("{} {} {}".format(rover[0], rover[1], rover[2]))

        print("--------------------------------------")

    exit()

if __name__ == "__main__":
    main()
