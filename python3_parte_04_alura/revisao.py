class Filme:
    def __init__(self, name, ano, duracao,):
        self.__name = name
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.likes

    @property
    def dar_likes(self):
        self.__likes += 1

    @property
    def name(self):
        return self.__nome

    @name.setter
    def name(self, name):
        self.__name = name


class Serie:
    def __init__(self, nome, ano, temporada):
        self.__nome = nome
        self.ano = ano
        self.temporada = temporada
        self.__likes = 0

    @property
    def __likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def __nome(self):
        return self.__nome

    @nome.setter
    def __nome(self, nome):
        self.__nome = nome


if __name__ == '__main__':
    vingadore = Filme('vingadores - guerra infinita=', 2019, 160)
    print(vingadore)
