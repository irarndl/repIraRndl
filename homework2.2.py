import string
import random
word=''.join(random.sample(string.ascii_letters,10))
word=word.lower()
print(word.count(word[0]))
print(word.count(word[1]))
print(word.count(word[2]))
print(word.count(word[3]))
print(word.count(word[4]))
print(word.count(word[5]))
print(word.count(word[6]))
print(word.count(word[7]))
print(word.count(word[8]))
print(word.count(word[9]))