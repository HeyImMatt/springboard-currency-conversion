from forex_python.converter import CurrencyRates, CurrencyCodes

cr = CurrencyRates()
cc = CurrencyCodes()

def validate_codes(from_code, to_code):
    from_name = cc.get_currency_name(from_code)
    to_name = cc.get_currency_name(to_code)
    
    if from_name == None or to_name == None:
        return False

    return True

def get_rate(from_code, to_code, amount):
    try: 
        rate = "{:.2f}".format(cr.convert(from_code, to_code, amount))
        symbol = cc.get_symbol(to_code)
        return f'{symbol}{rate}'
    except:
        print('Cannot convert. Conversion service down')