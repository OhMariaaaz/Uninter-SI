'''
################################################################# MADEIREIRA:
Você foi contratado para desenvolver um sistema de Venda de uma Empresa Y que
vende toras de arvore para outras empresas que vendem madeira. Você ficou com
a parte de desenvolver a interface com o cliente.
A Empresa Y opera as vendas da seguinte maneira:

⦁	Tora de Pinho (PIN), o valor do metro cúbico (m³) é de 150.40;
⦁	Tora de Peroba (PER), o valor do metro cúbico (m³) é de 170.20;
⦁	Tora de Mogno (MOG), o valor do metro cúbico (m³) é de 190.90;
⦁	Tora de Ipê (IPE), o valor do metro cúbico (m³) é de 210.10; 
⦁	Tora de Imbuia (IMB), o valor do metro cúbico (m³) é de 220.70;

⦁	Se a quantidade (em m³) de toras for menor que 100 não há desconto na
venda (0/100);
⦁	Se a quantidade (em m³) de toras for igual ou maior que 100 e menor que
500, o desconto será de 4% (4/100);
⦁	Se a quantidade (em m³) de toras for igual ou maior que 500 e menor que
1000, o desconto será de 9% (9/100);
⦁	Se a quantidade (em m³) de toras for igual ou maior que 1000 e menor ou
igual que 2000, o desconto será de 16% (16/100);
⦁	Se a quantidade (em m³) de toras for maior que 2000, não é aceito pedidos
com essa quantidade de toras;
	
⦁	Para o adicional de transporte rodoviário (1) é cobrado um valor extra de
1000 reais;
⦁	Para o adicional de transporte ferroviário (2) é cobrado um valor extra de
2000 reais;
⦁	Para o adicional de transporte hidroviário (3) é cobrado um valor extra de
2500 reais;

O valor final da conta é calculado da seguinte maneira:

total = ((tipoMadeira * qtdToras)*(1-desconto)) + transporte

#################################################### ELABORE UM PROGRAMA QUE:
⦁	Deve-se implementar o print com o seu nome completo (somente print, não
usar input aqui). 
Por exemplo: print(“Bem-vindos a Madeireira do Lenhador Bruno Kostiuk”)
[EXIGÊNCIA DE CÓDIGO 1 de 7];

⦁	Deve-se implementar a função escolha_tipo() que não recebe parâmetros e
que:[EXIGÊNCIA DE CÓDIGO 2 de 7];
    ⦁	Pergunta o tipo de madeira desejado;
    ⦁	Retorna o VALOR do tipo de madeira com base na escolha do usuário (use
    return);
    ⦁	Repete a pergunta do item B.a se digitar uma opção diferente de:
    PIN/PER/MOG/IPE/IMB;
    ⦁	Deve-se implementar a função qtd_toras() que não recebe parâmetros e
    que: [EXIGÊNCIA DE CÓDIGO 3 de 7];
    ⦁	Pergunta a quantidade de toras;
    ⦁	Retorna (use return) a quantidade de toras E o valor do desconto (os
    dois valores) seguindo a regra do enunciado;
    ⦁	Repete a pergunta do item C.a se digitar um valor acima de 2000 ou
    valor não numérico (use try/except para não numérico)

⦁	Deve-se implementar a função transporte() que não recebe parâmetros e que:
[EXIGÊNCIA DE CÓDIGO 4 de 7];
    ⦁	Pergunta pelo serviço adicional de transporte;
    ⦁	Retorna (use return) o valor de apenas uma das opções de transporte;
    ⦁	Repetir a pergunta item D.a se digitar uma opção diferente de: 1/2/3;

⦁	Deve-se implementar o total a pagar no código principal (main), ou seja,
não pode estar dentro de função, conforme o enunciado [EXIGÊNCIA DE CÓDIGO 5
de 7];

⦁	Deve-se implementar try/except [EXIGÊNCIA DE CÓDIGO 6 de 7];

⦁	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 7 de
 7];

⦁	Deve-se apresentar na saída de console uma mensagem com o seu nome
completo [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];

⦁	Deve-se apresentar na saída de console um pedido no qual o usuário errou
a opção de tipo de madeira [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4];

⦁	Deve-se apresentar na saída de console um pedido no qual o usuário digitou
um valor que ultrapasse a quantidade máxima de toras aceitas (2000) [EXIGÊNCIA
DE SAÍDA DE CONSOLE 3 de 4];

⦁	Deve-se apresentar na saída de console um pedido com opção de tipo de
madeira, quantidade de toras e transporte válidos [EXIGÊNCIA DE SAÍDA DE
CONSOLE 4 de 4];

'''
# [EXIGÊNCIA DE CÓDIGO 1 de 6] Apresentar em print nome completo.
print("\n---Sistema realizado por Maria Eduarda Gomes! <3---\n")

