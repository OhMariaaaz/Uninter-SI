'''
########################################################### PIZZARIA SABORES:
Você e sua equipe de programadores foram contratados para desenvolver um app 
de vendas para uma Pizzaria que vende sabores de Pizzas Doces e Pizzas 
Salgadas. Você ficou com a parte de desenvolver a interface do cliente para 
retirada do produto.

A Loja possui seguinte relação:
⦁	Tamanho P: Pizza Salgada (PS) custa 30 reais e a Pizza Doce (PD) custa 
34 reais;

⦁	Tamanho M: Pizza Salgada (PS) custa 45 reais e a Pizza Doce (PD) custa 
48 reais;

⦁	Tamanho G: Pizza Salgada (PS) custa 60 reais e a Pizza Doce (PD) custa 
66 reais;

#################################################### ELABORE UM PROGRAMA QUE:
⦁	Deve-se implementar o print com o seu nome completo (somente print, não 
usar input aqui). 

Por exemplo: print(“Bem-vindos a Pizzaria do Bruno Kostiuk”) 
Além do seu nome completo, deve-se implementar um print com um Menu para o 
cliente. [EXIGÊNCIA DE CÓDIGO 1 de 8];

⦁	Deve-se implementar o input do sabor (PS/PD) e o print “Sabor inválido. 
Tente novamente" se o usuário entra com valor diferente de PS e PD [EXIGÊNCIA
 DE CÓDIGO 2 de 8];

⦁	Deve-se implementar o input do tamanho (P/M/G) e o print “Tamanho inválido
. Tente novamente" se o usuário com entra valor diferente de P, M ou G [
EXIGÊNCIA DE CÓDIGO 3 de 8];

⦁	Deve-se implementar if, elif e/ou else, utilizando o modelo aninhado (aula
 3 - Tema 4) com cada uma das combinações de sabor e tamanho [EXIGÊNCIA DE 
 CÓDIGO 4 de 8];

⦁	Deve-se implementar um acumulador para somar os valores dos pedidos (valor
 total do pedido) [EXIGÊNCIA DE CÓDIGO 5 de 8];

⦁	Deve-se implementar o input com a pergunta: “Deseja pedir mais alguma 
coisa?”. Se sim repetir a partir do item B, senão encerrar o programa executar
 o print do acumulador [EXIGÊNCIA DE CÓDIGO 6 de 8];

⦁	Deve-se implementar as estruturas de while, break, continue (todas elas) [
EXIGÊNCIA DE CÓDIGO 7 de 8];

⦁	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de
 8];

⦁	Deve-se apresentar na saída de console uma mensagem com o seu nome 
completo e o menu para o cliente conhecer as opções  [EXIGÊNCIA DE SAÍDA DE 
CONSOLE 1 de 4];

⦁	Deve-se apresentar na saída de console um pedido em que o usuário errou o
sabor [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4];

⦁	Deve-se apresentar na saída de console um pedido em que o usuário errou o
tamanho [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];

⦁	Deve-se apresentar na saída de console um pedido com duas opções sabores 
diferentes e com tamanhos diferentes [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];  
'''
# [EXIGÊNCIA DE CÓDIGO 8 de 8] Código comentadinho :)
# [EXIGÊNCIA DE CÓDIGO 1 de 8] Apresentar em print nome completo.
print("\n---Sistema realizado por Maria Eduarda Gomes! <3---\n")

# Função para exibir uma linha de separação.
def imprime_linha():
    print("---------------------------------------------------")

# Print inicial
imprime_linha()
print("--------------BEM VINDO AO GOMES PIZZAS------------")
imprime_linha()

# Exibir o cardápio
def exibir_menu():
    print("----------------------CARDÁPIO---------------------")
    imprime_linha()
    print("-| TAMANHO | PIZZA SALGADA (PS) | PIZZA DOCE(PD) |-")
    print("-|    P    |       R$ 30.00     |    R$ 34.00    |-")
    print("-|    M    |       R$ 45.00     |    R$ 48.00    |-")
    print("-|    G    |       R$ 60.00     |    R$ 66.00    |-")
    imprime_linha()

# Exibir o valor final
def exibir_valor_final(valor_total):
    imprime_linha()
    print("------------- DADOS FINAIS DO PEDIDO: -------------")
    imprime_linha()
    print(f"Valor final do pedido: R$ {valor_total:.2f}")
    imprime_linha()

# Variável do valor total
valor_total = 0

# [EXIGÊNCIA DE CÓDIGO 7 de 8] Laço para inserir pizzas ao pedido
while True:
    exibir_menu()

    # [EXIGÊNCIA DE CÓDIGO 2 de 8] Solicitar sabor da pizza
    sabor_pizza = input("\nDigite o código do sabor de pizza desejada " +
                        "(Pizza Salgada - PS | Pizza Doce - PD): ").upper()
    
    # Laço repetido se valor incorreto
    if sabor_pizza not in ("PD", "PS"):
        print("Sabor inválido. Tente novamente.")
        continue
    
    # [EXIGÊNCIA DE CÓDIGO 3 de 8] Solicitar tamanho da pizza
    tamanho_pizza = input("\nDigite o código do tamanho pizza desejada " +
                          "(Pequena - P | Média - M | Grande - G): ").upper()
    
    # Laço repetido se valor incorreto
    if tamanho_pizza not in ("P", "M", "G"):
        print("Tamanho inválido. Tente novamente.")
        continue

    # [EXIGÊNCIA DE CÓDIGO 4 de 8] Usando If, Elif e Else
    if sabor_pizza == "PS" and tamanho_pizza == "P":
        valor_pizza = 30
        descricao_pizza = "Pizza Salgada Pequena" 
    elif sabor_pizza == "PS" and tamanho_pizza == "M":
        valor_pizza = 45
        descricao_pizza = "Pizza Salgada Média" 
    elif sabor_pizza == "PS" and tamanho_pizza == "G":
        valor_pizza = 60
        descricao_pizza = "Pizza Salgada Grande"
    elif sabor_pizza == "PD" and tamanho_pizza == "P":
        valor_pizza = 34
        descricao_pizza = "Pizza Doce Pequena"
    elif sabor_pizza == "PD" and tamanho_pizza == "M":
        valor_pizza = 48
        descricao_pizza = "Pizza Doce Média"
    else:
        valor_pizza = 66
        descricao_pizza = "Pizza Doce Grande"

    # [EXIGÊNCIA DE CÓDIGO 5 de 8] Incrementar valor total
    valor_total += valor_pizza

    imprime_linha()
    # Preview da pizza escolhida e valor atual do pedido
    print(f"Você escolheu a pizza: {descricao_pizza}")
    print(f"Valor da pizza: R$ {valor_pizza:.2f}")
    print(f"Valor total do pedido: R$ {valor_total:.2f}")
    imprime_linha()

    # [EXIGÊNCIA DE CÓDIGO 6 de 8] Finalizar pedido ou continuar
    if input("Deseja adicionar mais pizzas ao pedido? (Pressione 'S' - Sim " +
             "| Pressione qualquer tecla - Não): ").upper() != "S":
        break

exibir_valor_final(valor_total)
