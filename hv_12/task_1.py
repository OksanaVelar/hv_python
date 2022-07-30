# Напишите программу, удаляющую из текста все слова, содержащие ""абв""
text = 'Предать забвению - значит полностью забыть, вычеркнуть из памяти что-либо, или кого либо. А делать что-то самозабвенно - значит глубоко увлечься тем, что ты делаешь, забыв о чем-либо другом'
print(f'Исходный текст:\n "{text}"')
print(' ')
words = text.split(' ')
# print(words)
fragment = 'абв'
cat_words = []
for word in words:
    if fragment not in word:
        cat_words.append(word)

cat_text = ' '.join(cat_words)
print(f'Усеченный текст:\n "{cat_text}"')

