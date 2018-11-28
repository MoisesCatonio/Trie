from collections import OrderedDict
from copy import deepcopy
alfabeto = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
defaultdict = OrderedDict() 

for letter in alfabeto:
		defaultdict[letter] = None
		
class No():

	def __init__(self, char=None):
		self.char = char
		self.filhos = deepcopy(defaultdict)
		self.folha = False

	def print(self, palavra):
		if (self.folha == True):
				print(palavra)
		for letter in alfabeto:
				if (self.filhos[letter] is not None):
						self.filhos[letter].print(deepcopy(palavra+letter))		
class Arvore():
	referencia = No(); 
	palavras = []
	def Insert(self, palavra, no=referencia):
		palavra = palavra.lower()
		listedPalavra = list(palavra)
		contador = 0
		for char in listedPalavra:
			contador+= 1
			if(no.filhos[char] is not None):
				no = no.filhos[char]
			else:
				no.filhos[char] = No(char)
				no = no.filhos[char]
			if (contador == len(listedPalavra)):
				no.folha = True
	def print(self):
		self.referencia.print("")

	def busca(self, palavra, no=referencia):
		palavra = palavra.lower()
		listedPalavra = list(palavra)
		retorno = ""
		contador = 0
		last_char_folha = False
		for char in listedPalavra:
			contador += 1
			if(contador <= len(listedPalavra)):
				if(no.filhos[char] is not None):
					no = no.filhos[char]
					retorno = retorno + str(no.char)
				else:
					retorno = ""
					print("Palavra não encontrada")
					break
			last_char_folha = no.folha
		if(last_char_folha == True):
			print("A seguinte palavra foi encontrada: ")
			return retorno
		else:
			print("A palavra não foi encontrada")
			retorno = ""
			return retorno
		
tree = Arvore()
tree.Insert("Cavalo")
tree.Insert("Abelha")
tree.Insert("Abeliano")
tree.Insert("Cava")

tree.print()				

print(tree.busca("Abel"))
