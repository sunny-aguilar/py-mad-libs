# This simple project creates a phrased based on user's input

words = ['black', 'cat', 'balcony']
sentence = ['The', ' jumped of the', '.']
phrase = ''

for i in range(len(sentence)):
    phrase += sentence[i] + words[i]

print(phrase)
