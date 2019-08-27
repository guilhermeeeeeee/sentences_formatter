def get_string_number() :
    return {
            1: ['um', 'dez', 'cento', 'mil', 'milhao'],
            2: ['dois', 'vinte', 'dozentos'],
            3: ['tres', 'trinta', 'trezentos'],
            4: ['quatro', 'quarenta' , 'quatrocentos'],
            5: ['cinco', 'cinquenta', 'quinhentos'],
            6: ['seis', 'sessenta', 'seiscentos'],
            7: ['sete', 'setenta', 'setecentos'],
            8: ['oito', 'oitenta', 'oitocentos'],
            9: ['nove', 'noventa', 'novecentos'],
            11: 'onze',
            12: 'doze',
            13: 'treze',
            14: 'quatorze',
            15: 'quinze',
            16: 'dezeseis',
            17: 'dezesete',
            18: 'dezoito',
            19: 'dezenove'
        }

def separate_decimals(number):
    decimals = []
    divisor = 1
    while True :
        last_number = int((number / divisor) % 10)
        if last_number <= 0 :
            break
        divisor = divisor * 10
        decimals.append(last_number)
    return decimals


def written_number(number):
    number_translate = get_string_number()
    if not number:
        return 'zero'
    if number > 0 and number < 10:
        return number_translate.get(number)[0]
    if number == 100 :
        return 'cem'
    if number > 10 and number < 20  :
        return number_translate.get(number)
    decimals = separate_decimals(number)
    numbers = []
    for index, number in enumerate(decimals):
        decimal_translate = number_translate.get(number)[index]
        numbers.append(decimal_translate)
    return ' e '.join(reversed(numbers))
