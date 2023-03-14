import datetime as d
from matplotlib import pyplot as pt
from matplotlib import style
from pandas_datareader import data as pdr
import requests
import yfinance as yfin
#getting the ticker symbol when user enters company name
def getTicker(company_name):
    yfinance = "https://query2.finance.yahoo.com/v1/finance/search"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    params = {"q": company_name, "quotes_count": 1, "country": "United States"}

    res = requests.get(url=yfinance, params=params, headers={'User-Agent': user_agent})
    data = res.json()

    company_code = data['quotes'][0]['symbol']
    return company_code
a=int(input("press 1 for single graph and press 2 for vs graph"))
#taking start time and endtime as input
sty=int(input("enter start year"))
stm=int(input("enter start month"))
std=int(input("enter start day"))
#ending year input
eny=int(input("enter end year"))
enm=int(input("enter ending month"))
enda=int(input("enter ending date"))
start=d.datetime(sty,stm,std)
end=d.datetime(eny,enm,enda)
if a==1:
#taking company input and retrieving ticker symbols
    comp1=input("enter company")
    c1=str(getTicker(comp1))
    yfin.pdr_override()
    cdata1=pdr.get_data_yahoo(c1,start,end)
    style.use('ggplot')
    cdata1['Close'].plot(figsize=(8,8))
    pt.title(comp1)
    pt.ylabel("Close Price")
    pt.show()
else:
     yfin.pdr_override()
     comp1=input("enter first company")
     c1=str(getTicker(comp1))
     comp2=input("enter second company")
     c2=str(getTicker(comp2))
     cdata1=pdr.get_data_yahoo(c1,start,end)
     cdata1['Close'].plot(figsize=(8,8))
     cdata2=pdr.get_data_yahoo(c2,start,end)
     cdata2['Close'].plot(figsize=(8,8))
     style.use('ggplot')
     pt.title(comp1+' vs '+comp2)
     pt.ylabel("Close Price")
     pt.legend([comp1,comp2],loc='lower right')
     pt.show()
     