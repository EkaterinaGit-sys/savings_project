'''Задание 1. Программа считает, сколько денег было накоплено за неделю'''

#Функция считает сумму всех чисел из списка
def summa(num):
    total = 0
    for n in num:
        total+=n
    return total

#Ввод данных
name = input("Введите имя: ")
goal = float(input("Сколько хотите накопить? " ))

money =[] #пустой список, заполняется в цикле
for day in range(1,8):
    amount = float(input("Сколько отложили в день " + str(day) + "? "))
    money.append(amount)

#Вызов функции
saved = summa(money)
left = goal - saved #Считает сколько осталось до цели

#Вывод данных
print()
print("Здравствуйте, " + name + "!")
print("Вы откладывали по дням: ", money)
print("Всего накоплено: ", saved, "руб.")
print("Осталось накопить: ", left, "руб.")

if left <= 0:
    print("Цель достигнута!")
else:
    print("Цель не достигнута")