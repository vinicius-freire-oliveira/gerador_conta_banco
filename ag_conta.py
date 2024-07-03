""" Requisitos:
- Agência bancária = 4 dígitos mais dígito verificador - XXXX-X
- Conta bancária = 6 díditos mais dígito verificdor = XXXXXX-X
- Cartão Crédito = 16 dígítos divididos em 4 grupos de 4 dígitos sendo:
 * Os primeiros seis dígitos servem para identificar a bandeira (Visa, MasterCard, etc.), o banco emissor (Caixa, Banco do Brasil, Itau, etc.) e a sua função (crédito, débito ou múltiplo).
 * O primeiro dígito indica a bandeira:
  # American Express- começam com 3
  # Visa - começam com 4
  # Mastercard - começam com 5
 * Todos os números de cartão de crédito podem começar apenas por 3, 4, 5 e 6. 
 * Os próximos nove dígitos servem para identificar o cliente, sua agência bancaria e outros dados pessoais, como as bandeiras das quais está autorizado a utilizar. Já o último dígito é um digito verificador. """

# Importação dos módulos necessários
import random  # Módulo para geração de números aleatórios
import string  # Módulo para manipulação de strings

# Classe para gerar documentos bancários brasileiros
class GeradorBR:
    # Método estático para gerar um número de conta bancária
    @staticmethod
    def gerar_conta_bancaria():
        # Geração dos dígitos aleatórios para o número da conta (6 dígitos)
        numero_conta = ''.join(random.choices(string.digits, k=6))
        # Geração de um dígito aleatório para o dígito verificador
        digito_verificador = random.choice(string.digits)

        # Retorna o número da conta formatado
        return f"{numero_conta}-{digito_verificador}"

    # Método estático para gerar um número de agência bancária
    @staticmethod
    def gerar_agencia():
        # Geração dos dígitos aleatórios para o número da agência (4 dígitos)
        numero_agencia = ''.join(random.choices(string.digits, k=4))
        # Geração de um dígito aleatório para o dígito verificador
        digito_verificador = random.choice(string.digits)

        # Retorna o número da agência formatado
        return f"{numero_agencia}-{digito_verificador}"

    # Método estático para gerar um número de cartão bancário
    @staticmethod
    def gerar_cartao_bancario():
        # Seleção aleatória da bandeira do cartão (4 para Visa, 5 para MasterCard, 6 para American Express)
        bandeira = random.choice(["4", "5"])

        # Geração dos dígitos do cliente (9 dígitos)
        numeros_cliente = ''.join(random.choices(string.digits, k=8))

        # Geração dos dígitos restantes (6 dígitos)
        numeros_restantes = ''.join(random.choices(string.digits, k=6))

        # Concatenação dos números para formar os 16 dígitos
        numero_cartao_sem_dv = bandeira + numeros_cliente + numeros_restantes[:6]

        # Cálculo do dígito verificador usando o algoritmo de Luhn
        soma = 0
        invertido = numero_cartao_sem_dv[::-1]
        for i, d in enumerate(invertido):
            digito = int(d)
            if i % 2 == 0:
                digito *= 2
                if digito > 9:
                    digito -= 9
            soma += digito
        digito_verificador = (10 - (soma % 10)) % 10

        # Adiciona o dígito verificador ao número do cartão
        numero_cartao = numero_cartao_sem_dv + str(digito_verificador)

        # Divisão do número do cartão em grupos de 4 dígitos para formatação
        grupos = [numero_cartao[i:i+4] for i in range(0, len(numero_cartao), 4)]
        numero_formatado = ' '.join(grupos)

        # Criação da representação com os quatro últimos dígitos visíveis
        numero_formatado_visivel = f"**** **** **** {numero_cartao[-4:]}"

        # Retorna as duas representações do número do cartão
        return numero_formatado, numero_formatado_visivel

# Função para simular a geração dos documentos bancários
def simular_documentos():
    print("Simulação de Documentos Bancários\n")
    print("Número da Conta Bancária:", GeradorBR.gerar_conta_bancaria())  # Gera e exibe um número de conta bancária
    print("Número da Agência:", GeradorBR.gerar_agencia())  # Gera e exibe um número de agência bancária
    numero_cartao_formatado, numero_cartao_visivel = GeradorBR.gerar_cartao_bancario()
    print("Número do Cartão Bancário:", numero_cartao_formatado)  # Gera e exibe um número de cartão bancário formatado
    print("Número do Cartão Bancário (visível):", numero_cartao_visivel)  # Exibe a representação com os quatro últimos dígitos visíveis

# Executar a simulação
simular_documentos()

