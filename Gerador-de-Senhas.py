"""
Projeto: Gerador de Senhas
Descrição: Um programa para gerar senhas aleatórias com comprimento especificado pelo usuário.
Autor: Joseffer Maxwel Oliveira das Mercês
Contato: joseffermax1472@gmail.com
GitHub: https://github.com/joseffermax
Direitos Autorais © 2023 Joseffer Maxwel Oliveira das Mercês. Todos os direitos reservados.
"""

import os
import random
from time import sleep
from colorama import Style

senhas_geradas = []

# Função para ler um número inteiro do usuário
def leiaInt(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Erro... Digite uma opção válida!")
            voltar()
            return None
        
# Função para criar uma linha de caracteres "-" com tamanho padrão de 55
def linha(tam=55):
    return '-' * tam

# Função para imprimir o cabeçalho centralizado
def cabecalho(txt):
    print(linha())
    print(txt.center(55))
    print(linha())

# Função para exibir o menu e retornar a opção escolhida pelo usuário
def menu(lista):
    while True:
        limpartela()
        cabecalho('GERADOR DE SENHAS')
        for c, item in enumerate(lista, 1):
            print(f'[{c}] - {item}')
        print(linha())
        opcao = leiaInt('Sua opção: ')
        if opcao is None:
            continue
        if opcao in [1, 2, 3]:
            return opcao
        else:
            print("Erro... Por favor, digite um número inteiro válido!")
            voltar()

# Função para limpar a tela do console
def limpartela():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

# Função para aguardar a pressão da tecla Enter para voltar
def voltar():
    input("Pressione " + Style.BRIGHT + "'Enter'" + Style.RESET_ALL + " para voltar... ")
    return

while True:
    # Exibe o menu e aguarda a escolha do usuário
    resposta = menu(['Iniciar', 'Histórico', 'Sair do Sistema'])
    limpartela()
    cabecalho('GERADOR DE SENHAS')

    if resposta == 1: # Iniciar
        while True:
            banco = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&" # Banco de onde são geradas as senhas
            entrada = None
            comprimento = None
            while entrada is None:
                try:
                    entrada = int(input('Quantidade de senhas a serem geradas: '))
                except ValueError: # Entrada para caso o usuário digite letras de vez números
                    print('Erro... Digite um número inteiro válido!')
                    voltar()
                    limpartela()
                    cabecalho('GERADOR DE SENHAS')
            
            entrada_original = entrada # Armanezar a variável entrada

            while comprimento is None:
                try:
                    comprimento = int(input('Insira o comprimento da senha: '))
                except ValueError: # Entrada para caso o usuário digite letras de vez números
                    print('Erro... Digite um número inteiro válido!')
                    voltar()
                    limpartela()
                    cabecalho('GERADOR DE SENHAS')
                    entrada = entrada_original
                    print(f'Quantidade de senhas a serem geradas: {entrada}')
            print(linha())
            print('PROCESSANDO...')
            print(linha())
            sleep(3)
            print('Senha(s) Gerada(s)'.center(55))
            for _ in range(entrada): # Gera as senhas aleatórias
                senha = ''.join(random.choices(banco, k=comprimento))
                senhas_geradas.append(senha)
                print(senha)
            print(linha())
            while True: # Entrada para verificar se deve continuar ou não
                escolha = input("Deseja gerar novas senhas? (S/N): ")
                if escolha.upper() == 'N': # Primeira entrada caso o usuário não queira mais gerar senhas
                    break  
                elif escolha.upper() == 'S': # Segunda entrada caso o usuário deseje continuar gerando senhas
                    limpartela()
                    cabecalho('GERADOR DE SENHAS')
                    break
                else: # Terceira entrada caso o usuário não digite nem 'S' ou 'N'
                    print("Opção inválida. Digite apenas 'S' ou 'N'.")
            if escolha.upper() == 'N':
                break
                    
    elif resposta == 2: # Histórico
        while True:
            limpartela()
            cabecalho('HISTÓRICO')
            if not senhas_geradas: # Primeira entrada
                print('Nenhuma Senha Cadastrada!')
            else: # Segunda entrada, quando o usuário digitar a(s) senha(s)
                print('Senhas Cadastradas:')
                for i, senha in enumerate(senhas_geradas, 1): # Adiciona números (1º) no começo de cada senha gerada
                    print(f'{i}º - {senha}')               
            print(linha())
            sair = input("Pressione 'Q' para sair: ")
            if sair.upper() == 'Q': # Entrada para sair do histórico
                break
            else: # Entrada para verificar se o usuário caso não digite 'Q' para sair
                print("Erro... É apenas aceito 'Q' como resposta!")
                voltar()
                limpartela()
            
    elif resposta == 3: # Sair
        while True:
                limpartela()
                cabecalho('GERADOR DE SENHAS')
                print("Encerrando o programa...")
                print("Obrigado pela preferência!")
                print(linha())
                sair_ou_voltar = input("Deseja sair do programa? S/N: ")
                if sair_ou_voltar.upper() == "S": # Primeira entrada para sair do programa
                    exit()
                elif sair_ou_voltar.upper() == "N": # Segunda entrada caso o usuário deseja voltar para o programa
                    print("Retornando ao Menu...")
                    sleep(2)
                    limpartela()
                    break
                else: # Entrada de erro caso o usuário não digite 'S' ou 'N'
                    print("Opção inválida. Apenas 'S' e 'N' são permitidos!") 
                    voltar()
                limpartela()
    else: # Opção extra para garantir
        print('Erro... Digite uma opção válida!')
        voltar()
