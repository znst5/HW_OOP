# Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков и возвращает их
# плоское представление, т. е. последовательность, состоящую из вложенных элементов. Функция test в коде ниже также должна
# отработать без ошибок.

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.outer_idx = 0
        self.inner_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.outer_idx < len(self.list_of_list):
            current_list = self.list_of_list[self.outer_idx]

            if self.inner_idx < len(current_list):
                item = current_list[self.inner_idx]
                self.inner_idx += 1
                return item

            else:
                self.outer_idx += 1
                self.inner_idx = 0

        raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

# Доработать функцию flat_generator. Должен получиться генератор, который принимает список списков и возвращает их плоское
# представление. Функция test в коде ниже также должна отработать без ошибок.

import types


def flat_generator(list_of_lists):
    current_list = []
    for i in list_of_lists:
        for j in i:
            yield j
            current_list.append(j)
    return current_list


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()