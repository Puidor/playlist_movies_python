# Classe Mãe
class Programa:
    def __init__(self, nome, ano):
        # Inicializa atributos privados com apenas 1 underline (_). [Convenção entre os programadores]
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


# Classe Filha - Herda atributos da classe Programa
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        # super() -> Inicializa atributos do construtor da classe mãe
        super().__init__(nome, ano)
        self.duracao = duracao


# Classe Filha - Herda atributos da classe Programa
class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        # super() -> Inicializa atributos do construtor da classe mãe
        super().__init__(nome, ano)
        self.temporada = temporada


vingadores = Filme("vingadores - guerra infinita", 2018, 160)

print(
    f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} minutos - Likes {vingadores.likes}')

vikings = Serie("vikings", 2015, 5)

print(
    f'Nome: {vikings.nome} - Ano: {vikings.ano} - Temporadas: {vikings.temporada} - Likes {vikings.likes}')
