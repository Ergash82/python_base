# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

totalExpenses = 12000
total_grant = 10000
month = 1
while month < 10:
    expenses += expenses * .03
    totalExpenses += expenses
    total_grant += educational_grant
    month += 1

expenses = (totalExpenses) - (total_grant)
print(total_grant)
print(totalExpenses)
print(f' Студенту надо попросить: {round(expenses,2)} руб')
