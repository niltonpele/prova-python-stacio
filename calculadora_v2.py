# Variável de controle para saída do loop
saida = ''

# Função para adição
def adicao(a, b):
    return a + b

# Função para subtração
def subtracao(a, b):
    return a - b

# Função para multiplicação
def multiplicacao(a, b):
    return a * b

# Função para divisão
def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b

# Função calculadora
def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao.lower() == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    return resultado

# Loop principal
while saida.lower() != 'n':
    # Solicita os números e a operação do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, / ou o nome da operação): ")
    
    # Chama a função calculadora e imprime o resultado
    resultado = calculadora(num1, num2, operacao)
    print("Resultado da operação:", resultado)
    
    # Pergunta ao usuário se deseja continuar
    saida = input("Deseja continuar? (S/N): ")