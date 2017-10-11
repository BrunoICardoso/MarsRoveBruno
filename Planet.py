#Objectc do planeta Marte para demostrar tem uma verificaçãono construturo de inteiros e pra valores
# positivos
class Mars:

    def __init__(self, x, y):

        if type(x) == int and type(x) == int:

            if int(x) >= 0 and int(y) >= 0:

                self.x = x
                self.y = y

            else:
                raise ValueError("Valor tem que ser positivo")
        else:
            raise ValueError("Valor não é um inteiro")

        self.busy = []



