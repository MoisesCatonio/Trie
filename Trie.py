class No():

    def __init__(self, char=None):
        self.char = char
        self.filhos = {}
        self.folha = 0

class Arvore():
    referencia = No(); 
    palavras = []
    new_palavra = ""

    def PalavraToList(self, palavra):
        letrasPalavra = []
        for character in palavra:
            letrasPalavra.append(character)
        return letrasPalavra

    def Insert(self, palavra, no=referencia):
        listedPalavra = self.PalavraToList(palavra)
        for char in listedPalavra:
            if(char in no.filhos):
                no = no.filhos[char]
            else:
                no.filhos[char] = No(char)
                no = no.filhos[char]

    def __str__(self, no=referencia):
        
        # try 1
        if(len(no.filhos) != 0):
            for chave in no.filhos:    
                self.new_palavra = self.new_palavra + str(chave) 
                no = no.filhos[chave]
                self.__str__(no)
        else:
            self.palavras.append(self.new_palavra)
            self.new_palavra = ""
            no = self.referencia
        
        # try 2
        # if(len(no.filhos) > 0):
        #     for chave in no.filhos:
        #         self.new_palavra = self.new_palavra + str(chave)
        #         if(len(no.filhos) > 0):
        #             no = no.filhos[chave]
        #             self.__str__(no)
        #         else:
        #             self.palavras.append(self.new_palavra)
        #             self.new_palavra = ""

        for word in self.palavras:
            return word



tree = Arvore();

tree.Insert("League")

print(tree)
tree.Insert("Of")

print(tree)
tree.Insert("Legends")


# verify = tree.referencia.filhos['L'].filhos['e']
# print(verify.filhos)