
from MicahStockAPI import getFreeCashFlow, getDebtEquityRatio

# Only input True or False

def Make_Graphs(Stock):
    
    inputreceiver = Stock
    getFreeCashFlow(inputreceiver)
    getDebtEquityRatio(inputreceiver)

