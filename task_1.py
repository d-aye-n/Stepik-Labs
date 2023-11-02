money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

current_money = money_capital
month_num = 0
current_spend = spend
current_diff = spend - salary

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while current_money >= current_spend - salary:
    month_num += 1
    current_money -= current_spend - salary
    current_spend *= 1 + increase
print("Количество месяцев, которое можно протянуть без долгов:", month_num)
