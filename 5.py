def func():
  final_sum = 0
  go = True
  while go:
    l = input('Введите числа через пробел или $ для завершения программы: ').split()
    sum = 0
    for x in l:
      if x == '$':
        go = False
        break
      else:
        sum += int(x)
    final_sum += sum
    print(f'Текущая сумма равна {final_sum}')
  print(f'Финальная сумма равна {final_sum}')
func()