text=input('Enter some text please\n').lower()
word=input('Enter one more word please\n').lower()
n=text.count(word)
final_text=f"Слово {word} встречается в тексте {n} раз"
print(final_text)
