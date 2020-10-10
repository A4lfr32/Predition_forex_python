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

# mt5.WaitForTerminal()

#%%
mt5.initialize()
print(mt5.terminal_info())
print(mt5.version())

Num_velas=1000
# Copying data to pandas data frame
stockdata = pd.DataFrame()
rates = mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_M1, 0, Num_velas)
# Deinitializing MT5 connection
mt5.shutdown()
# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(rates)
# convert time in seconds into the datetime format
rates_frame.index=pd.to_datetime(rates_frame['time'], unit='s')
rates_frame.asfreq(freq='T')

rates_frame.columns=['time', 'Open', 'High', 'Low', 'Close', 'tick_volume', 'spread','real_volume']
mpf.plot(rates_frame,type='candle')

#%%

# AR example
# from statsmodels.tsa.ar_model import AR #op1
from statsmodels.tsa.ar_model import AutoReg
from random import random
import matplotlib.pyplot as plt
# contrived dataset
# fit model
# model = AR(rates_frame.Close) #op1
rates_frame.index=pd.date_range(as2[0], periods=len(as2),freq='D')
model = AutoReg(rates_frame.Close,lags=400,seasonal=True).fit()
# model_fit = model.fit(maxlag=400)#op1
# make prediction
# yhat = model.predict('23:55:00','23:59:00')
yhat = model.predict(len(rates_frame.Close)-10, len(rates_frame.Close)+500)

plt.plot(rates_frame.Close)
plt.plot(yhat)
# plt.show()


# %%

# %%
