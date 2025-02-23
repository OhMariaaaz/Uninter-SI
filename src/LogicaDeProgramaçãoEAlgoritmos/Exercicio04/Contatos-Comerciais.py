'''

Você e sua equipe de programadores foram contratados por uma pequena empresa 
para desenvolver um software de gerenciamento de Contatos Comerciais. Este 
software deve ter o seguinte menu e opções:
⦁	Cadastrar Contato
⦁	Consultar Contato
⦁	Consultar Todos 
⦁	Consultar por Id
⦁	Consultar por Atividade
⦁	Retornar ao menu
⦁	Remover Contato
⦁	Encerrar Programa

Elabore um programa em Python que: 
⦁	Deve-se implementar o print com o seu nome completo (somente print, 
não usar input aqui). 
Por exemplo: print(“Bem vindos a lista de contatos do Bruno Kostiuk”)  
[EXIGÊNCIA DE CÓDIGO 1 de 8];

⦁	Deve-se implementar uma lista com o nome de lista_contatos e a variável 
id_global com valor inicial igual ao número de seu RU 
[EXIGÊNCIA DE CÓDIGO 2 de 8];

⦁	Deve-se implementar uma função chamada cadastrar_contato(id) que recebe 
apenas id como parâmetro e que: [EXIGÊNCIA DE CÓDIGO 3 de 8];

⦁	Pergunta nome, atividade, telefone do contato;

⦁	Armazena o id (este é fornecido via parâmetro da função), nome, atividade,
 telefone dentro de um dicionário;

⦁	Copiar o dicionário para dentro da lista_contatos (utilizar o copy);

⦁	Deve-se implementar uma função chamada consultar_contatos() que não recebe 
parâmetros e que: [EXIGÊNCIA DE CÓDIGO 4 de 8];

⦁	Deve-se perguntar qual opção deseja (1. Consultar Todos / 2. Consultar por
Id / 3. Consultar por Setor / 4. Retornar ao menu):

⦁	Se Consultar Todos, apresentar todos os contatos com todos os seus dados 
cadastrados;

⦁	Se Consultar por Id, solicitar ao usuário que informe um id, e apresentar 
o contato específico (apenas 1) com todos os seus dados cadastrados;

⦁	Se Consultar por Atividade, solicitar ao usuário que informe a atividade, 
e apresentar o(s) contato(s) que exercem aquela atividade com todos os seus 
dados cadastrados;

⦁	Se Retornar ao menu, deve-se retornar ao menu principal (return);

⦁	Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" 
e repetir a pergunta D.a.

⦁	Enquanto o usuário não escolher a opção 4, o menu consultar contatos deve 
se repetir.

⦁	Deve-se implementar uma função chamada remover_contato() em que: 
[EXIGÊNCIA DE CÓDIGO 5 de 8];

⦁	Deve-se pergunta pelo id do contato a ser removido;

⦁	Remover o contato da lista_contatos;

⦁	Se o id fornecido não for de um contato da lista, printar “Id inválido” e 
repetir a pergunta E.a.

⦁	Deve-se implementar uma estrutura de menu no código principal (main), ou 
seja, não pode estar dentro de função, em que: [EXIGÊNCIA DE CÓDIGO 6 de 8];

⦁	Deve-se pergunta qual opção deseja (1. Cadastrar Contato / 2. Consultar 
Contato / 3. Remover Contato / 4. Encerrar Programa):

⦁	Se Cadastrar Contato, incrementar em um id_ global e em seguida, chamar a 
função cadastrar_contato (id_ global);

⦁	Se Consultar Contato, chamar função consultar_contato ();

⦁	Se Remover Contato, chamar função remover_ contato ();

⦁	Se Encerrar Programa, sair do menu (e com isso acabar a execução do 
código);

⦁	Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida"
 e repetir a pergunta F.a.

⦁	Enquanto o usuário não escolher a opção 4, o menu deve se repetir.

⦁	Deve-se implementar uma lista de dicionários (uma lista contento 
dicionários dentro) [EXIGÊNCIA DE CÓDIGO 7 de 8];

⦁	Deve-se inserir comentários relevantes no código 
[EXIGÊNCIA DE CÓDIGO 8 de 8];

⦁	Deve-se apresentar na saída de console um cadastro do seu contato da 
seguinte forma: para nome informe seu nome completo (não usar apelidos ou 
abreviações), para atividade informar como estudante, e para telefone informe
 sua RU. [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 6];

⦁	Deve-se apresentar na saída de console um cadastro de mais 2 contatos com 
mesmo tipo de atividade (por exemplo: marceneiro, padeiro, pintor, pedreiro) 
[EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 6];

⦁	Deve-se apresentar na saída de console uma consulta de todos os contatos 
[EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 6];

⦁	Deve-se apresentar na saída de console uma consulta por código (id) de um 
dos contados [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 6];

⦁	Deve-se apresentar na saída de console uma consulta por atividade em que 2 
contatos exerçam a mesma atividade [EXIGÊNCIA DE SAÍDA DE CONSOLE 5 de 6];

⦁	Deve-se apresentar na saída de console uma remoção de um dos contatos e em 
seguida de uma consulta de todos os contatos, provando que o contato foi 
removido [EXIGÊNCIA DE SAÍDA DE CONSOLE 6 de 6];

'''
# [EXIGÊNCIA DE CÓDIGO 8 de 8] Código comentadinho :)
# [EXIGÊNCIA DE CÓDIGO 1 de 8] Apresentar em print nome completo.
print("\n---Sistema realizado por Maria Eduarda Gomes! <3---\n")

