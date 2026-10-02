'''Задание 1. Программа считает, сколько денег было накоплено за неделю'''

print("Изменения для клона")

from typing import List

def summa(numbers: List[float]) -> float:
    total = 0.0
    for n in numbers:
        total += n
    return total

def input_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число.")

def save_history(entries: List[str], filename: str = "history.txt") -> None:
    with open(filename, "a", encoding="utf-8") as f:
        for line in entries:
            f.write(line + "\n")

def main() -> None:
    name = input("Введите имя: ")
    goal = input_float("Сколько хотите накопить? ")

    money = []
    for day in range(1, 8):
        amount = input_float(f"Сколько отложили в день {day}? ")
        money.append(amount)

    saved = summa(money)
    left = goal - saved

    print()
    print(f"Здравствуйте, {name}!")
    print("Вы откладывали по дням: ", money)
    print(f"Всего накоплено: {saved} руб.")
    print(f"Осталось накопить: {left} руб.")
    print("Цель достигнута!" if left <= 0 else "Цель не достигнута")

    save_history([f"{name}: накоплено {saved}, осталось {left}"])

if __name__ == "__main__":
    main()