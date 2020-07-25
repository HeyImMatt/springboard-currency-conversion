from forex_python.converter import CurrencyRates, CurrencyCodes

cr = CurrencyRates()
cc = CurrencyCodes()

def validate_code(code):
    '''Handles 3-letter currency code validaton'''
    name = cc.get_currency_name(code)
    
    if name == None:
        return False

    return True

def get_rate(from_code, to_code, amount):
    '''Handles the rate conversion to 2 decimals and gets currency symbol.'''
    try: 
        rate = "{:.2f}".format(cr.convert(from_code, to_code, amount))
        symbol = cc.get_symbol(to_code)
        return f'{symbol}{rate}'
    except:
        return False