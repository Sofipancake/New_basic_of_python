#В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.

#Можно ли, используя только методы класса str, решить поставленную задачу?
#Функция должна возвращать результат числового типа, например float.

#Подумайте:
#есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
#Сильно ли усложняется код функции при этом?
#Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.

#Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
#В качестве примера выведите курсы доллара и евро.


import requests


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    text_url = response.text
    valute_search = text_url.find(code)  #Можно добавить .upper для переведения code в верхний регистр
    if valute_search != -1:
        valute_info = text_url[valute_search:text_url.find('</Value>', valute_search)]
        nominal = float(valute_info[valute_info.find('<Nominal>') + 9:valute_info.find('</Nominal>')])
        valute = float(valute_info[valute_info.find('<Value>') + 7:].replace(',', '.'))
        response.close()
    else:
        response.close()
        return

    print(f'Соотношение валют: {nominal} {code} = {valute:.2f} RUB')
    result_value = round(valute / nominal , 2)
    return result_value


print(currency_rates("USD"))
print(currency_rates("SEK"))
print(currency_rates("noname"))