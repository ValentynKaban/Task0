from random import randint

numbers = []
for i in range(30):
    numbers.append(randint(-100, 100))
maxnumber = max(numbers)
print(numbers)
print("Максимальне число =", maxnumber)
print("Порядковий номер максимального числа =", int(numbers.index(maxnumber))+1)
print("Пари від’ємних чисел, що стоять поруч:")
for i in range(29):
  if numbers[i] < 0 and numbers[i+1] < 0:
    print(numbers[i], numbers[i+1])
  



#Сформувати список з 30 випадкових цілих чисел від -100 до + 100.
#Знайти максимальний елемент списку і його порядковий номер.
#Вивести пари від’ємних чисел, що стоять поруч.
