#Задание: Финансовая подушка безопасности: Планирование будущего

money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0

while money_capital > 0:
    different = salary - spend
    if abs(different) > money_capital:
        break
    money_capital += different
    spend += spend * increase
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)