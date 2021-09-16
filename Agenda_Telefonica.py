import os

contatos = []
contatos_favoritos = []
a = 0

def lista_favoritos():
    global contatos_favoritos
    os.system('cls')
    
    if contatos_favoritos == []:
        print('\n\t | Lista de Favoritos Vazia|')
        return 0
    print('\n\t | Lista de Favoritos |')
    for item in contatos_favoritos:
        dados(item[0], item[1], item[2])
        

def favoritar():
    global contatos_favoritos
    global contatos
    contatos_alterar = []
    os.system('cls')
    if contatos == []:
        print('\n\t | Não há o que favoritar |')
        return 0
    print('\n\t | Adicionar os Favoritos |\n')
    print('Qual contato deseja favoritar ?')
    x=0
    cont = 1
    for nomes in contatos:
        print(f'[{cont}] - {nomes[x]}')
        contatos_alterar.append(nomes[x])
        x+2
        cont+=1
    
    print('\n[0] - Sair')
    y = int(input('\n>>> '))
    if y == 0:
        os.system('cls')
        return 0

    nome = contatos_alterar[y-1]
    x=0
    for item in contatos:
        if item[x] == nome:
            contatos_favoritos.append([item[x], item[x+1], item[x+2]])



def excluir():
    contatos_apagar = []
    global contatos
    os.system('cls')
    if contatos == []:
        print('\n\t | Não há o que excluir |')
        return 0
    print('\n\t | Excluir Contato |\n')
    print('Qual contato deseja apagar ?')
    x=0
    cont = 1
    for nomes in contatos:
        print(f'[{cont}] - {nomes[x]}')
        contatos_apagar.append(nomes[x])
        x+2
        cont+=1

    print('\n[0] - Sair')
    y = int(input('\n>>> '))
    if y == 0:
        os.system('cls')
        return 0

    del(contatos[y-1])
    os.system('cls')
    print('\t   Contato excluído com sucesso!')


def alterar():
    contatos_alterar = []
    global contatos
    os.system('cls')
    if contatos == []:
        print('\n\t | Não há o que alterar |')
        return 0
    print('\n\t | Alterar Contato |\n')
    print('Qual contato deseja alterar ?\n')
    x=0
    cont = 1
    for nomes in contatos:
        print(f'[{cont}] - {nomes[x]}')
        contatos_alterar.append(nomes[x])
        x+2
        cont+=1
    
    print('\n[0] - Sair')
    y = int(input('\n>>> '))
    if y == 0:
        os.system('cls')
        return 0
    nome = contatos_alterar[y-1]
    x=0
    for item in contatos:
        if item[x] == nome:
            print(f'\nNome atual: {item[x]}')
            print(f'Número atual: {item[x+1]}')
            print(f'Cidade atual: {item[x+2]}')
            item[x] = input('\nNovo nome: ')
            item[x+1] = input('Novo número: ')
            item[x+2] = input('Nova cidade: ')
            os.system('cls')
            print('\t   Contato alterado com sucesso!')
            break

def pesquisar():
    global contatos
    os.system('cls')
    if contatos == []:
        print('\n\t | Não há o que pesquisar |')
        return 0
    print('\n\t| Pesquisar |')
    nome = input("\nInsira o nome do contato: ")
    x=0
    for item in contatos:
        if item[x] == nome:
            os.system('cls')
            print('\t    <Contato encontrado>')
            dados(item[x], item[x+1], item[x+2])
       
    if item[x] != nome:
        os.system('cls')
        print('\t <Contato não encontrado!>')

def dados(nome, telefone, cidade):
    print('\nNome: %s Telefone: %s Cidade: %s' %(nome, telefone, cidade))

def lista():
    os.system('cls')
    if contatos == []:
        print('\n\t | Lista de Contatos Vazia |')
        return 0
    print('\n\t | Lista de Contatos |')
    for item in contatos:
        dados(item[0], item[1], item[2])

def cadastro():
    global contatos
    os.system('cls')
    print('\t| CADASTROS |\n')
    nome = input('Nome: ')
    telefone = input('Telefone: ')
    cidade = input('Cidade: ')
    contatos.append([nome, telefone, cidade])
    os.system('cls')
    print('\n\t    <Contato foi Salvo!>')


def validar_resposta(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return(valor)
        except ValueError:
            print('Valor inválido, digite um número válido entre %d e %d' %(inicio,fim))

def main():
    global a
    if a == 0:
        os.system('cls')
        a+=1
    print('\n\t  -= AGENDA TELEFÔNICA =-')
    print('\n[1] - CADASTRAR   |   [5] - EXCLUIR')
    print('[2] - PESQUISAR   |   [6] - CONTATOS SALVOS')
    print('[3] - ALTERAR     |   [7] - CONTATOS FAVORITOS')
    print('[4] - FAVORITAR   |   [0] - SAIR')

    return validar_resposta('\n>>> ',0,7)


while True:
    choice = main()
    if choice == 0:
        os.system.exit
    elif choice == 1:
        cadastro()
    elif choice == 2:
        pesquisar()
    elif choice == 3:
        alterar()
    elif choice == 4:
        favoritar()
    elif choice == 5:
        excluir()
    elif choice == 6:
        lista()
    elif choice == 7:
        lista_favoritos()