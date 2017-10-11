"""
Criei objecto ROVER para ficar mais com relacionamento entre o planet onde pode ser classes diferentes
de planetas ou referenciar varios tipos


"""

class Rover:
    def __init__(self, x, y, command, planet=None):

        self._x = x
        self._y = y
        self._direction = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
        self._command = command
        self._Planet = planet
        self.initial = (self._x, self._y, self._command)


    # Na função setDirectionCommand, basicamente é uma siminulçao de uma bussola, onde verifica a posição atual
    # e direciona conforme os comandos de (M L R).

    def SetDirectionCommand(self, valor):
        directions = ("N", "E", "S", "W")

        if valor == 'L':

            if directions.index(self._command) == 0:
                self._command = directions[3]

            else:
                self._command = directions[directions.index(self._command) - 1]

        elif valor == 'R':

            if directions.index(self._command) == 3:
                self._command = directions[0]

            else:
                self._command = directions[directions.index(self._command) + 1]
    # ================================================================================


    # Nas três funções abaixo são basicamente retorna o tipo certo de cada variavel do construtor

    def getCommand(self) -> str:
        return self._command

    def getX(self)-> int:
        return self._x

    def getY(self)-> int:
        return self._y

    # ==================================++++


        # Função initial verificar se a posição do robo se já esta ocupada ou não no planeta
        # com isso o get_formatted_position or current mostra posição atual do robô

    def initial(self, tup):
        for field in self._Planet.busy:
            if (tup[0], tup[1]) == (field[0], field[1]):
                raise RuntimeError("Está posição já esta ocupada")
        self._initial = tup

    def get_formatted_position(self):

        return "{} {} {}".format(self._x, self._y, self._direction)

    def get_current_position(self):
        return (self._x, self._y)

    def return_to_start(self):
        self._x = self._initial[0]
        self._y = self._initial[1]
        self._direction = self._initial[2]
    # ==============================================


    # Move o Rover para frente com sentido através das coordenadas Y e X onde tem
    # um DICT com valores fixo em coordenadas.

    def goforward(self):

        for direction in self._command:
            self._x += self._direction[direction][0]
            self._y += self._direction[direction][1]

        for spaces in self._Planet.busy:
            if self.get_current_position() == (spaces[0], spaces[1]):
                print("Atingiu uma posição que já foi tomada. \n Retornando a posição")
                self.return_to_start()

