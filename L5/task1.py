from collections import defaultdict

companies_results = defaultdict(int)

companies_list = []

companies_qty = int(input('Введите количество предприятий: '))

for i in range(companies_qty):
    companies_list.append(input('Введите наименование предприятия: '))

for q_profit in range(1, 5):
    for company in companies_list:
        companies_results[company] += int(input(f'Введите прибыль за квартал {q_profit} для компании {company}: '))

avg_profit_all = round(sum(companies_results.values()) / companies_qty, 2)

print(f'Средняя прибыль за год для всех предприятий составила: {avg_profit_all} ед.')

best_companies = []
worst_companies = []
for (company, profit) in companies_results.items():
    if profit < avg_profit_all:
        worst_companies.append(company)
    else:
        best_companies.append(company)

print(f'Предприятия, прибыль которых оказалась выше средней: {best_companies}')

print(f'Предприятия, прибыль которых оказалась ниже средней: {worst_companies}')

