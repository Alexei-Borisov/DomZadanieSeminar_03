#3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом

text = input('Введите строку: ')

a = 0
for i in text:
    if not i.isdigit() and i == '.' or i == ',':
        a += 1
if a != 1:
    print('Строка не является дробным число')
else:
    print('Строка является дробным числом')

    