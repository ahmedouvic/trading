
from django.shortcuts import render

from etc.trading_scripts.back_test import get_weights, symbols


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
    print(weight_dict)
    print _weights, symbols
    return render(request, 'weights.html', context)