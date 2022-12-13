import unittest
from hse_python.practice_9 import *


class SingleLineTasksTestCase(unittest.TestCase):
    def test_find_numbers_divided_on_17(self):
        self.assertEqual(find_numbers_divided_on_17([]), [])
        self.assertEqual(
            find_numbers_divided_on_17([1, 17, 0, 34, 35]),
            [17, 34]
        )

    def test_find_numbers_contained_2(self):
        self.assertEqual(find_numbers_contained_2([]), [])
        self.assertEqual(
            find_numbers_contained_2([12, 17, 0, 234, 35, -2]),
            [12, 234]
        )

    def test_find_palindromic_numbers(self):
        self.assertEqual(find_palindromic_numbers([]), [])
        self.assertEqual(
            find_palindromic_numbers([1, 17, 0, 34, 22, 171, 1001, 35]),
            [1, 22, 171]
        )

    def test_count_spaces(self):
        self.assertEqual(count_spaces(''), 0)
        self.assertEqual(
            count_spaces('1  2d c '),
            4
        )

    def test_delete_vowels(self):
        self.assertEqual(delete_vowels(''), '')
        self.assertEqual(
            delete_vowels('qwertyuiopasdfghjklzxcvbnm'),
            'qwrtpsdfghjklzxcvbnm'
        )

    def test_find_short_words(self):
        self.assertEqual(find_short_words(''), [])
        self.assertEqual(
            find_short_words('privet menya zovut petya'),
            ['menya', 'zovut', 'petya']
        )

    def test_get_all_words_dictionary(self):
        self.assertEqual(get_all_words_dictionary(''), {})
        self.assertEqual(
            get_all_words_dictionary('1 2d c c'),
            {'1': 1, '2d': 2, 'c': 1}
        )

    def test_get_all_symbols_dictionary(self):
        self.assertEqual(get_all_symbols_dictionary(''), set())
        self.assertEqual(
            get_all_symbols_dictionary('1  2d c '),
            {'1', ' ', '2', 'd', 'c'}
        )

    def test_square_numbers(self):
        self.assertEqual(square_numbers([]), [])
        self.assertEqual(
            square_numbers([1, 2, 3]),
            [1, 4, 9]
        )

    def test_find_points_on_line(self):
        self.assertEqual(find_points_on_line([]), {})
        self.assertEqual(
            find_points_on_line([(1, 1), (2, 3), (5, 3), (1, 3)]),
            {(1, 3): math.sqrt(10)}
        )

    def test_square_special_numbers(self):
        self.assertEqual(square_special_numbers([]), [])
        self.assertEqual(
            square_special_numbers([0, 1, 2, 3, 4]),
            [0, 1, 4, 3, 16]
        )

    def test_find_the_farthest_point(self):
        self.assertEqual(find_the_farthest_point([]), 0)
        self.assertEqual(
            find_the_farthest_point([(0, 1), (1, 1), (1, 0), (-2, 0)]),
            math.sqrt(2)
        )

    def test_get_add_and_sub(self):
        self.assertEqual(get_add_and_sub([], []), [])
        self.assertEqual(
            get_add_and_sub([1, 2, 3, 4], [4, 3, 2, 1]),
            [(5, -3), (5, -1), (5, 1), (5, 3)]
        )

    def test_convert_csv_to_dict(self):
        self.assertEqual(convert_csv_to_dict(''), [])
        self.assertEqual(convert_csv_to_dict(
            "name,Petya,Vasya,Masha,Vova\n"
            "grade,5,5,8,3\n"
            "subject,math,language,physics,math\n"
            "year,1999,2000,1995,1998"
        ), [
            {
                'name': 'Petya',
                'grade': '5',
                'subject': 'math',
                'year': '1999'
            },
            {
                'name': 'Vasya',
                'grade': '5',
                'subject': 'language',
                'year': '2000'
            },
            {
                'name': 'Masha',
                'grade': '8',
                'subject': 'physics',
                'year': '1995'
            },
            {
                'name': 'Vova',
                'grade': '3',
                'subject': 'math',
                'year': '1998'
            },
        ])

    def test_get_column_sum(self):
        self.assertEqual(get_column_sum([]), [])
        self.assertEqual(
            get_column_sum([
                [11.9, 12.2, 12.9],
                [15.3, 15.1, 15.1],
                [16.3, 16.5, 16.5],
                [17.7, 17.5, 18.1]
            ]),
            [61.2, 61.3, 62.6]
        )


if __name__ == '__main__':
    unittest.main()
