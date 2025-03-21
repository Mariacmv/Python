from modelos.restaurante import Restaurante #importa a classe restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 5)

restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
# restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_mexicano.alternar_estado() #por que tem que ser fora do main? Porque 

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
