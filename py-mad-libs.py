# This simple project creates a phrased based on user's input

words = ['cat', 'balcony']
sentence = ['The', 'jumped of the', '.']
phrase = ''

for i in range(len(sentence)):
    phrase += sentence[i]

print(phrase)
