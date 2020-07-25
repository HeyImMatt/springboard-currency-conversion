from forex import validate_code

def form_validate(from_code, to_code, amount):
    if validate_code(from_code) == False:
        return f'From code not valid: {from_code}'
    
    if validate_code(to_code) == False:
        return f'To code not valid: {to_code}'

    try:
        float(amount)
    except:
        return f'Amount needs to be a valid number: {amount}'

    return True