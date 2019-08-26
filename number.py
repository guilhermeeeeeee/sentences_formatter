def get_string_number() :
    return {
            1: ['um', 'dez', ['cem', 'cento'], 'mil', 'milhao'],
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
    divisor = 10
    while True :
        last_number = (number / divisor) % 10
        if last_number <= 0 :
            break
        divisor = divisor * 10
        decimals.append(last_number)
    return decimals

def generate_number_translate(number):
    if number[:1] == 0:
        return number.get(number)
    second_number = number[:1]


def translate_number(number):
    number_translate = get_string_number()
    if number > 10 and number < 20  :
        return number_translate.get(number)
    if number == 100 :
        return 'cem'
    decimals = separate_decimals(number)
    numbers = []
    for index, number in enumerate(decimals):
        print(decimals)
        decimal_translate = number_translate.get(number)[index]
        numbers.append(decimal_translate)
    return ' e '.join(numbers)

print(translate_number(123))