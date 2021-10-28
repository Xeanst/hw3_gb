def my_func(x,y):
  return(x**y)
x = float(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))
print(f'Число {x} в степени {y} равно {my_func(x,y)}')