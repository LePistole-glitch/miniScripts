A = int(input("Numero: "))
cont = 0

while True:
    if A % 2 == 0:
        A = A / 2
        cont = cont + 1
        print(A)
    else:
        A = 3*(A) + 1
        cont = cont + 1
        print(A)
    if A == 1:
        cont = cont + 1
        break

print("Iteraciones: "+str(cont))