import copy

# Função simples apenas para exibir uma linha de separação.
def imprime_linha():
    print("---------------------------------------------------")

# Função que exibe o menu de opções de consulta.
def print_menu_consultar():
    imprime_linha()
    print("---------------------------------------------------")
    print("---------------- CONSULTAR CADASTRO -----------------")
    imprime_linha()
    print("--------- |    1 - Consultar todos        | ---------")
    print("--------- |    2 - Consultar por ID       | ---------")
    print("--------- |    3 - Consultar por Atividade| ---------")
    print("--------- |    4 - Retornar ao menu       | ---------")
    imprime_linha()

# [EXIGÊNCIA DE CÓDIGO 3 de 8] Função cadastrar contatos. Solicita o nome,
# a atividade e o telefone de cada um dos contatos.
def cadastrar_contato(id, lista_contatos):
    try:
        # Solicitando as informações do contato.
        nome_contato = input("Digite o nome do contato: ")
        atividade = input("Digite a atividade do contato: ")
        telefone_contato = input("Digite o telefone do contato: ")

        # Criando um novo dicionário com os dados do contato.
        novo_contato = {'id': id,
                        'Nome': nome_contato,
                        'Atividade': atividade,
                        'Telefone': telefone_contato}

        # Adicionando o dicionário à lista de contatos.
        lista_contatos.append(copy.deepcopy(novo_contato))
        
        # Incrementando o ID global.
        id += 1
        print("Contato cadastrado com sucesso!")
        return id
    except Exception as e:
        # Tratando possíveis erros.
        print(f"Erro de dado ({e}). Por favor, tente novamente")

