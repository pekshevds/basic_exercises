# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
counter = 0
for ch in word:
    counter += 1 if ch.lower() in 'аеёиоуэяю' else 0
print(counter)



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(' ')))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split(' '):
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split(' ')
counter = 0
for word in words:
    counter += len(word)
print(int(counter/len(words)))