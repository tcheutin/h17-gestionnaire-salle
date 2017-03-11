from django import template
import locale
locale.setlocale(locale.LC_ALL, '')

register = template.Library()

@register.filter(name='currency')
def formatCurrency(value):
    return locale.currency(value, grouping=True)

@register.filter(name='bigint')
def formatInteger(value):
    return locale.format('%d', value, grouping=True)
