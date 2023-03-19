#minimo comun multiplo

def mcm(n1,n2):
    x = max(n1,n2)

    while True:
        if (x % n1 ==0) and (x% n2 ==0):
            return x
        x +=1

  

print(mcm(10 ,90))
print(mcm(45 , 9))
print(mcm(8 , 0))
print(mcm(27 , -4))
