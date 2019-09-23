# This simple project creates a phrased based on user's input

words = [' cat', ' balcony', ' ran.']
sentence = ['The', ' jumped of the', ' and it']
phrase = ''

for i in range(len(sentence)):
    phrase += sentence[i] + words[i]

print(phrase)
