print('Bem vindo a empresa do Marcus Vinicius da Silva Nunes')

#Lista que irá armazenar os funcionários cadastrados
lista_funcionarios = []
#id global único para cada funcionário cadastrado, iniciando deste número
id_global = 0001

#função cadastrar funcionário
def cadastrar_funcionario(id):
    print('\nCADASTRO DE FUNCIONARIO')

    nome = input('Digite o nome do funcionário: ')
    setor = input('Digite o setor do funcionário: ')
    salario = float(input('Digite o salario do funcionário: R$ '))

#criação de dicionário para cada funcionário
    funcionario = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }

#Nesta parte, se adiciona uma cópia do dicionário para a lista principal
    lista_funcionarios.append(funcionario.copy())
    print(f'Funcionario cadastrado com sucesso! ID: {id}')

#função de consultar os funcionários cadastrados
def consultar_funcionarios():
    while True:
        print('\nConsulta de Funcionários')
        print('1 - Consultar Todos')
        print('2 - Consultar por ID')
        print('3 - Consultar por Setor')
        print('4 - Retornar ao menu principal')

        escolha = input('Digite uma opção: ')

#Opção de listar todos os funcionários
        if escolha == '1':
            if not lista_funcionarios: #caso ainda não tenha nenhum funcionário cadastrado, print a seguir
                print('Nenhum funcionário cadastrado.')
            else:
                for func in lista_funcionarios:
                    print(f'ID: {func["id"]} | Nome: {func["nome"]} | Setor: {func["setor"]} | Salário: {func["salario"]:.2f}')
#opção de buscar o funcionário por seu ID
        elif escolha == '2':
            try:
                id_busca = int(input('Digite o ID do funcionário: '))
            except ValueError:
                print('ID inválido. Digite um número inteiro')
                continue
#Caso o funcionário não seja encontrado, retornará a mensagem do print
            encontrado = False
            for func in lista_funcionarios:
                if func['id'] == id_busca:
                    print(f'ID: {func["id"]} | Nome: {func["nome"]} | Setor: {func["setor"]} | Salário: {func["salario"]:.2f}')
                    encontrado = True
                    break
            if not encontrado:
                print('Funcionário não encontrado.')
#opção de busca dos funcionários cadastrados pelo setor
        elif escolha == '3':
            setor_busca = input('Digite o setor do(s) funcionário(s): ')
            encontrado = False #caso não tenha funcionário cadastrado no setor buscado
            for func in lista_funcionarios:
                if func['setor'] == setor_busca:
                    print(f'ID: {func["id"]} | Nome: {func["nome"]} | Setor: {func["setor"]} | Salário: {func["salario"]:.2f}')
                    encontrado = True
            if not encontrado:
                print('Nenhum funcionário encontrado nesse setor.')
#Opção para retornar ao menu principal
        elif escolha == '4':
            print('Saindo...')
            return
        #Caso não tenha sido escolhida nenhuma das opções válidas
        else:
            print('Opção inválida. Por favor, escolha uma opção de 1 a 4')

#Função para remover funcionários cadastrados
def remover_funcionario():
    while True:
        try:
            id_remover = int(input('Digite o Id do funcionario: '))
        except ValueError: #Except para caso seja digitado o número float, por exemplo, ou algo diferente de um número inteiro.
            print('Por favor, digite um número inteiro.')
            continue
#Para o colaborador com ID encontrado para ser removido, teremos:
        for colab in lista_funcionarios:
            if colab['id'] == id_remover:
                lista_funcionarios.remove(colab)
                print(f'Funcionario de ID {id_remover} removido com sucesso!')
                return

#Caso não tenha funcionário com o ID selecionado para remover, teremos o print
        print('ID inválido. Nenhum funcionario foi encontrado com este ID.')

#a partir daqui é o menu principal
while True:
    print('\nMENU PRINCIPAL')
    print('1 - Cadastrar Funcionario')
    print('2 - Consultar Funcionario')
    print('3 - Remover Funcionario')
    print('4 - Encerrar Programa')

    escolha = input('Digite uma opção: ')

    if escolha == '1':
        cadastrar_funcionario(id_global)
        id_global += 1 #Aqui se acrescenta o ID global quando um novo cadastro for realizado
    elif escolha == '2':
        consultar_funcionarios()
    elif escolha == '3':
        remover_funcionario()
    elif escolha == '4':
        print('Programa encerrado.')
        break #Aqui sai do loop para encerrar o sistema
    else:
        print('Opção inválida. Por favor, escolha uma opção de 1 a 4')