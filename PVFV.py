

def PV_val():
    i = (float)(input('What is the required rate as A PERCENTAGE?'))*.01
    print("i is ", i)
    n = (float)(input('What is THE NUMBER OF PERIODS?'))
    

    print("n is ", n)
    fv =(float)(input('What is the FUTURE VALUE?'))
    print("fv is ", fv)
    partA = ((1)/pow(i+1, n))
    print(partA)
    pv = partA *fv
    print("present value is ", pv)
    return pv


def FV_val():
##note: If compounding semiannually, don't forget to divide
##the i by two and double n

    n = (float)(input('What is THE NUMBER OF PERIODS?'))
    print("n is ", n)
    pv =(float)(input('What is the PRESENT VALUE?'))
    print("pv is ", pv)

    i = input('What is the required rate as A PERCENTAGE?')
    if (i=='?'):
        fv = (float)(input('What is THE future value?'))

        i = (pow((fv/pv), (1/n))) -1
        print("i is ", i)
        return i
    i = (float)(i)*.01
    print("i is ", i)
    fv = pv*(pow(i+1, n))
    print("future value is ", fv)
    return fv

def PV_Annuity():
    AType = input('Is this an ORDINARY ANNUITY(end of each period) or an ANNUITY DUE(start)? o or d')

    i = (float)(input('What is the required rate as A PERCENTAGE?'))*.01
    print("i is ", i)

    n = (float)(input('What is THE NUMBER OF PERIODS?'))
    if (AType=='d'):
        n = n-1
    print("n is ", n)





    a =(input('What is the ANNUITY?'))
    print("annuity is", a)

    if (a=='?'):
        pvA = (float)(input('What is THE present value of the annuity?'))
        print("future value of annuity is", a)
        AType = input('Is this an ORDINARY ANNUITY(end of each period) or an ANNUITY DUE(start)? o or d')
        if (AType=='d'):
            a = pvA/(((1-( 1/pow((1+i),n) ))/i)+1)
            print("Annuity is " , a)
            return a
        a = pvA/((1-( 1/pow((1+i),n) ))/i)
        print("Annuity is " , a)
        return a



    a = (float)(a)






    pA = pow((i+1), n)
    pB = 1/pA
    pC = 1 - pB
    pD = pC/i


    if (AType=='d'):
        pvAnn = a*(pD+1)
        print("present value of Annuity is",pvAnn)
        return pvAnn
    pvAnn = a*pD
    print("present value of Annuity is",pvAnn)
    return pvAnn

def FV_Annuity():
    AType = input('Is this an ORDINARY ANNUITY(end of each period) or an ANNUITY DUE(start)? o or d')

    i = (float)(input('What is the required rate as A PERCENTAGE?'))*.01



    print("i is ", i)

    n = (float)(input('What is THE NUMBER OF PERIODS?'))
    if (AType=='d'):
        n = n-1
    print("n is ", n)

    a =(input('What is the ANNUITY?'))
    print("annuity is", a)

    if (a=='?'):
        fvA = (float)(input('What is THE future value of the annuity?'))
        print("future value of annuity is", a)
        AType = input('Is this an ORDINARY ANNUITY(end of each period) or an ANNUITY DUE(start)? o or d')
        if (AType=='d'):
            a = fvA/((( pow((1+i),n) -1)/i)+1)
            print("Annuity is " , a)
            return a
        a = fvA/(( pow((1+i),n) -1)/i)
        print("Annuity is " , a)
        return a



    a = (float)(a)
    if (AType=='d'):
         fvAnn = a*((((pow(i+1, n) -1)/i)-1)+1)
         print ("future value of Anuuity is ", fvAnn)
         return fvAnn
    fvAnn = a*(((pow(i+1, n) -1)/i)-1)
    print ("future value of Anuuity is ", fvAnn)
    return fvAnn



##FV_Annuity()
##PV_Annuity()
PV_val()
##x = PV_Annuity() + PV_val()##use this to calculate bond price
##print(x)

##FV_val()

## a = pow(a,2)
## b = pow(b,2)
## c = pow(c,2)
## d = pow(d,2)
## e = pow(e,2)
##
## a = a*.2
## b = b*.2
## c = c*.2
## d = d*.2
## e = e*.2
## 
## print(a)
## print(b)
## print(c)
## print(d)
## print(e)
## 
## theSum = a + b + c + d + e