a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
def division(a,b):
  if b == 0:
    return('делить на ноль нельзя!')
  else:
    c = a/b
    return(c)
print('Результат деления {0} на {1}: {2}'.format(a,b,division(a,b)))