# title Csv to Json converter
# description
# Конвертировать csv файл в json файл
# end
import argparse
import asyncio
import csv
import json
import logging
import os.path
import sys
from typing import List, Dict

from hse_python.practice_7 import config_loader
from hse_python.utils.decorators import async_measure_time
from hse_python.utils.errors import WrongCsvStructureError

config = config_loader.Config()

logger = logging.getLogger(__name__)
logger.setLevel(logging.getLevelName(config.get(config_loader.LOGGING_LEVEL)))

handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(logging.Formatter(fmt=config.get(config_loader.LOGGING_FORMAT)))

# https://stackoverflow.com/a/55877763
logger.propagate = False
logger.addHandler(handler)


class AsyncCsvToJsonConverter:
    def __init__(self,
                 csv_delimiter: str,
                 ignoring_wrong_column_number: bool,
                 overwrite_output_file: bool):
        self.csv_delimiter = csv_delimiter
        self.ignoring_wrong_column_number = ignoring_wrong_column_number
        self.overwrite_output_file = overwrite_output_file

    def __read_data(self, input_file: str):
        with open(input_file, mode='r', newline='') as f:
            reader = csv.reader(f, delimiter=self.csv_delimiter)
            return list(reader)

    def __convert_row(self, columns: List[str], row: List[str]):
        if not self.ignoring_wrong_column_number and len(columns) != len(row):
            raise WrongCsvStructureError(f"Different numbers of columns in rows {columns} and {row}")
        return dict(zip(columns, row))

    @async_measure_time(logger=logger)
    async def convert_data(self, data: List[List[str]]):
        if len(data) == 0:
            raise WrongCsvStructureError(f"No rows in csv file {input_file}")
        columns = data[0]
        result = [self.__convert_row(columns, row) for row in data[1:]]
        return result

    def __write_data(self, output_file: str, data: List[Dict[str, str]]):
        if not self.overwrite_output_file and os.path.exists(output_file):
            raise FileExistsError("Output file already exists, maybe you want to use overwrite mode")
        with open(output_file, mode='w') as f:
            json.dump(data, f, indent=2)

    @async_measure_time(logger=logger)
    async def convert_file(self, input_file: str, output_file: str):
        logger.info("Csv to json conversation")
        data = self.__read_data(input_file)
        logger.debug(f"Got {len(data)} rows from input file")
        converted_data = await self.convert_data(data)
        logger.debug(f"Writing {len(converted_data)} rows to output file")
        self.__write_data(output_file, converted_data)
        logger.info(f"Converting {len(converted_data)} rows was successfully finished")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''Application converts csv file to json file''')
    parser.add_argument('input_file', type=str, help='Input file location')
    parser.add_argument('output_file', type=str, help='Output file location')
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file

    converter = AsyncCsvToJsonConverter(
        csv_delimiter=config.get(config_loader.CSV_DELIMITER),
        ignoring_wrong_column_number=config.get(config_loader.IGNORING_WRONG_COLUMN_NUMBER),
        overwrite_output_file=config.get(config_loader.OVERWRITE_OUTPUT_FILE),
    )
    asyncio.run(converter.convert_file(input_file, output_file))
