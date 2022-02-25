"""Написать тело функцию email_parse(email: str), которая при помощи регулярного выражения извлекает имя пользователя
и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.

Пример:
$ email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
$ email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru"""


import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'^[a-z0-9]+@\w+[.]\w+$')
    if not RE_MAIL.findall(email):
        raise ValueError(f'Wrong email: {email}')
    else:
        new_re_mail = re.compile(r'[@]')
        value = new_re_mail.split(email)
    key = ['username', 'domain']
    dict_out = {k:v for k,v in zip(key, value)}
    print(dict_out)


if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrainsru')
