# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым
# результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы
# в расчете на одного сотрудника.
earnings = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издержек: "))
if earnings > costs:
    print("У нас прибыль, босс!")
    income = earnings - costs
    profit_margin = (income / earnings) * 100
    print("{0:.2f}".format(profit_margin) +"%" +" годовых")
    employees = int(input("Введите количество сотрудиков: "))
    income_per_employee = income/employees
    print(f"Прибыль на одного сотрудика : {income_per_employee}")
elif costs > earnings:
    print("У нас убыток, босс, давайте кого-нибудь уволим за это!")
else:
    print("У нас 0 проибыли, босс!")