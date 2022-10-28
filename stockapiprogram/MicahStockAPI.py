import datetime
import urllib, json
import urllib.request
import dateutil.relativedelta
from operator import truediv
import mplcyberpunk
import matplotlib.pylab as plt
# DO NOT TOUCH API KEY
####################################
api_key = '6327aab714c9a2.75763093'#
####################################

DEBUG = True

def getFreeCashFlow(ticker):
    url1 = f'http://eodhistoricaldata.com/api/fundamentals/AAPL.US?api_token={api_key}&&filter=Financials::Cash_Flow::yearly::2021-09-30::filing_date'
    dataX = urllib.request.urlopen(url1).read()
    dataX = json.loads(dataX)
    dataX
    last_day_month = {
        '01':'31',
        '02':'28',
        '03':'31',
        '04':'30',
        '05':'31',
        '06':'30',
        '07':'31',
        '08':'31',
        '09':'30',
        '10':'31',
        '11':'30',
        '12':'31',
    }
    last_day_month_backwards = dict(reversed(list(last_day_month.items())))

    tickersymbol = ticker.upper()
    month_list = ['2021-12-31','2021-11-30','2021-10-31','2021-09-30','2021-08-31','2021-07-31','2021-06-30','2021-05-31','2021-04-30','2021-03-31','2021-02-28']
    cashflowlist = []
    cashflowdatelist = []
    for i in month_list:
        url1 = f'http://eodhistoricaldata.com/api/fundamentals/{tickersymbol}.US?api_token={api_key}&&filter=Financials::Cash_Flow::yearly::{i}::freeCashFlow,Financials::Cash_Flow::yearly::2020-09-30::freeCashFlow'
        dataX = urllib.request.urlopen(url1).read()
        dataX = json.loads(dataX)
        if dataX[f'Financials::Cash_Flow::yearly::{i}::freeCashFlow'] != 'NA':
            if DEBUG:
                print(f"Yes! Free Cash Flow Found for {i}!")
            url_date = datetime.datetime.strptime(i, "%Y-%m-%d").date()
            for k in last_day_month_backwards:
                if int(k) == url_date.month:
                    correct_day_month = url_date.replace(day=int(last_day_month[k]))
                    if DEBUG:
                        print(f'{k} is correct!')
                        print(correct_day_month)
                    for j in range (1,10):
                        d2 = correct_day_month - dateutil.relativedelta.relativedelta(year=correct_day_month.year-j)
                        url_cashflowjson = f'http://eodhistoricaldata.com/api/fundamentals/{tickersymbol}.US?api_token={api_key}&&filter=Financials::Cash_Flow::yearly::{d2}::freeCashFlow'
                        cashflowjson = urllib.request.urlopen(url_cashflowjson).read()
                        cashflowdic = json.loads(cashflowjson)
                        cashflowlist.append(cashflowdic)
                        cashflowdatelist.append(str(d2))
                        if DEBUG:
                            print(d2)
                            print(cashflowdic)
                            print(type(cashflowdic))
                            print(cashflowlist)
                            print(cashflowdatelist)
                    break
                if DEBUG:
                    print(f"{k} does not match {url_date.month}")
            break
        if DEBUG:
            print(f'No Free Cash Flow for {i}.')
    
    # 2 lists needed for graphing Free Cashflow graphs
    floatcashflowlist = [float(z) for z in cashflowlist]
    graphfreecashflowdatelist = [datetime.datetime.strptime(date,"%Y-%m-%d").date() for date in cashflowdatelist]

    # Plot the graph and save it as an image
    plt.style.use("cyberpunk")
    plt.plot(graphfreecashflowdatelist,floatcashflowlist, marker = 'o',label='Free Cash Flow')
    plt.title(f'10 Year Historic Free Cash Flow of {ticker.upper()}')
    plt.hlines(y=0, xmin = graphfreecashflowdatelist[0], xmax = graphfreecashflowdatelist[8],linewidth=2, color='r')
    plt.xlabel('Year')
    plt.ylabel('Cashflow (in tens of millions)')
    mplcyberpunk.add_underglow()
    plt.savefig("freecashflowgraph.jpg")
    return print('######## Free Cash Flow Graph Saved! ########')

