salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
current_diff = 0
money_capital = 0
current_spend = spend

for i in range(months):
    current_diff = current_spend - salary
    money_capital += current_diff
    current_spend *= 1 + increase
    print(current_spend)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital, 2))
