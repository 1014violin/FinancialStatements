class BalanceSheet (object):
    def __init__(self):
        self = self

    #def currAssets(self, cash, accRe, inventory, preExpenses):
        #cAssets = cash + accRe + inventory + preExpenses
        #return cAssets

    def currAssets(self, cash, accRe, inventory, preExpenses):
        tassets = cash + accRe + inventory +  preExpenses
        return tassets

##     def fixedAssets(self, GrossPEQ, accDep, NetPEQ):
##         tassets = (GrossPEQ-accDep)+NetPEQ
##         return tassets


    def __str__(self):
        return "currAssets =   " + str(self.currAssets(cash, accRe, inventory, preExpenses))  #"\n" + "fixed assets" + #str(self.fixedAssets(GrossPEQ, accDep, NetPEQ))


def main():
    bs = BalanceSheet()
    bs.currAssets(14000, 555, 5555, 4444433)
    #bs.fixedAssets(3333, 8888, 4443)
    print (bs)




main()





