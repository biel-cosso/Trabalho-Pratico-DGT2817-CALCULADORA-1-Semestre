# Inicializa a variável de controle
saida = ''

# Funções para as operações básicas
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b

# Função principal da calculadora
def calculadora(num1, num2, operacao):
    operacao = operacao.lower()
    if operacao in ['+', 'soma']:
        resultado = adicao(num1, num2)
    elif operacao in ['-', 'subtracao']:
        resultado = subtracao(num1, num2)
    elif operacao in ['*', 'multiplicacao']:
        resultado = multiplicacao(num1, num2)
    elif operacao in ['/', 'divisao']:
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    return resultado

# Loop principal
while saida.lower() != 'n':
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação desejada (+, -, *, / ou nome da operação): ")
        resultado = calculadora(num1, num2, operacao)
        print(f"Resultado da operação: {resultado}")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos.")
    
    saida = input("Deseja continuar? (S/N): ")

