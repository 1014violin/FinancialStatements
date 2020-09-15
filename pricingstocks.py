def getKE_cm():

    d = (float)(input ("please type in the dividend"))
    print("d is ", d)

    po = (float)(input("please type in the price of the stock"))
    print("Po is ",po)
    g = (float) (input("please type in the growth rate as a percent"))*.01
    print("G is ",g)

    partA = d + (po*g)
    partB = partA / po

    print( "KE is ",partB)
    return partB



def getPO_cm():

    d = (float)(input ("please type in the dividend"))
    print("d is ", d)

    ke = (float)(input("please type in the ke"))*.01
    print("ke is ",ke)
    g = (float) (input("please type in the growth rate as a percent"))*.01
    print("G is ",g)
    po = d/(ke-g)
    print("po is ",po)

    return po




po = getPO_cm()