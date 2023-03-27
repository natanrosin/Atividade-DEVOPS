print("Esta é a Loja Desconto da Cidade, bem-vindo! Aqui quem fala é Natan Willian Rosin")

print("Para iniciar vamos realizar uma analise de credito")

cargo = input("Informe seu cargo na empresa que trabalha atualmente: ")

salario = float(input("Informe seu salario: "))

Ano_de_nascimento =int(input("informe seu ano de nascimento: "))
from datetime import datetime
hoje = datetime.now()
ano = int(hoje.strftime("%Y"))
idade = (ano - Ano_de_nascimento)
limite=salario*(idade/1000) + 100

print("Seu cargo atual é {}".format(cargo))
print("Seu salario é {}".format(salario))
print("Seu ano de nascimento é {}".format(Ano_de_nascimento))
print("Sua idade é: ",idade,"anos")
print("Seu limite de credito é: ",limite,"reais")

# Etapa 3
Nome_do_produto = input("informe o nome do produto: ")
preco_do_produto = float(input("informe o preco do produto: "))
porcentagem=(preco_do_produto * 100)/ limite
primeiro_nome="Natan"
nome_completo="Natan Willian Rosin"
desconto=(preco_do_produto * int(len(primeiro_nome)))/100
produto_com_desconto=(preco_do_produto - desconto)

if preco_do_produto <= (limite * 0.60):
    print("liberado")
elif preco_do_produto > (limite * 0.60) and preco_do_produto < (limite * 0.90):
    print("liberado ao parcelar em até 2 vezes")
elif preco_do_produto >= (limite * 0.90) and preco_do_produto <= (limite * 1.00):
    print("liberado ao parcelar em 3 ou mais vezes")
else:
    print("bloqueado")
if preco_do_produto >= int(len(nome_completo)) and preco_do_produto <= idade:
    print("você terá um desconto de 5%")
    print("o valor do produto com desconto é: ", produto_com_desconto)

# Etapa 4

def obter_limite():
    print("Esta é a Loja Desconto da Cidade, bem-vindo! Aqui quem fala é Natan Willian Rosin")
    print("Para iniciar vamos realizar uma analise de credito")
    cargo = input("Informe seu cargo na empresa que trabalha atualmente: ")
    salario = float(input("Informe seu salario: "))
    Ano_de_nascimento =int(input("informe seu ano de nascimento: "))
    from datetime import datetime
    hoje = datetime.now()
    ano = int(hoje.strftime("%Y"))
    idade = (ano - Ano_de_nascimento)
    limite=salario*(idade/1000) + 100
    print("Seu cargo atual é {}".format(cargo))
    print("Seu salario é {}".format(salario))
    print("Seu ano de nascimento é {}".format(Ano_de_nascimento))
    print("Sua idade é: ",idade,"anos")
    print("Seu limite de credito é: ",limite,"reais")
    return limite,idade
def verificar_produto(limite):
    Nome_do_produto = input("informe o nome do produto: ")
    preco_do_produto = float(input("informe o preco do produto: "))
    porcentagem=(preco_do_produto * 100)/ limite
    primeiro_nome="Natan"
    nome_completo="Natan Willian Rosin"
    desconto=(preco_do_produto * int(len(primeiro_nome)))/100
    produto_com_desconto=(preco_do_produto - desconto)
    saldo = limite - preco_do_produto

    if preco_do_produto <= (limite * 0.60):
        print("liberado")
    elif preco_do_produto > (limite * 0.60) and preco_do_produto < (limite * 0.90):
        print("liberado ao parcelar em até 2 vezes")
    elif preco_do_produto >= (limite * 0.90) and preco_do_produto <= (limite * 1.00):
        print("liberado ao parcelar em 3 ou mais vezes")
    else:
        print("bloqueado")
    if preco_do_produto >= int(len(nome_completo)) and preco_do_produto <= idade:
        print("você terá um desconto de 5%")
        print("o valor do produto com desconto é: ", produto_com_desconto)
    return saldo
limite,idade = obter_limite()
Quantidade_de_produto = int(input("Quantidade de produtos que deseja cadastrar: "))
print("Quantidade de produtos solicitados para cadastro é: ", Quantidade_de_produto)
for Quantidade_de_produto in range(Quantidade_de_produto):
    saldo = verificar_produto(limite)
    limite = saldo
    print("Você ainda pode gastar: ", saldo)
