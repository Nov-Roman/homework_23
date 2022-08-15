from typing import Iterator, List, Iterable, Set, Union


def filter_(iterable: Iterator, string_to_search: str) -> Iterable:
    """Получить данные, которые содержат определенный текст"""
    if not isinstance(string_to_search, str):
        raise TypeError("Переданы неверные данные, разрешены только строки")
    return filter(lambda line: string_to_search in line, iterable)


def sort_(iterable: Iterator, order: str = 'asc') -> List:
    """Сортировка данных в порядке возрастания или убывания"""
    if order not in ('asc', 'desc'):
        raise ValueError('Неверный аргумент, разрешено использовать только по возрастанию или по убыванию.')
    if order == 'desc':
        return sorted(iterable, reverse=True)
    return sorted(iterable, reverse=False)


def map_(iterable: Iterator, column: Union[str, int]) -> Iterable:
    """Получить только указанный столбец"""
    if not str(column).isdigit():
        raise TypeError('Не число передается в качестве номера столбца')
    return map(lambda line: line.split(' ')[int(column)] + '\n', iterable)


def limit_(iterable: Iterator, number: Union[str, int]) -> List:
    """Предельные строки, возвращаемые переданным числом"""
    if not str(number).isdigit():
        raise TypeError('Разрешены только цифры')
    return list(iterable)[:int(number)]


def unique_(iterable: Iterator, *args) -> Set:
    """Возвращает только уникальные строки"""
    return set(iterable)
