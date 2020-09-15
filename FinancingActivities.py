'''
ASSETS BELOW
'''

def getAccountsRec():##CURRENT ASSET
    yr1 = (float)(input('Accounts Receivable year 1'))
    yr2 = (float)(input('Accounts Receivable year 2'))

    ar = yr2 - yr1
    if (ar>0):
        print("accounts receivable has increased, DEDUCT", ar)
    else:
        print("accounts receivable has decreased, ADD", ar)

    return ar

def getInventory():##CURRENT ASSET
    yr1 = (float)(input('Inventory year 1'))
    yr2 = (float)(input('Inventory year 2'))

    i = yr2 - yr1
    if (i>0):
        print("inventory has increased, DEDUCT", i)
    else:
        print("inventory has decreased, ADD", i)

    return i

def getPrepaidEx():## CURRENT ASSET
    yr1 = (float)(input('Prepaid Expenses  year 1'))
    yr2 = (float)(input('Prepaid Expenses  year 2'))

    preEx = yr2 - yr1
    if (preEx>0):
        print("prepaid expenses has increased, DEDUCT", preEx)
    else:
        print("prepaid expenses has decreased, ADD", preEx)

    return preEx

'''
LIABILITIES BELOW
'''



def getAccountsPayable():## CURRENT LIABILITY
    yr1 = (float)(input('AccountsPayable  year 1'))
    yr2 = (float)(input('AccountsPayable  year 2'))

    accP = yr2 - yr1
    if (accP>0):
        print("AccountsPayable has increased, ADD", accP)
    else:
        print("AccountsPayable has decreased  , SUBTRACT", accP)

    return accP



def getAccruedEx():## CURRENT LIABILITY
    yr1 = (float)(input('AccruedEx  year 1'))
    yr2 = (float)(input('AccruedEx  year 2'))

    acc = yr2 - yr1
    if (acc>0):
        print("AccruedEx has increased, ADD", acc)
    else:
        print("AccruedEx has decreased  , SUBTRACT", acc)

    return acc

'''
OTHER
'''
def getDepExpense():
    depEx =(float)(input('please type in Depreciation Expense '))
    print('Depreciation expense is ', depEx)
    return depEx



def operatingActivities():
    ##NETINCOME IS A CURRENT ASSET
    netI =(float)(input('please type net income (earnings after taxes)'))

    ##ASSETS
    dep = getDepExpense()
    ar = getAccountsRec()
    i = getInventory()
    pEX = getPrepaidEx()

    ##LIABILITIES
    ap = getAccountsPayable()
    aEX = getAccruedEx()

    totalAssets = netI + dep - ar - i - pEX
    print ("total Assets ", totalAssets)

    totalLib = ap + aEX
    print ("total lib ", totalLib)

    total = totalAssets + totalLib
    print(total)



operatingActivities()