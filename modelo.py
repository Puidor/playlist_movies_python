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
        self._likes += 1

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

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Duração: {self.duracao} minutos - Likes {self._likes}'


# Classe Filha - Herda atributos da classe Programa
class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        # super() -> Inicializa atributos do construtor da classe mãe
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Temporadas: {self.temporada} - Likes {self._likes}'


# Classe Playlist
class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    # Método que transforma a classe em um iteravel, passa o atributo "item" que queremos iterar
    def __getitem__(self, item):
        return self._programas[item]

    # Criando Getters para retorar listagem dos programas e tamanho
    @property
    def listagem(self):
        return self._programas

    # Método que transforma um item em sizeble/possivel de ser lido seu tamanho
    def __len__(self):
        return len(self._programas)


# Criando objetos
vingadores = Filme("vingadores - guerra infinita", 2018, 160)
titanic = Filme("titanic 2 - o retorno de jack", 2022, 180)
got = Serie("game of thrones", 2006, 6)
vikings = Serie("vikings", 2015, 5)

# Likes
vikings.dar_like()
vikings.dar_like()
vikings.dar_like()
titanic.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

# Criando lista com todos os filmes e séries
filmes_e_series = [vingadores, vikings, titanic, got]
# Criando objeto playlist
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f"\nTamanho da Playlist: {len(playlist_fim_de_semana)}\n")

# iteração na lista para printar os filmes e series
for programa in playlist_fim_de_semana:
    print(programa)
