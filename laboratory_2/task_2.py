#Продолжение финансового планирования

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
months = 10
money_capital = 0

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for i in range(1, months+1):
    different = spend - salary
    money_capital += abs(different)
    spend += spend * increase


print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital, 2))
