#3.12 Вводим с клаиватуры строку. Необходимо вывести строку, 
#где развернём подстроку между первой и последней буквой "о" из исходной строки. 
#Если она только одна или её нет - то сообщить, что буква "о" - одна или не встречается.

text = input('Введите текст: ')

min_o = 0
max_o = 0

for i in range(len(text)):
    if text[i] == 'o':
        min_o == i
        break
for j in range(len(text)-1, -1, -1):
    if text[j] == 'o':
        max_o == j
        break
if min_o > 0 or max_o > 0:
    text_o = (text[:min_o] + text[max_o:min_o:-1] + text[max_o:])
    print(f'{text_o}')
else:
    print('Буквы о - отсутствуют')
