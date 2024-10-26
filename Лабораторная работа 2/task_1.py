money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

count = 1  # количество месяцев без долгов начиная со 2, так как первый уже считаем
all_money = salary + money_capital - spend  # бюджет

while all_money != 0:
    spend = spend + spend * increase
    all_money += salary
    if all_money > spend:
        count += 1
        all_money -= spend
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", count)
