##ebit = 740000
##t = .35*ebt
##eat = ebt-t


def shareNum():
    ebit = (float)(input("ebit"))
    print("ebit is ",ebit)
    totalI = (float)(input("totalI"))
    print("totalI is ", totalI)
    ebt = (float)(ebit - totalI)
    tPer = (float)(input("tax percent"))*.01
    print("tPer is ",tPer)
    t = tPer*ebt
    eat = ebt - t
    print("eat is ", eat)
    sharesOld = (float)(input ("shares old"))
    print("sharesOld is ", sharesOld)
    sharesNew = (float)(input("amound of shares added/ new"))
    print("sharesNew is ", sharesNew)
    totalShares = sharesOld + sharesNew
    eps = eat/totalShares
    print("eps is " , eps)
    return eps

shareNum()