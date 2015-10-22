# -*- coding: utf-8 -*-

#EXEMPLE BASIQUE

###########################################################

import time
import datetime
from pytz import timezone
import pytz
import numpy as np
import pandas as pd
from zipline.utils.factory import load_bars_from_yahoo
from pandas import tseries

from algo import start_algo3

start_time = time.time()

###########################################################
def assets_meanvar1(names, prices):

    Price = np.mean(prices)
    weights = np.ones(len(names)) / len(names)

    for i in range(len(names)):
        weights[i] = i*Price/1000

    return weights, Price
###########################################################

end = datetime.datetime(2015, 10, 20, tzinfo=pytz.utc)
end64 = np.datetime64(end)

start = datetime.datetime(2014, 10, 20, tzinfo=pytz.utc)
start64 = np.datetime64(start)
symbols = ['VNQ', 'XLE', 'VTI', 'VEA', 'VWO', 'VIG', 'SCHP', 'MUB', 'LQD', 'EMB']
df = load_bars_from_yahoo(stocks=symbols, start=start64, end=end64)

prices_list = {'VNQ': df.VNQ['close'], 'XLE': df.XLE['close'], 'VTI': df.VTI['close'], 'VEA': df.VEA['close'],
               'VWO': df.VWO['close'], 'VIG': df.VIG['close'], 'SCHP': df.SCHP['close'], 'MUB': df.MUB['close'],
               'LQD': df.LQD['close'], 'EMB': df.EMB['close']}


prices = []
for s in symbols:
    prices_out = prices_list[s]
    prices.append(prices_out)

def get_weights():
    weights, price = assets_meanvar1(symbols, prices)
    return weights

# Back Test

# resultat, Portfolio_risk_metrics = start_algo3(df)    # 'resultat' est le portefeuille
# # On veut afficher la courbe 'resultat.portfolio_value' qui sont les valeurs numériques du portefeuille
# print(resultat.portfolio_value.plot())
# show()
# #On veut afficher les valeurs numériques "Portfolio_risk_metrics"
# print(Portfolio_risk_metrics)


