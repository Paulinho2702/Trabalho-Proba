
def Fatorial(i):
    F = 1
    while (i>1):
        F = F * i
        i = i-1
    return F    

def Calcula(x, n, p):
    q = 1 - p
    Cnx = (Fatorial(n)) // ((Fatorial(n-x)) * (Fatorial(x)))
    return Cnx * (p**x) * (q**(n-x))

def CalculaB(x,n,p):
    z=0
    for x in range(x+1):
        z+= Calcula(x, n, p)
    return z

x = int(input("Digite o número de tentativas: "))

n = int(input("Digite o número de sucessos: "))

p = float(input("Digite a porcentagem de sucessos em valor absoluto: "))


prob1 = Calcula(x,n,p)
print(f"O número binomial individual é: {prob1:.2%}")
prob2 = CalculaB(x,n,p)
print(f"O número binomial acumulado é: {prob2:.2%}")