"""Задание 3
Есть два списка:

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей','Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:

('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:

('Станислав', None)
Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких ситуациях генератор даст эффект."""


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Ростислав', 'Виктория']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    """генератор, возвращающий
    кортежи
    вида( < tutor >, < klass >)"""
    for name,klass in zip(tutors, klasses):
        yield name,klass


while len(tutors) > len(klasses):
    klasses.append('None')
generator = check_gen(tutors, klasses)
print(type(generator))
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration

# Предыдущее решение (не получилось реализовать None
#def check_gen(tutors: list, klasses: list):
#    for i in range(len(tutors)):
#        row = []
#        row.append(tutors[i])
#        row.append(klasses[i])
#        yield tuple(row)


#generator = check_gen(tutors, klasses)
#print(type(generator))
#for _ in range(len(tutors)):
#    print(next(generator))