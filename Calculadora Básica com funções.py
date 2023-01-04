n1 = float(input('Insira o primeiro valor: '))
n2 = float(input('Insira o segundo valor: '))
op = (input('Insira o Sinal da Operação: '))

def soma (a,b):
    resultado = n1+n2
    return (resultado)

def diminui (a,b):
    resultado = n1-n2
    return (resultado)

def mult (a,b):
    resultado = n1*n2
    return (resultado)

def divide (a,b):
    resultado = n1/n2
    return (resultado)

if op == "+":
    print(f"\n O resultado da operação {n1} {op} {n2} é: {soma(n1,n2)}")

if op == "-":
    print(f"\n O resultado da operação {n1} {op} {n2} é: {diminui(n1,n2)}")

if op == "*":
    print(f"\n O resultado da operação {n1} {op} {n2} é: {mult(n1,n2)}")

if op == "/":
    print(f"\n O resultado da operação {n1} {op} {n2} é: {divide(n1,n2)}")