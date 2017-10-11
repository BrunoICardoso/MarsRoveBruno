from Rover import Rover
import re

# Criei essa classe para verifição do de exploração do planeta
# com regras de validação


class Scanner:

    # Varificação de inteiros e largura para fazer a verificação
    # da largura de cada pergunta como 2 a 3

    def Check_Coordinate(self, x, y) -> bool:

        if type(x) == int and type(x) == int:

            if int(x) >= 0 and int(y) >= 0:
                return True
            else:
                return False
        else:
            return False

    def Check_Size2_Input(self, size) -> bool:

        if (len(size) == 2):
            return True

        return False

    def Check_Size3_Input(self, size) -> bool:

        if (len(size) == 3):
            return True

        return False

    def Check_Exit_Input(self, exit) -> bool:

        if exit.lower() == 'exit':
            return True

        return False
    # ================================================

    # Verificação de do comando MLR e inteiros para devolver o object Rover e trazer verificção par ao MAIN


    def Park_Rover(self, command, mars) -> Rover and bool:

        if self.Check_Rover(int(command[0]), int(command[1]), str(command[2])):

            rover = Rover(int(command[0]),int(command[1]), command[2], mars)

            return rover, True

        return None,False


    def Check_Rover(self, x, y, direction) -> bool:

        if self.Check_Coordinate(x, y) and direction.upper() in ('N', 'E', 'S', 'W'):

            return True

        else:
            print("Digite dois números seguidos junto com N, E, S ou W")

            return False

    def Rover_Explore(self, rover, mars, command):

        for explo in command:

            if explo == "L":

                rover.SetDirectionCommand(explo)
               
            elif explo == "R":

                rover.SetDirectionCommand(explo)

            elif explo == "M":
               
                rover.goforward()

        mars.busy.append((rover.getX(), rover.getY(), rover.getCommand()))


    def Check_Sequence_Operations(self, sequence) -> bool:

        if re.compile("^[MRL]*$").match(sequence):
            return True

        else:
            print("Apenas valores 'L', 'M' , 'R'")


