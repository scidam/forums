import string

words = input('Enter a series of words separated by spaces: ')
 
print('The length of the input string is ',len(words))


current_word = ''
container = []
for j in words:
    word_beginning_flag = j in string.ascii_letters # you can define string.ascii_letters manually instead

    if word_beginning_flag:
        current_word += j

    if j not in string.ascii_letters:
        word_beginning_flag = False
        if current_word:
            container.append((current_word, len(current_word)))
            current_word = ''
else:
    if words[-1] in string.ascii_letters:
        container.append((current_word, len(current_word)))

print("Result is ready: ", container)
        
