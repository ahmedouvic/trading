
from django.shortcuts import render

from etc.trading_scripts.back_test import get_results, get_weights, symbols
from django.views.decorators.cache import cache_page


def index(request):
    """
    Index page
    """
    context = {}
    return render(request, 'index.html', context)


def weights(request):
    """
    Return weights
    """
    context = {}
    _weights = get_weights()
    weight_dict = {}
    for i in range(len(symbols)):
        weight_dict.update({'%s' % symbols[i]: _weights[i]})
    context.update({'weights': weight_dict})
    # print(weight_dict)
    # print _weights, symbols
    return render(request, 'weights.html', context)


@cache_page(60 * 60 * 2)
def metrics(request):
    """
    Return metrics
    """
    context = {}
    result, portfolio_risk_metrics = get_results()
    context.update({'risk_metrics': portfolio_risk_metrics.to_dict()})
    result.portfolio_value.plot()
    # print result.to_json()
    return render(request, 'metrics.html', context)