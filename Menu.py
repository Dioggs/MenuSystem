#Setup
import math

#Funções
def indentificador_de_numero_primo(pergunta_numero):
      for val in range(2, pergunta_numero + 1):
        if pergunta_numero % val == 0:
            if val == pergunta_numero or val == 1:
                print(f'O numero {pergunta_numero} é primo')
                break
            else:
                print(f'o numero {pergunta_numero} não é primo')
                break

def logaritmo_de_numero(pergunta_numero):
    print(f'o logaritmo base 10 do {pergunta_numero} é {math.log(pergunta_numero, 10)}')

def calculadora_de_indice_de_massa_corporea(pergunta_peso, pergunta_altura):
    resultado = pergunta_peso / (pergunta_altura ** 2)
    
    if resultado < 18.5:
        print('Você está abaixo do peso')

    if resultado >= 18.5 and resultado <= 24.9:
        print('Você tem peso normal')

    if resultado >= 25.0 and resultado <= 29.9:
        print('Você tem pré obesidade')

    if resultado >= 30.0 and resultado <= 34.9:
        print('Você tem obesidade de grau 1')

    if resultado >= 35.0 and resultado <= 39.9:
        print('Você tem obesidade de grau 2')

    if resultado >= 40.0:
        print('Você tem obesidade grau 3')


#Perguntas
pergunta_menu = input('Olá, qual item do menu você gostaria?: ')

match pergunta_menu:
    case 'a': 
        pergunta_numero = abs(int(input('Digite um numero: ')))
        indentificador_de_numero_primo(pergunta_numero)
    case 'b':
        pergunta_numero = int(input('Digite um numero: '))
        logaritmo_de_numero(pergunta_numero)
    case 'c':
        pergunta_peso = int(input('Qual o seu peso?: '))
        pergunta_altura = float(input('Qual a sua altura?: '))
        calculadora_de_indice_de_massa_corporea(pergunta_peso, pergunta_altura)
    case 'f':
        print('Tenha um bom dia!')



