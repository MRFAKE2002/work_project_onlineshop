from django import template

register = template.Library()

@register.filter
def persian_numbers(number):
    
    english_numbers = "0123456789"
    
    persian_numbers = "۰۱۲۳۴۵۶۷۸۹"
    
    number = str(number)
    
    convert_e_to_p_numbers = number.maketrans(english_numbers, persian_numbers)
    
    return number.translate(convert_e_to_p_numbers)
