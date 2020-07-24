from forex_python.converter import CurrencyRates, CurrencyCodes

cr = CurrencyRates()
cc = CurrencyCodes()

def get_rate(from_code, to_code, amount):
    try: 
        rate = "{:.2f}".format(cr.convert(from_code, to_code, amount))
        symbol = cc.get_symbol(to_code)
        return f'{symbol}{rate}'
    except:
        print('Cannot convert. Conversion service down')