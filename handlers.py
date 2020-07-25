from forex import validate_code

def form_validate(from_code, to_code, amount):
    if validate_code(from_code) == False:
        return 'From code not valid'
    
    if validate_code(to_code) == False:
        return 'To code not valid'

    try:
        float(amount)
    except:
        return 'Amount needs to be a valid number'

    return True