def myPi(n):
    denominator = 1
    addto = 1

    for i in range(n):
        denominator = denominator + 2
        addto = addto - (1/denominator)
        denominator = denominator + 2
        addto = addto + (1/denominator)
    print(addto)
    pi = addto * 4

    return(pi)
n = int(input(""))
print(myPi(n))