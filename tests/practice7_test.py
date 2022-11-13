import asyncio
import json
import os
import unittest
from tempfile import TemporaryDirectory

from hse_python.practice_7 import *


class CsvToJsonConverterTestCase(unittest.TestCase):
    def test_file_converting_correctness(self):
        with TemporaryDirectory() as tmp_dir:
            csv_to_json_converter = AsyncCsvToJsonConverter(
                csv_delimiter=",",
                ignoring_wrong_column_number=False,
                overwrite_output_file=False
            )
            input_filepath = os.path.join(tmp_dir, 'input.csv')
            output_filepath = os.path.join(tmp_dir, 'output.json')
            with open(input_filepath, "w") as input_file:
                input_file.write(
                    "id,name,birth,salary,department\n1,Ivan,1980,150000,1"
                )
            asyncio.run(csv_to_json_converter.convert_file(input_filepath, output_filepath))
            with open(output_filepath, "r") as output_file:
                result = output_file.read()
            self.assertEqual(
                '[\n'
                '  {\n'
                '    "id": "1",\n'
                '    "name": "Ivan",\n'
                '    "birth": "1980",\n'
                '    "salary": "150000",\n'
                '    "department": "1"\n'
                '  }\n'
                ']',
                result
            )

    def test_data_convert_correctness(self):
        csv_to_json_converter = AsyncCsvToJsonConverter(
            csv_delimiter=",",
            ignoring_wrong_column_number=False,
            overwrite_output_file=False
        )
        data = [["id", "name", "birth", "salary", "department"], ["1", "Ivan", "1980", "150000", "1"]]
        result = asyncio.run(csv_to_json_converter.convert_data(data))
        self.assertEqual(
            [
                {
                    "id": "1",
                    "name": "Ivan",
                    "birth": "1980",
                    "salary": "150000",
                    "department": "1"
                }
            ],
            result
        )

    def test_only_column_names_data(self):
        csv_to_json_converter = AsyncCsvToJsonConverter(
            csv_delimiter=",",
            ignoring_wrong_column_number=False,
            overwrite_output_file=False
        )
        data = [["id", "name", "birth", "salary", "department"]]
        result = asyncio.run(csv_to_json_converter.convert_data(data))
        self.assertEqual(
            [],
            result
        )

    def test_missing_fields_file(self):
        with TemporaryDirectory() as tmp_dir:
            csv_to_json_converter = AsyncCsvToJsonConverter(
                csv_delimiter=",",
                ignoring_wrong_column_number=False,
                overwrite_output_file=False
            )
            input_filepath = os.path.join(tmp_dir, 'input.csv')
            output_filepath = os.path.join(tmp_dir, 'output.json')
            with open(input_filepath, "w") as input_file:
                input_file.write(
                    "id,name,birth,salary,department\n2,Alex,1960,200000,5\n3,Ivan,,130000,8"
                )
            asyncio.run(csv_to_json_converter.convert_file(input_filepath, output_filepath))
            with open(output_filepath, "r") as output_file:
                result = json.load(output_file)
            self.assertEqual(
                [
                    {
                        "id": "2",
                        "name": "Alex",
                        "birth": "1960",
                        "salary": "200000",
                        "department": "5"
                    },
                    {
                        "id": "3",
                        "name": "Ivan",
                        "birth": "",
                        "salary": "130000",
                        "department": "8"
                    }
                ],
                result
            )


if __name__ == '__main__':
    unittest.main()
