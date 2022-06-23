amount_of_tickets = int(input('Введите количество билетов:\n'))

if 0 < amount_of_tickets:
    pass
else:
    print("Количество билетов введено некорректно")

list_of_tickets = [i for i in range(0, amount_of_tickets, 1)]

list_of_ages = [int(input('Введите возраст посетителя:\n')) for age in list_of_tickets]

list_of_prices = []

for age in list_of_ages:
    if 0 < age < 18:
        price_of_ticket = 0
        list_of_prices.append(price_of_ticket)
    elif 18 <= age <= 25:
        price_of_ticket = 990
        list_of_prices.append(price_of_ticket)
    elif 25 < age < 123:
        price_of_ticket = 1390
        list_of_prices.append(price_of_ticket)
    else:
        print("Возраст введен некорректно")

if len(list_of_tickets) > 3:
    print("Сумма к оплате: ", round(sum(list_of_prices) - 10/100 * sum(list_of_prices), 2))
else:
    print("Сумма к оплате: ", sum(list_of_prices))
