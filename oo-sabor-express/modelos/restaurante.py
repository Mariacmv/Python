class Restaurante: #uma classe define um estrutura modelo, um molde
    nome = ''
    categoria = ''
    status = False

#Instanciando uma classe: criando um objeto
restaurante_praca = Restaurante() #variável do tipo Restaurante
restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]
# print(restaurantes)

restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

#Para imprimir um objeto é necessário utilizar a função dir
print(dir(restaurante_praca))




class Musica:
    nome = ''
    artista = ''
    duracao = float
    
faixa1 = Musica('Still with you', 'Jungkook', 3)
faixa2 = Musica('Magic Shop', 'BTS', 3,50)
faixa3 = Musica('Michael Jordan', 'Neffex', 2,95)
 
#OU

faixa1 = Musica()
faixa1.nome('Still with you')
faixa1.artista('Jungkoook')
faixa1.duracao(300)

faixa2 = Musica()
faixa2.nome('Magic Shop')
faixa2.artista('BTS')
faixa2.duracao(350)

faixa3 = Musica()
faixa3.nome('Michael Jordan')
faixa3.artista('Neffex')
faixa3.duracao(295)