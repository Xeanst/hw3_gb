def my_func(x,y):
  num = 1
  for i in range(y*(-1)):
    num *= x
  return(num)
x = float(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))
print(f'Число {x} в степени {y} равно {my_func(x,y)}')