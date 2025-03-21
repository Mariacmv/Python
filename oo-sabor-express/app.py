from modelos.restaurante import Restaurante #importa a classe restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_mexicano.alternar_estado() #por que tem que ser fora do main?

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
