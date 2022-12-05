# Вывести последнюю букву в слове
word = 'Архангельск'
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.find('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
glas = set('аиеёоуыэюя')
word_set = set(word.lower())
print(f'{len(word_set.intersection(glas))} гласных слове')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
sentence = sentence.split(' ')
print(len(sentence))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split(' ')
for word in words:
    print(word[0])



# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split(' ')
avrg = sum(len(word) for word in words)/(len(words))
print(avrg)