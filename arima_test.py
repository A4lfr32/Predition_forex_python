# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:24:57 2019

@author: Nielsen
"""

# -*- coding: utf-8 -*-
# %% 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

import mplfinance as mpf
# from matplotlib.dates import num2date
# Initializing MT5 connection 
import MetaTrader5 as mt5

#%%
mt5.initialize()
# mt5.WaitForTerminal()

print(mt5.terminal_info())
print(mt5.version())

Num_velas=1000
# Copying data to pandas data frame
stockdata = pd.DataFrame()
rates = mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_M1, 0, Num_velas)
# Deinitializing MT5 connection
mt5.shutdown
# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(rates)
# convert time in seconds into the datetime format
rates_frame.index=pd.to_datetime(rates_frame['time'], unit='s')

rates_frame.columns=['time', 'Open', 'High', 'Low', 'Close', 'tick_volume', 'spread','real_volume']
mpf.plot(rates_frame,type='candle')
#%%

# ARIMA example
from statsmodels.tsa.arima.model import ARIMA
# from random import random
# contrived dataset
data = rates_frame.Close
# fit model
model = ARIMA(data, order=(40, 1, 10))
model_fit = model.fit()
# make prediction
yhat = model_fit.predict(len(data), len(data)+100, typ='levels')

plt.plot(rates_frame[-500:].Close)
plt.plot(yhat)
# plt.show()
# %%

# %%
