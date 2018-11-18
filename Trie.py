class No():

    def __init__(self, char=None):
        self.char = char
        self.filhos = {}
        self.folha = 0

class Arvore():
    listedPalavra = []
    referencia = No(); 
    palavras = []
    new_palavra = ""

    # def AtualizarFolhas(self, no=referencia):
    #     if(len(no.filhos) != 0):
    #         for key in no.filhos:
    #             no = no.filhos[key]
    #             self.AtualizarFolhas(no)
    #     else:
    #         no.folha = 1

    def PalavraToList(self, palavra):
        letrasPalavra = []
        for character in palavra:
            letrasPalavra.append(character)
        return letrasPalavra

    def Insert(self, palavra, no=referencia):
        self.listedPalavra = self.PalavraToList(palavra)
        for char in self.listedPalavra:
            if(char in no.filhos):
                no = no.filhos[char]
            else:
                no.filhos[char] = No(char)
                no = no.filhos[char]
        # self.AtualizarFolhas()

    def __str__(self, no=referencia):
        
        if(len(no.filhos) != 0):
            for chave in no.filhos:
                print(no.filhos)
                self.new_palavra = self.new_palavra + str(chave) 
                no = no.filhos[chave]
                self.__str__(no)
        else:
            self.palavras.append(self.new_palavra)
            self.new_palavra = ""

        for word in self.palavras:
            return word



tree = Arvore();

tree.Insert("League")

print(tree)
tree.Insert("Of")

# print(vars(tree))

print(tree)
tree.Insert("Legends")

