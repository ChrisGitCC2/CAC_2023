def maxcomdiv(a,b):

    mcd = False

    if a > 0 and b >0 and a != b:  

        if a > b:
                aux = a
                a=b
                b=aux
        i=a
            
        while mcd == False and i>=1:

                if a % i == 0 and b % i == 0:
                    #print ("El MCD ES " , i)
                    mcd = True
                    return i
                else:
                    i -= 1  

        


print ("El mcd es " , maxcomdiv(15,25))
print ("El mcd es " , maxcomdiv(27,9))
print ("El mcd es " , maxcomdiv(27,27))


                