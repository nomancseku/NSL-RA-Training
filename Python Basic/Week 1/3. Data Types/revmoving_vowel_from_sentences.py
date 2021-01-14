vowels = 'aeiou'
sentence = 'I am awesome!'
filtered_letters = []

for letter in sentence:
    if letter not in vowels:
        filtered_letters.append(letter)

print(''.join(filtered_letters))
print(filtered_letters)

#using list comprehension
vowels = 'aeiou'
sentence = 'I am awesome'
filtered_sentence = ''.join([letter for letter in sentence if letter not in vowels])
print(filtered_sentence)
