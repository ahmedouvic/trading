# -*- coding: utf-8 -*-
__author__ = 'ahmed'

from django import template
import logging
from django.core.urlresolvers import reverse, NoReverseMatch


register = template.Library()

# initiate logger
logging.getLogger(__name__)


@register.filter()
def match_url(request_path, url_name):
    """
    """
    try:
        path = reverse(url_name)
        if path == request_path:
            return True
        return False
    except NoReverseMatch:
        return False
