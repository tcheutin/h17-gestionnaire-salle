from django import template
from datetime import date
import locale
locale.setlocale(locale.LC_ALL, '')

register = template.Library()

@register.filter(name='currency')
def formatCurrency(value):
    return locale.currency(value, grouping=True)

@register.filter(name='bigint')
def formatInteger(value):
    return locale.format('%d', value, grouping=True)
    
@register.filter(name='ratio')
def ratio(value, arg):
    return value / arg * 100
    
@register.filter(name='date')
def formatDate(value):
    return '{:%Y-%m-%d}'.format(value.date())