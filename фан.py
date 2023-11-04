with open('яой.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line)
author = input('Введіть aвтора: ')
with open('яой.txt', 'a', encoding='utf-8') as file:
    file.write(author)
while True:
    answer = input('Дщдати ще одну цитату (так/ні): ')
    if answer == 'так':
        quote = input('Введіть цитату: ')
        author = input('Введіть автора: ')
        file = open('яой.txt', 'a', encoding='utf-8')
        file.write(quote +'\n' + author)
        file.close()
    else:
        break
with open('яой.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line)
