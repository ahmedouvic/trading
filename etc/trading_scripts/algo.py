# -*- coding: utf-8 -*-

import scipy.optimize

import numpy as np
import scipy
from numpy import dot, cov
from zipline.api import (add_history,
                         history,
                         order_target_percent,
                         record)

from zipline import TradingAlgorithm


###########################################################

def compute_var(W, C):
    return dot(dot(W, C), W)


def initialize(context):

    context.stocks = ['VNQ', 'XLE', 'VTI','VEA', 'VWO', 'VIG', 'SCHP', 'MUB', 'LQD', 'EMB']

    context.leverage = 2
    add_history(950, '1d', 'price')

    context.x0 = 1.0*np.ones(len(context.stocks))/len(context.stocks)
    #context.i = 0
    context.day_count = -1


def handle_data(context, data):
    context.day_count += 1
    if context.day_count < 100:
        return

    prices = history(950, '1d', 'price').dropna()

    security_index = 0;
    daily_returns = np.zeros((len(context.stocks), 950))
    for security in context.stocks:
        if data.has_key(security):
            for day in range(0, 99):
                day_of = prices[security][day]
                day_before = prices[security][day - 1]
                daily_returns[security_index][day] = (day_of - day_before) / day_before
            security_index = security_index + 1
    covars = cov(daily_returns)

    covars = covars * 250

###########################################################
    returns = prices.pct_change().dropna()

    bnds = ((0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1))
    cons = ({'type': 'eq', 'fun': lambda x:  np.sum(x)-1.0})

    res = scipy.optimize.minimize(compute_var,
                                  context.x0,
                                  cov(daily_returns)*255,
                                  method='SLSQP',
                                  constraints=cons,
                                  bounds=bnds)

    allocation = res.x
    allocation[allocation < 0] = 0  # jamais de vente, que des achats
    denom = np.sum(allocation)
    if denom != 0:
        allocation = allocation/denom

    context.x0 = allocation

    record(stocks=np.sum(allocation[0:-1]))
    record(bonds=allocation[-1])

    for i, stock in enumerate(context.stocks):
        order_target_percent(stock, allocation[i])


###########################################################


def start_algo3(data):

    algo = TradingAlgorithm(initialize=initialize,
                            handle_data=handle_data)
    results = algo.run(data)
    return results, algo.perf_tracker.cumulative_risk_metrics



