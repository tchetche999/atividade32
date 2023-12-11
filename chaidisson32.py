def calcSalario(a):
    a = a+(a*(15/100))
    print(f'Com o aumento, seu salário agora é de R${a}')
salario = float(input("Digite seu salário: "))
calcSalario(salario)