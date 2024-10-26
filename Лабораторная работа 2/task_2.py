salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0  # финансовая подушка б

for i in range(1, months+1):
    money_capital += spend
    money_capital -= salary
    spend = spend + spend * increase

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
