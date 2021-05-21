import requests
from bs4 import BeautifulSoup

res = requests.get('https://merolagani.com/StockQuote.aspx')  # getting response from the website
soup = BeautifulSoup(res.text, 'html.parser')  # changes the string from res.text to soup object using html parser
stock_table = soup.tbody  # getting the table containing stock details

# getting the contents from the table
company = stock_table.select('a')
ltp = stock_table.select('td:nth-child(3)')
change = stock_table.select('td:nth-child(4)')
highest = stock_table.select('td:nth-child(5)')
lowest = stock_table.select('td:nth-child(6)')
start = stock_table.select('td:nth-child(7)')


# creating a function that sorts the stocks according to their change
def sort_stocks_by_change(stock_list):
    return sorted(stock_list, key=lambda k: k['change'], reverse=True)


#  creating a function to append the stock details to a list
def create_custom_ml(company, ltp, change, highest, lowest, start):
    stocks = []
    for idx, item in enumerate(company):
        name = company[idx].getText()
        last_price = ltp[idx].getText()
        diff_price = float(change[idx].getText())
        high_price = highest[idx].getText()
        low_price = lowest[idx].getText()
        opening_price = start[idx].getText()
        stocks.append({'company': name, 'LTP': last_price, 'change': diff_price, 'high': high_price, 'low': low_price,
                       'open': opening_price})
    return sort_stocks_by_change(stocks)


create_custom_ml(company, ltp, change, highest, lowest, start)


