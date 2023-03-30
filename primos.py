n = int(input("Digite um número:"))
q = 0
for x in range(1,n):
    if(n % x == 0):
        q = q + 1;

if(q<3):
    print(n , " é um número primo!")
else:
    print(n , " não é um número primo!")
