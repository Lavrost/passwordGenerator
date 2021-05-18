import random


def password_generation(number: int, symbols_type: str):
    """Эта функция создает пароль из символов a-z A-Z !"#$%&'()*+,-.\/:;<=>?@[]^_`{|}~"""
    all_symbols = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-.\/:;<=>?@[]^_`{|}~'''
    symbols_standard = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    q = symbols_type
    if q == '+':
        symbols = all_symbols
    else:
        symbols = symbols_standard
    i = 0
    password = ''
    while i < number:
        password += random.choice(symbols)
        i += 1
    return password


print('Введите длину пароля')
pass_len = int(input())
while pass_len < 3:
    print('Введите число > 2')
    pass_len = int(input())

print('Поставьте +, если хотите использовать НЕ только бувкоциферные символы')
type_symbols = str(input())


my_pass = password_generation(pass_len, type_symbols)  # my_pass - ваш новый пароль
print(my_pass)
