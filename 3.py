def max_sum(a,b,c):
  nums = set([a, b, c])
  smallest = min(nums)
  nums.remove(smallest)
  return(sum(nums))
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
print(f'Сумма двух наибольших чисел равна {max_sum(a,b,c)}')