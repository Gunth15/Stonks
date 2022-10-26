from MicahStockAPI import getFreeCashFlow
import datetime
import matplotlib.pylab as plt
import mplcyberpunk

inputreceiver = input("Type a Stock Ticker: ")
x, y = getFreeCashFlow(inputreceiver)

date_list = [datetime.datetime.strptime(date,"%Y-%m-%d").date() for date in x]
cashvalues = [float(k) for k in y]

plt.style.use("cyberpunk")
plt.plot(date_list,cashvalues, marker = 'o',label='Free Cash Flow')
plt.title(f'10 Year Historic Free Cash Flow of {inputreceiver.upper()}')
plt.hlines(y=0, xmin = date_list[0], xmax = date_list[8],linewidth=2, color='r')
plt.xlabel('Year')
plt.ylabel('Cashflow (in tens of millions)')
mplcyberpunk.add_underglow()
plt.show()


