import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime
from datetime import date, timedelta
from tweets.aapl import sentiment_aapl
from tweets.jpm import sentiment_jpm
from tweets.nflx import sentiment_nflx

aapl = sentiment_aapl.final
jpm = sentiment_jpm.final
nflx = sentiment_nflx.final

def get_stock_data(ticker, sentiment):
	end_date = datetime.datetime(2017,5,3) #change this
	start_date = end_date - timedelta(days=22) #change this
	print("START DATE", start_date)
	stock = web.DataReader(ticker,'yahoo', start_date, end_date)
	stock['Percent'] = (stock['Adj Close']-stock['Adj Close'].shift(1))/stock['Adj Close']*100
	pct_change = stock['Percent'].tolist()
	change_list=[]
	for i in pct_change[1:]:
		short = round(i, 3)
		change_list.append(short)
	name = [ticker]
	final_list = name+change_list
	dates = stock.index.values
	date_list = ['Date']
	for day in dates[1:]:
		correct = str(day)[:10]
		date_list.append(correct)
	stock_dict = {'stock': final_list, 'date_list': date_list, 'sentiment': sentiment}
	return stock_dict

aapl_info = get_stock_data('AAPL', aapl)
jpm_info = get_stock_data('JPM', jpm)
nflx_info = get_stock_data('NFLX', nflx)