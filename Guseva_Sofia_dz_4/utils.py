import requests


def currency_rates(code: str):
    """возвращает курс валюты `code` по отношению к рублю"""
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    text_url = response.text
    valute_search = text_url.find(code)  #Можно добавить .upper для переведения code в верхний регистр
    if valute_search != -1:
        valute_info = text_url[valute_search:text_url.find('</Value>', valute_search)]
        nominal = float(valute_info[valute_info.find('<Nominal>') + 9:valute_info.find('</Nominal>')])
        valute = float(valute_info[valute_info.find('<Value>') + 7:].replace(',', '.'))
        response.close()
        result_value = round(valute / nominal, 2)
        print(result_value)
    else:
        response.close()
        print("None")


if __name__ == '__main__':
    currency_rates(__name__)

# "PS
#C:\Users\User\PycharmProjects\New_basic_of_python\Guseva_Sofia_dz_4 > python
#utils.py
#None"