# Função simples apenas para exibir uma linha de separação.
def imprime_linha():
    print("---------------------------------------------------")

# Frescura
imprime_linha()
print("-------------BEM VINDO AO GOMES TORA&PAU-----------")
imprime_linha()
print("-----------------MENU DE ENCOMENDAS----------------")
imprime_linha()
print("-----------| CÓDIGO | TIPO DE MADEIRA |------------")
print("-----------|  PIN   |  Tora de Pinho  |------------")
print("-----------|  PER   |  Tora de Peroba |------------")
print("-----------|  MOG   |  Tora de Mogno  |------------")
print("-----------|  IPE   |  Tora de Ipê    |------------")
print("-----------|  IMB   |  Tora de Imbuia |------------")
imprime_linha()

def escolha_tipo_madeira():
    tipos_madeiras = {
        'PIN': {'Valor Base da Madeira': 150.40, 
                'Descrição do Tipo': 'Tora de Pinho'},
        'PER': {'Valor Base da Madeira': 170.20, 
                'Descrição do Tipo': 'Tora de Peroba'}, 
        'MOG': {'Valor Base da Madeira': 190.90, 
                'Descrição do Tipo': 'Tora de Mogno'},
        'IPE': {'Valor Base da Madeira': 210.10, 
                'Descrição do Tipo': 'Tora de Ipê'},
        'IMB': {'Valor Base da Madeira': 220.70, 
                'Descrição do Tipo': 'Tora de Imbuia'}
    }

    while True:
        imprime_linha()
        try:
            escolha_madeira = input("Qual o tipo de madeira que você deseja" +
                      "(PIN/PER/MOG/IPE/IMB)?: ").upper()
            if escolha_madeira in tipos_madeiras:
                imprime_linha()
                return tipos_madeiras[escolha_madeira]
            else:
                print("Escolha inválida! Tente novamente.")
        except ValueError:
            print("Escolha inválida! Tente novamente.")

def qtde_toras():
    LIMITE_QUANTIDADE = 2000
    DESCONTOS = {
        (0, 100): 0,
        (100, 500): 0.04,
        (500, 1000): 0.09,
        (1000, LIMITE_QUANTIDADE): 0.16
    }

    while True:
        imprime_linha()
        try:
            qtde_tora = int(input("Qual a quantidade desejada de toras " +
                                  "em m³?: "))
            if qtde_tora <= 0:
                print("A quantidade deve ser um número positivo. Tente " +
                      "novamente.")
                continue
            if qtde_tora <= LIMITE_QUANTIDADE:
                for intervalo, desconto in DESCONTOS.items():
                    if intervalo[0] <= qtde_tora < intervalo[1]:
                        break
                imprime_linha()
                info_pedido = {
                    'Quantidade de Toras': qtde_tora, 
                    'Desconto': desconto}
                return info_pedido
            else:
                print("Não aceitamos pedidos acima de 2000! Por favor, " +
                      "insira a quantidade novamente.")
        except ValueError:
            print("Escolha inválida! Tente novamente.")

def transporte():
    meio_transporte = {
        1: {'Meio de Transporte': 'Transporte Rodoviário', 
            'Valor Adicional de Transporte': 1000}, 
        2: {'Meio de Transporte': 'Transporte Ferroviário', 
            'Valor Adicional de Transporte': 2000}, 
        3: {'Meio de Transporte': 'Transporte Hidroviário', 
            'Valor Adicional de Transporte': 3000},
    }

    while True:
        imprime_linha()
        try:
            transporte_escolhido = int(input(
                "Qual será a forma de transporte?\n" +
                "1 - Transporte Rodoviário  - R$ 1000.00\n" +
                "2 - Transporte Ferroviário - R$ 2000.00\n" +
                "3 - Transporte Hidroviário - R$ 3000.00\n"
            ))
            imprime_linha()
            if transporte_escolhido in meio_transporte:
                return meio_transporte[transporte_escolhido]
            else:
                print("Escolha inválida! Tente novamente.")
        except ValueError:
            print("Escolha inválida! Tente novamente.")

pedido = {}

for chave, item in escolha_tipo_madeira().items():
    pedido[chave] = item

for chave, item in qtde_toras().items():
    pedido[chave] = item

for chave, item in transporte().items():
    pedido[chave] = item

pedido['total'] = (
    (pedido['Valor Base da Madeira'] * pedido['Quantidade de Toras'])
    *(1-pedido['Desconto'])) + pedido['Valor Adicional de Transporte']

imprime_linha()
print("------------- DADOS FINAIS DO PEDIDO: -------------")
imprime_linha()
for chave, valor in pedido.items():
    print(f"{chave}: {valor}")
imprime_linha()
