class Restaurante: #uma classe define um estrutura modelo, um molde
    restaurantes = [] #éum atributo da classe Restaurante
    
    def __init__(self, nome, categoria): #função que serve como construtor. parâmetro self faz referência ao objeto que está sendo instanciado
        self.nome = nome
        self.categoria = categoria
        self.status = False #ao passar os atributos como self eles DEVEM ser passados como parâmetro
        Restaurante.restaurantes.append(self) #toda vez que criar um objeto eu o adiciono à lista
    
    def __str__(self): #método especial que transforma em string (?)
        return f'{self.nome} | {self.categoria}' #self.o que quero exibir, o return que faz a devolução

    def listar_restaurantes(): #consigo determinar que é um método próprio porque não tem __a__
        for restaurante in Restaurante.restaurantes:
            print(f'Nome do restaurante: {restaurante.nome} | Categoria: {restaurante.categoria}') #pegnado da lista, por issonão utiliza o self

#Instanciando uma classe: criando um objeto
restaurante_praca = Restaurante('Praça', 'Gourmet') #variável do tipo Restaurante
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

# restaurantes = [restaurante_praca, restaurante_pizza]
# # print(restaurantes)

# restaurante_praca.nome = 'Praça'
# restaurante_praca.categoria = 'Gourmet'

# #Para imprimir um objeto é necessário utilizar a função dir
# print(dir(restaurante_praca))

Restaurante.listar_restaurantes()




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

class Musica(self, nome, artista, duracao):
    self.nome = nome
    self.artista = artista
    self.duracao = duracao
    
faixa1 = Musica('Soap', 'Melanie Martinez', 310)