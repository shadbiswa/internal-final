def item():
    while true:
    try:
        number_of_words = int(input('Enter the number of words: '))
        return number_of_words
    except error:
        print('You must enter a number')

words = []
for word in range(number_of_words):
    words.append(input(f'Enter word {word + 1}: '))
print(words)
