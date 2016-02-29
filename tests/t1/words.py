# Write a program to read in words from the keyboard one at a time until the word "quit" is typed.
# Store them in a list then print them alphabetically
history = []
i = 0
print('Give me some words to order, say quit to stop me')
while i < 10:
    word = input('Give me a word: ')
    if str.lower(word) == 'quit':
        print('I will stop then')
        i = 12374
    else:
        x = word
        history.append(x)
print (history)
#dont know how to place in alphabetic order
