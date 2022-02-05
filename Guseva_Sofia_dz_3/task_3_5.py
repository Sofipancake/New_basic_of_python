#Задание 5
#Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):

#nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
#adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
#adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

#Например:
#>>> get_jokes(2)
#["лес завтра зеленый", "город вчера веселый"]
#Документировать код функции.

#Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
#Сможете ли вы сделать аргументы именованными?
from random import choice, shuffle

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    list_out = []
    while len(list_out) < count:
        list_out.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    return list_out


print(get_jokes(2))    #['огонь вчера мягкий', 'лес вчера утопичный']
print(get_jokes(10))   #['город вчера зеленый', 'лес сегодня зеленый', 'лес позавчера веселый', 'дом вчера яркий', 'лес ночью мягкий', 'город ночью утопичный', 'город вчера веселый', 'город сегодня зеленый', 'огонь вчера яркий', 'автомобиль ночью веселый']


# Раскомментируйте для реализации подзаданий: документирование, флаг и именованные аргументы
def get_jokes_adv(count, flag='repeat') -> list:
    """Возвращает список шуток в количестве count, с регулированием повторяющихся элементов"""
    list_out = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if flag != 'repeat': # перемешивает карты для того чтобы была видимость выбора случайного элемента
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)

    for i in range(count):
        if len(nouns) and len(adverbs) and len(adjectives):
            if flag != 'repeat':
                list_out.append(f'{nouns.pop()} {adverbs.pop()} {adjectives.pop()}')
            else:
                list_out.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')

    return list_out


print(get_jokes_adv(2)) #['лес сегодня мягкий', 'город сегодня мягкий']
print(get_jokes_adv(2, flag='no_repeat')) #['автомобиль вчера веселый', 'лес ночью яркий']
print(get_jokes_adv(10)) #город позавчера веселый', 'автомобиль сегодня мягкий', 'автомобиль вчера утопичный', 'лес вчера веселый', 'автомобиль вчера зеленый', 'город завтра зеленый', 'дом позавчера мягкий', 'автомобиль сегодня яркий', 'автомобиль ночью утопичный']
print(get_jokes_adv(10, flag='no_repeat')) #['огонь завтра мягкий', 'дом вчера зеленый', 'автомобиль ночью утопичный', 'лес позавчера веселый', 'город сегодня яркий']
