
'''
Income Statement functions
'''
##1
def getSales():
    sales = (int)(input('please type in Sales (1st on Balance Sheet)'))
    print('sales is = ' , sales)
    return sales

##2
def getGoodsCost():
    goodsCost = (int)(input('please type in Cost of goods sold (2nd on Balance Sheet)'))
    print('Cost of Goods Sold is' ,goodsCost)
    return goodsCost

##3
def getGrossProfit(sales, goodsCost):
    gp = sales - goodsCost
    print('Gross Profit is ', gp)
    return gp

##4
def getSellAdmin():
    sAdmin = (int)(input('please type in Selling/ Administration Expense (4th on Balance Sheet)'))
    print('Selling and Admin Expense is', sAdmin)
    return sAdmin

##5
def getDepExpense():
    depEx =(int)(input('please type in Depreciation Expense (5th on Balance Sheet)'))
    print('Depreciation expense is ', depEx)
    return depEx

##6
def getOpProfit(gp, sa_Ex, dp_Ex):
    op_P =gp - sa_Ex - dp_Ex
    print('Operating Profit is ', op_P)
    return op_P

##7
def getInterestExpense():
    i_Ex = (int)(input('please type in Interest Expense (7th on Balance Sheet)'))
    print('interest expense is' , i_Ex)
    return i_Ex

##8
def getEbeforeT(op, i_Ex):
    ebeforeT = op - i_Ex
    print('Earnings before Taxes = ',ebeforeT)
    return ebeforeT

##9
def getTaxes():
    t = (int)(input('please type in Taxes (9th on Balance Sheet)'))
    print('taxes are = ' , t)
    return t

##10
def getEAfterT(ebeforeT, t):
    eAfterT = ebeforeT - t
    print('Earnings AFTER Taxes Or Net Income = ',eAfterT)
    return eAfterT

##11
def getPrefStockDiv():
    psd = (int)(input('please type in preferred stock dividends (11th on Balance Sheet)'))
    print('preferred stock dividends = ',psd)
    return psd

##12

def getstockEarnings(eat, psd):
    se = eat - psd
    print('earnings available to common stockholders = ',se)
    return se

##13

def getSharesO():
    sharesO = (int)(input('please type in  number of Shares outstanding (13th on Balance Sheet)'))
    print('shares Outstanding = ',sharesO)
    return sharesO

##14
def ePerShare(se,sharesO ):
    if (sharesO == 0):
        print("divided by 0 ")
        return -1
    eps = se/sharesO ##
    print('earnings per share = ',eps)
    return eps


'''
Cash Flow extra functions
'''
def equip_Price():
    ep = (int)(input('please type in  the price to purchase equipment (for Cash Flow Statement)'))
    print('price to purchase equipment = ',ep)
    return ep





def completeIncomeStatement():

    gp = getGrossProfit(getSales(), getGoodsCost())
    sa= getSellAdmin()
    dp = getDepExpense()
    op = getOpProfit(gp, sa, dp)
    i_Ex = getInterestExpense()
    ebt = getEbeforeT(op, i_Ex)
    t = getTaxes()
    eat = getEAfterT(ebt, t)##calculate net profit
    psd = getPrefStockDiv()
    se = getstockEarnings(eat, psd)
    so = getSharesO()
    eps = ePerShare(se, so)

    return eps



def cashFlow(): ##regular cash flows

    ##gp = getGrossProfit(getSales(), getGoodsCost())
    gp =(int)(input('gross profit'))
    print("gross profit is ", gp)
    sa= getSellAdmin()
    dp = getDepExpense()

    op = getOpProfit(gp, sa, dp)
    i_Ex = getInterestExpense()
    ebt = getEbeforeT(op, i_Ex)
    t = getTaxes()
    eat = getEAfterT(ebt, t)
    pe = equip_Price()
    amount = eat - pe
    print("Earnings after Taxes minus equipment price = ", amount)
    cashFlow = amount + dp
    print ("Cash Flow Amount is ", cashFlow)
    return cashFlow


def peRatio(): ##es  is earnings per share, market value per share
    es =(float)(input('Earnings per share'))
    print("es is", es)
    mValue = (float)(input('Market Value per share'))
    print ("mValue is ",mValue)
    pe = mValue/ es
    print (pe)
    return pe


completeIncomeStatement()

##peRatio()
