'''
############################################################# PLANO DE SAÚDE:
Imagina-se que você é um dos programadores responsáveis pela construção
de app para uma empresa X que vende Planos de Saúde. Uma das estratégias 
dessa empresa X é cobrar um valor diferente com base na idade do cliente, 
conforme a listagem abaixo:

⦁	Se a idade for maior ou igual que 0 e menor que 19, 
o valor será de 100% do valor base do plano (100 / 100);

⦁	Se a idade for maior ou igual que 19 e menor que 29, 
o valor será de 150% do valor base do plano (150 / 100);

⦁	Se a idade for maior ou igual que 29 e menor que 39, 
o valor será de 225% do valor base do plano (225 / 100);

⦁	Se a idade for maior ou igual que 39 e menor que 49, 
o valor será de 240% do valor base do plano (240 / 100);

⦁	Se a idade for maior ou igual que 49 e menor que 59, 
o valor será de 350% do valor base do plano (350 / 100);

⦁	Se a idade for maior ou igual que 59, 
o valor será de 600% do valor base do plano (600 / 100);

O valor mensal do plano é calculado da seguinte maneira:

Exemplo: 
Se o valor_base informado for 100.00 e a idade for 45 anos 
(240% segundo a tabela acima)

#################################################### ELABORE UM PROGRAMA QUE:
⦁	Deve-se implementar o print com o seu nome completo (somente print, 
não usar input aqui). Por exemplo: print(“Sistema desenvolvido por Bruno 
Kostiuk”) [EXIGÊNCIA DE CÓDIGO 1 de 6];

⦁	Deve-se implementar o input do valor_base do plano e da idade do 
cliente [EXIGÊNCIA DE CÓDIGO 2 de 6];

⦁	Deve-se implementar as regras de valores conforme a enunciado acima 
(obs.: atente-se as condições de menor, igual e maior) [EXIGÊNCIA DE CÓDIGO 3 de 6];

⦁	Deve-se implementar o valor_mensal [EXIGÊNCIA DE CÓDIGO 4 de 6];

⦁	Deve-se implementar as estruturas if, elif e else (todas elas) 
[EXIGÊNCIA DE CÓDIGO 5 de 6];  

⦁	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 
6 de 6];

⦁	Deve-se apresentar na saída de console uma mensagem com seu nome completo
[EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 2];

⦁	Deve-se apresentar na saída de console a utilização do sistema informando 
uma idade maior ou igual a 29 anos, apresentando na saída de console o 
valor_mensal do plano [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 2];  
'''
# [EXIGÊNCIA DE CÓDIGO 6 de 6] Comentários relevantes
# [EXIGÊNCIA DE CÓDIGO 1 de 6] Nome completo.
print("\n---Sistema realizado por Maria Eduarda Gomes! <3---\n")

# Função para exibir uma linha de separação.
def imprime_linha():
    print("---------------------------------------------------")

# Print inicial
imprime_linha()
print("--------BEM VINDO AO GOMES HEALTH AND CARE---------")
imprime_linha()

# Variável de controle de erro
erro = False

# Entrada de dados com tratamento de erro
try:
    # [EXIGÊNCIA DE CÓDIGO 2 de 6] Input da idade e valor base
    idade_cliente = int(input("Para começar, informe a idade do cliente: "))
    valor_base = float(input("Informe o valor base do plano de saúde: R$"))

    # [EXIGÊNCIA DE CÓDIGO 3 de 6] Verificação da faixa etária
    # [EXIGÊNCIA DE CÓDIGO 5 de 6] Usando IF, ELIF e ELSE
    if idade_cliente >= 0 and idade_cliente < 19:
        print("Faixa etária de 0 a 18 anos.")
        valor_faixa_etaria = 1.00
    elif idade_cliente >= 19 and idade_cliente < 29:
        print("Faixa etária de 19 a 28 anos.")
        valor_faixa_etaria = 1.50
    elif idade_cliente >= 29 and idade_cliente < 39:
        print("Faixa etária de 29 a 38 anos.")
        valor_faixa_etaria = 2.25
    elif idade_cliente >= 39 and idade_cliente < 49:
        print("Faixa etária de 39 a 48 anos.")
        valor_faixa_etaria = 2.40
    elif idade_cliente >= 49 and idade_cliente < 59:
        print("Faixa etária de 49 a 58 anos.")
        valor_faixa_etaria = 3.50
    elif idade_cliente >= 59:
        print("Faixa etária acima de 59 anos.")
        valor_faixa_etaria = 6.00
    else:
        print("Erro de valor. Por favor, tente novamente.")
        erro = True

except ValueError:
    print("Erro de valor. Por favor, insira valores numéricos válidos.")
    erro = True

if not erro:
    imprime_linha()

    # [EXIGÊNCIA DE CÓDIGO 4 de 6] Implementando o valor mensal
    valor_mensal = valor_base * valor_faixa_etaria
    print(f"O valor mensal do plano é de: R${valor_mensal:.2f}")
