class Restaurante: #uma classe define um estrutura modelo, um molde
    restaurantes = [] #é um atributo da classe Restaurante
    
    def __init__(self, nome, categoria): #função que serve como construtor. parâmetro self faz referência ao objeto que está sendo instanciado
        self._nome = nome.title() #só a primeira letra maiúscula
        self._categoria = categoria.upper() #toda as letras ficam maiúsculas
        self._status = False #ao passar os atributos como self eles DEVEM ser passados como parâmetro
        Restaurante.restaurantes.append(self) #toda vez que criar um objeto eu o adiciono à lista
    
    def __str__(self): #método especial que transforma em string (?)
        return f'{self._nome} | {self._categoria}' #self.o que quero exibir, o return que faz a devolução

    def listar_restaurantes(): #consigo determinar que é um método próprio porque não tem __a__
        print(f"{'Nome do restaurante'.ljust(46)} | {'Categoria'.ljust(36)} | {'Status'}") #coloca entre chaves para manter o espaçamento definido abaixo
        for restaurante in Restaurante.restaurantes:
            print(f'Nome do restaurante: {restaurante._nome.ljust(25)} | Categoria: {restaurante._categoria.ljust(25)} | Status: {restaurante.status}') #pegando da lista, por isso não utiliza o self. Para imprimir não utiliza o _status porque se refere ao atributo não à propriedade status

    @property
    def status(self): #pra definir se 
        return '✓' if self._status else '✗'
        
    def alternar_estado(self): #método para os objetos
        self._status = not self._status

#Instanciando uma classe: criando um objeto
# restaurante_praca = Restaurante('praça', 'Gourmet') #variável do tipo Restaurante
# restaurante_praca.alternar_estado()
# restaurante_pizza = Restaurante('pizza express', 'Italiana')

# restaurantes = [restaurante_praca, restaurante_pizza]
# # print(restaurantes)

# restaurante_praca.nome = 'Praça'
# restaurante_praca.categoria = 'Gourmet'

# #Para imprimir um objeto é necessário utilizar a função dir
# print(dir(restaurante_praca))

# Restaurante.listar_restaurantes()









# class Musica:
#     nome = ''
#     artista = ''
#     duracao = float
    
# faixa1 = Musica('Still with you', 'Jungkook', 3)
# faixa2 = Musica('Magic Shop', 'BTS', 3,50)
# faixa3 = Musica('Michael Jordan', 'Neffex', 2,95)
 
# #OU

# faixa1 = Musica()
# faixa1.nome('Still with you')
# faixa1.artista('Jungkoook')
# faixa1.duracao(300)

# faixa2 = Musica()
# faixa2.nome('Magic Shop')
# faixa2.artista('BTS')
# faixa2.duracao(350)

# faixa3 = Musica()
# faixa3.nome('Michael Jordan')
# faixa3.artista('Neffex')
# faixa3.duracao(295)

# class Musica(self, nome, artista, duracao):
#     self.nome = nome
#     self.artista = artista
#     self.duracao = duracao
    
# faixa1 = Musica('Soap', 'Melanie Martinez', 310)