def getDebtEquityRatio(ticker):
    last_day_month = {
        '01':'31',
        '02':'28',
        '03':'31',
        '04':'30',
        '05':'31',
        '06':'30',
        '07':'31',
        '08':'31',
        '09':'30',
        '10':'31',
        '11':'30',
        '12':'31',
    }
    last_day_month_backwards = dict(reversed(list(last_day_month.items())))

    tickersymbol = ticker.upper()
    month_list = ['2021-12-31','2021-11-30','2021-10-31','2021-09-30','2021-08-31','2021-07-31','2021-06-30','2021-05-31','2021-04-30','2021-03-31','2021-02-28']
    debtlist = []
    equitylist = []
    debtdatelist = []
    for i in month_list:
        url1 = f'http://eodhistoricaldata.com/api/fundamentals/{tickersymbol}.US?api_token={api_key}&&filter=Financials::Balance_Sheet::yearly::{i}::shortLongTermDebtTotal'
        dataX = urllib.request.urlopen(url1).read()
        dataX = json.loads(dataX)
        if dataX != 'NA':
            if DEBUG:
                print(f"Yes! Debt Found for {i}!")
            url_date = datetime.datetime.strptime(i, "%Y-%m-%d").date()
            for k in last_day_month_backwards:
                if int(k) == url_date.month:
                    correct_day_month = url_date.replace(day=int(last_day_month[k]))
                    if DEBUG:
                        print(f'{k} is correct!')
                        print(correct_day_month)
                    for j in range (1,10):
                        # Logic for the Year Date
                        d2 = correct_day_month - dateutil.relativedelta.relativedelta(year=correct_day_month.year-j)
                        # Retrieve Debt value from API
                        url_debtjson = f'http://eodhistoricaldata.com/api/fundamentals/{tickersymbol}.US?api_token={api_key}&&filter=Financials::Balance_Sheet::yearly::{d2}::shortLongTermDebtTotal'
                        debtjson = urllib.request.urlopen(url_debtjson).read()
                        debtdic = json.loads(debtjson)
                        # Retrieve Equity Value from API
                        url_equityjson = f'http://eodhistoricaldata.com/api/fundamentals/{tickersymbol}.US?api_token={api_key}&&filter=Financials::Balance_Sheet::yearly::{d2}::totalStockholderEquity'
                        equityjson = urllib.request.urlopen(url_equityjson).read()
                        equitydic = json.loads(equityjson)
                        if debtdic == 'NA':
                            debtlist.append('0')
                        else:
                            debtlist.append(debtdic)
                        equitylist.append(equitydic)
                        debtdatelist.append(str(d2))
                        if DEBUG:
                            print(d2)
                            print(debtdic)
                            print(type(debtdic))
                            print(debtlist)
                            print(equitylist)
                            print(debtdatelist)
                    break
                if DEBUG:
                    print(f"{k} does not match {url_date.month}")
            break
        if DEBUG:
            print(f'No Debt for {i}.')
    
    if DEBUG:
        print(f'equitylist : {len(equitylist)}')
        print(f'debtlist : {len(debtlist)}')
        print(f'datelist : {len(debtdatelist)}')

    floatdebtlist = [float(k) for k in debtlist]
    floatequitylist = [float(l) for l in equitylist]
    ratiorangelist = [int(n) for n in floatdebtlist]
    debtequityratio = list(map(truediv, floatdebtlist, floatequitylist))
    
    if DEBUG:
        print(f'floatdebtlist : {len(floatdebtlist)}')
        print(f'floatequitylist : {len(floatequitylist)}')
        print(f'ratiorangelist : {len(ratiorangelist)}')
        print(f'debequityratio : {len(debtequityratio)}')
    
    # Turns the debt date list into date objects
    graphdebtdatelist = [datetime.datetime.strptime(date,"%Y-%m-%d").date() for date in debtdatelist]
    # Turns the debt date list into date objects
    
    # Graphing the Debt/Equity Ratio Graph 
    plt.style.use("cyberpunk")
    plt.plot(graphdebtdatelist,debtequityratio, marker = 'o',label='Debt/Equity Ratio')
    plt.title(f'10 Year Historic Debt/Equity Ratio of {ticker.upper()}')
    plt.hlines(y=0, xmin = graphdebtdatelist[0], xmax = graphdebtdatelist[8],linewidth=2, color='r')
    plt.xlabel('Year')
    plt.ylabel('Debt/Equity Ratio')
    mplcyberpunk.add_underglow()
    plt.savefig("debtequityratiograph.jpg")

    return print('######## Debt Equity Ratio Graph Saved! ########')
