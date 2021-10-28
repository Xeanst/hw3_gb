def int_func(text):
  return(text.capitalize())
word = input('Введите слово: ')
print(int_func(word))
text = input('Введите слова через пробел: ').split()
print(*[int_func(x) for x in text])