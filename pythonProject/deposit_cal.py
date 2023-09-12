# ввод суммы вклада
money = int(input("Введите сумму депозита: \n"))
# создание словаря с наименованием банка и процентной ставкой
per_cent = {'DenizBank': 7.3, 'VakıfBank' : 7.9, 'ZiraatBank': 5.6, 'YapiKredi': 6.3}
# создание списка и расчет суммы накоплений за год по каждому банку
deposit = [money*per_cent ['DenizBank']/100,
                money*per_cent ['VakıfBank']/100,
                money*per_cent ['ZiraatBank']/100,
                money*per_cent ['YapiKredi']/100]
# вывод суммы накоплений за год по каждому банку
print(list(map(round, deposit)))
maximum = round(max(deposit))
# вывод максимальной суммы накоплений
print (f"Максимальная сумма, которую вы можете заработать - {maximum} лир")

