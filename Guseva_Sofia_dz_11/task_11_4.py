"""Задание 4
Начать работу над проектом Склад оргтехники.

Создать класс, описывающий склад. А также класс Оргтехника, который будет базовым для классов-наследников.
 Эти классы — конкретные типы оргтехники (Принтер, Сканер, Ксерокс).
В базовом классе определить параметры, общие для приведённых типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Задание 5
Продолжить работу над заданием 4.
Разработать методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение
 компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
 можно использовать любую подходящую структуру (например, словарь).

Задание 6
Продолжить работу над заданием 5.

Реализовать механизм валидации вводимых пользователем данных. Например, для указания количества принтеров,
 отправленных на склад, нельзя использовать строковый тип данных!
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,изученных на уроках по ООП."""

class Equipment:
    def __init__(self, name_equipment: str, model: str, price: float, sn: str):
        self.name_equipment = name_equipment
        self.model = model
        self.price = price
        self.sn = sn

    def __str__(self):
        return f"{self.name_equipment} {self.model}"


class Printer(Equipment):
    def __init__(self, model: str, price: float, sn: str):
        super().__init__(self.__class__.__name__, model, price, sn)


class Scanner(Equipment):
    def __init__(self, model: str, price: float, sn: str):
        super().__init__(self.__class__.__name__, model, price, sn)


class Xserox(Equipment):
    def __init__(self, model: str, price: float, sn: str):
        super().__init__(self.__class__.__name__, model, price, sn)


class Warehouse:
    list_equipment = []
    count_equipment = {}

    def download(self, equipment, count):
        """Положить на склад"""
        if not isinstance(equipment, Equipment):
            raise Exception('Я складирую только оборудование')
        self.list_equipment.append(equipment)
        print(f'Мы положили на склад {equipment}')
        if not isinstance(count, int):
            raise Exception('Для указания количества нужно использовать целое число')
        if self.count_equipment.get(equipment.name_equipment) is not None:
            self.count_equipment[equipment.name_equipment] += count
        else:
            self.count_equipment.setdefault(equipment.name_equipment, count)

    def check_kolva(self):
        """Узнать количество каждого типа оборудования"""
        for k, v in self.count_equipment.items():
            print(f'На складе есть оборудование {k} в количестве {v} шт')


if __name__ == '__main__':
    printer01 = Printer('Lexmark B2338dw', 10599.0,'36SC126')
    printer02 = Printer('Pantum P2200', 11899.25, 'DR2347845')
    scanner01 = Scanner('Espada E-IScan', 4499.0, '4389G893H')
    scanner02 = Scanner('Fujitsu ScanSnap S1100i', 14299.23, 'UY57389UR')
    xserox01 = Xserox('WorkCentre 3025BI', 24124.98, 'EOI3473289')


    warehouse = Warehouse()
    warehouse.download(printer01, 1)
    warehouse.download(printer02, 3)
    warehouse.download(scanner01, 5)
    warehouse.check_kolva()
    warehouse.download(scanner02, 1)
    warehouse.download(xserox01, 1)
    warehouse.check_kolva()
    warehouse.download(printer01, 3)
    warehouse.check_kolva()
    warehouse.download('test', 1)