# [EXIGÊNCIA DE CÓDIGO 4 de 8] Função para consultar contatos.
def consultar_contatos():
    while True:
        try:
            print_menu_consultar()
            escolha = int(input("Escolha uma opção: "))

            if escolha == 1:
                # Consultando e exibindo todos os contatos.
                for registro in lista_contatos:
                    for chave, valor in registro.items():
                        print(f"{chave}: {valor}")
                return
            elif escolha == 2:
                # Consultando contato por ID fornecido no Input.
                procura_id = int(input("Digite o n° do ID que você deseja " + 
                                       "procurar: "))
                resultado_pesquisa = next((contato 
                                           for contato in lista_contatos 
                                           if contato['id'] == procura_id), 
                                           None)
                if resultado_pesquisa:
                    print(resultado_pesquisa)
                else:
                    print("Contato não encontrado.")
            elif escolha == 3:
                # Consultando contato por atividade que exerce.
                atividade_procurada = input("Digite a atividade: ")
                resultado_pesquisa = [contato 
                                      for contato in lista_contatos 
                                      if contato['Atividade'] == 
                                      atividade_procurada]
                if resultado_pesquisa:
                    for contato in resultado_pesquisa:
                        print(contato)
                else:
                    print("Nenhum contato encontrado com essa atividade.")
            elif escolha == 4:
                # Retornando ao menu principal.
                return
            else:
                # Tratando opção inválida.
                print("Opção inválida. Tente novamente.")
        except ValueError:
            # Tratando erro de valor inválido.
            print("Entrada inválida. Por favor, insira um número.")

# [EXIGÊNCIA DE CÓDIGO 5 de 8] Função para remover contatos.
def remover_contato():
    while True:
        try:
            id_procurado = int(input("ID do contato a ser removido: "))
            resultado_pesquisa = next((contato for contato in lista_contatos 
                                       if contato['id'] == id_procurado), 
                                       None)
            if resultado_pesquisa:
                # Removendo o contato da lista.
                lista_contatos.remove(resultado_pesquisa)
                print("Contato removido com sucesso!")
                return
            else:
                # Tratando ID inválido.
                print("Id inválido. Tente novamente.")
        except ValueError:
            # Tratando erro de valor inválido.
            print("Entrada inválida. Por favor, insira um número.")

# Função principal com o menu de opções.
# [EXIGÊNCIA DE CÓDIGO 6 de 8] Estrutura de menu no código principal (main).
def main():
    global id_global
    while True:
        imprime_linha()
        print("-------------BEM VINDO AO GOMES E-COMMERCE-----------")
        imprime_linha()
        print("----------------- MENU DE CADASTROS -----------------")
        imprime_linha()
        print("--------- |   1 - Cadastrar Contato       | ---------")
        print("--------- |   2 - Consultar Contatos      | ---------")
        print("--------- |   3 - Remover Contato         | ---------")
        print("--------- |   4 - Encerrar Programa       | ---------")
        imprime_linha()
        
        try:
            opcao = int(input("Digite a opção desejada: "))

            if opcao == 1:
                # Cadastrando um novo contato.
                id_global = cadastrar_contato(id_global, lista_contatos)
            elif opcao == 2:
                # Consultando contatos.
                consultar_contatos()
            elif opcao == 3:
                # Removendo um contato.
                remover_contato()
            elif opcao == 4:
                # Encerrando o programa.
                print("Encerrando o programa. Até logo!")
                break
            else:
                # Tratando opção inválida.
                print("Opção inválida. Tente novamente.")
        except ValueError:
            # Tratando erro de valor inválido.
            print("Entrada inválida. Por favor, insira um número.")

# Início do programa
if __name__ == "__main__":
    print("Bem vindos à lista de contatos do Maria Eduarda Gomes")
    
    # [EXIGÊNCIA DE CÓDIGO 2 de 8] Inicializando a lista de contatos e o ID 
    # global com meu número de RU.
    lista_contatos = []
    id_global = 5129006 

    # [EXIGÊNCIA DE CÓDIGO 7 de 8] Adicionando contatos iniciais à lista.
    lista_contatos.append({'id': 5129005, 
                           'Nome': 'João Silva', 
                           'Atividade': 'Marketing', 
                           'Telefone': '(32)98624-4503'
                           })
    lista_contatos.append({'id': 5129004, 
                           'Nome': 'Maria Souza', 
                           'Atividade': 'Desenvolvedor', 
                           'Telefone': '(59)94871-6423'
                           })

    # Executando o programa principal.
    main()
