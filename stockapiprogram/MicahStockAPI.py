import datetime
import urllib, json
import urllib.request
import dateutil.relativedelta
# DO NOT TOUCH API KEY
####################################
api_key = '6327aab714c9a2.75763093'#
####################################

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
            print(f"Yes! Free Cash Flow Found for {i}!")
            url_date = datetime.datetime.strptime(i, "%Y-%m-%d").date()
            for k in last_day_month_backwards:
                if int(k) == url_date.month:
                    correct_day_month = url_date.replace(day=int(last_day_month[k]))
                    print(f'{k} is correct!')
                    print(correct_day_month)
                    for j in range (1,10):
                        d2 = correct_day_month - dateutil.relativedelta.relativedelta(year=correct_day_month.year-j)
                        url_cashflowjson = f'http://eodhistoricaldata.com/api/fundamentals/{tickersymbol}.US?api_token={api_key}&&filter=Financials::Cash_Flow::yearly::{d2}::freeCashFlow'
                        cashflowjson = urllib.request.urlopen(url_cashflowjson).read()
                        cashflowdic = json.loads(cashflowjson)
                        cashflowlist.append(cashflowdic)
                        cashflowdatelist.append(str(d2))
                        print(d2)
                        print(cashflowdic)
                        print(type(cashflowdic))
                        print(cashflowlist)
                        print(cashflowdatelist)
                    break
                print(f"{k} does not match {url_date.month}")
            break
        print(f'No Free Cash Flow for {i}.')

    #freecashflow = {cashflowdatelist[l]: cashflowlist[l] for l in range(len(cashflowdatelist))}
    #print(freecashflow)
    return cashflowdatelist, cashflowlist