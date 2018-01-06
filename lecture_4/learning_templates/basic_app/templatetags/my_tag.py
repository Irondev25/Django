from django import template

register = template.Library()

def cut(value,arg):
    """This function removes arg from string"""
    return value.replace(arg,'')

register.filter('cut',cut)
