# title Сборник задач, выполняемых в одну строку, используя acomprehesion, filter, map
# description
# 1. Найти все числа от 1 до 1000, которые делятся на 17
# 2. Найти все числа от 1 до 1000, которые содержат в себе цифру 2
# 3. Найти все числа от 1 до 10000, которые являются палиндромом
# 4. Посчитать количество пробелов в строке
# 5. Есть любая последовательность непробельных символов латинского алфавита, удалить все гласные из этого слова
# 6. На входе строка со словами, разделенными через 1 пробел. Найти все слова, длина которых не больше 5
# 7. На входе строка со словами, разделенными через 1 пробел. Получить словарь, где в качестве ключа используется само слово, а в значении длина этого слова.
# 8. На входе предложение со всеми пробельными и непробельными символами латинского алфавита. Получить словарь используемых букв в строке, то есть на выходе список уникальных букв.
# 9. На входе список чисел, получить список квадратов этих чисел / use map
# 10. На входе список координат, например, [(1, 1), (2, 3), (5, 3)]. Найти все точки, которые принадлежат прямой y = 5 * x - 2. На выходе получить словарь из самой точки и расстоянии до этой точки из начала координат (0, 0)
# 11. Возвести в квадрат все четные числа от 2 до 27. На выходе список.
# 12. На входе список из координат точек на плоскости. Найти расстояние до самой удаленной точку от начала координат (0, 0) в первой четверти
# 13. На входе два списка чисел nums_first = [1, 2, 3, 5, 8] и nums_second = [2, 4, 8, 16, 32]. Получить пары сумм и разниц, [(3, -1), (6, -2), (11, -5), ...]
# 14. На входе список строк из чисел, например, ['43141', '32441', '431', '4154', '43121']. Найти четные квадраты этих чисел. Ответ записать снова в список из строк, то есть сформировать обратно список строк, но уже отфильтровать все четные квадраты.
# 15. Менеджер как обычно придумал свое представление данных, а нам оно не подходит
# 16. Получить сумму по столбцам у двумерного списка
# end
import math
from typing import List, Dict, Set, Tuple


def find_numbers_divided_on_17(numbers: List[int]) -> List[int]:
    return list(filter(lambda x: 1 <= x <= 1000 and x % 17 == 0, numbers))


def find_numbers_contained_2(numbers: List[int]) -> List[int]:
    return list(filter(lambda x: 1 <= x <= 1000 and '2' in str(x), numbers))


def find_palindromic_numbers(numbers: List[int]) -> List[int]:
    return list(filter(lambda x: 1 <= x <= 1000 and "".join(reversed(str(x))) == str(x), numbers))


def count_spaces(s: str) -> int:
    return sum(map(lambda x: 1 if x == ' ' else 0, s))


def delete_vowels(s: str) -> str:
    return "".join(filter(lambda x: x not in ['a', 'o', 'e', 'i', 'y', 'u'], s))


def find_short_words(s: str) -> List[str]:
    return list(filter(lambda x: 1 <= len(x) <= 5, s.split(' ')))


def get_all_words_dictionary(s: str) -> Dict[str, int]:
    return {word: len(word) for word in filter(lambda x: len(x) >= 1, s.split(' '))}


def get_all_symbols_dictionary(s: str) -> Set[str]:
    return {symb for symb in s}


def square_numbers(numbers: List[int]) -> List[int]:
    return list(map(lambda x: x * x, numbers))


Point = Tuple[int, int]


def find_points_on_line(points: List[Point]) -> Dict[Point, float]:
    return dict(
        map(
            lambda p: (p, math.sqrt(p[0] ** 2 + p[1] ** 2)),
            filter(lambda p: 5 * p[0] - 2 == p[1], points)
        )
    )


def square_special_numbers(numbers: List[int]) -> List[int]:
    return list(map(lambda x: x * x if x % 2 == 0 and 2 <= x <= 27 else x, numbers))


def find_the_farthest_point(points: List[Point]) -> float:
    return max(
        map(
            lambda p: math.sqrt(p[0] ** 2 + p[1] ** 2),
            filter(lambda p: p[0] >= 0 and p[1] >= 0, points)
        ),
        default=0.0
    )


def filter_even_squares(numbers: List[str]) -> List[str]:
    return list(map(
        str,
        map(
            lambda x: x * x,
            filter(lambda x: x % 2 == 0, map(int, numbers))
        )
    ))


def get_add_and_sub(nums_first: List[int], nums_second: List[int]) -> List[Tuple[int, int]]:
    return list(map(lambda x: (x[0] + x[1], x[0] - x[1]), zip(nums_first, nums_second)))


def convert_csv_to_dict(s: str) -> List[Dict[str, str]]:
    return list(map(
        dict, (
            zip(*map(
                lambda key_values: map(
                    lambda value: (key_values[0], value),
                    key_values[1].split(',')
                ),
                map(
                    lambda key_values_raw: key_values_raw.split(',', 1),
                    s.splitlines()
                )
            ))
        )
    ))


def get_column_sum(numbers: List[List[float]]) -> List[float]:
    return list(map(sum, zip(*numbers)))
