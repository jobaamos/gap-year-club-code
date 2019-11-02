#python program that checks if a given word is palindrome or not
word = (input('enter a word'))
the_reverse = (word[::-1])
print('the reverse of', word,'is', the_reverse)
if (word==the_reverse):
    print('therefore', word, 'is a palindrome')
else:
    print('therefore', word, 'is not a palindrome')
