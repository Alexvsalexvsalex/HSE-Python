# title Markdown
# description
# Создать markdown описание для выполненных задач
#
# Входные файлы должны удовлетворять структуре
# ```
# '# title <title>
# '# description
# '# <some number of lines with description>
# '# end
# '<code>
# ```
#
# end
import argparse
import asyncio
import logging
import os
from typing import List

from hse_python.practice_3.formatter import generate_task_markdown, generate_package_markdown
from hse_python.practice_3.parser import parse_source
from hse_python.practice_3.utils import Task
from hse_python.utils.decorators import measure_time

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

logger = logging.getLogger('markdown')


@measure_time(logger=logger)
def to_markdown(input_filepath: str, output_filepath: str) -> None:
    if output_filepath is None:
        raise ValueError('File markdown transform require output file name')
    task = asyncio.run(parse_source(input_filepath))

    with open(output_filepath, 'w') as output_file:
        output_file.write(generate_task_markdown(task))


def parse_package(input_package_path) -> List[Task]:
    loop = asyncio.new_event_loop()
    parsing_tasks = []
    for object_name in sorted(os.listdir(input_package_path)):
        object_path = os.path.join(input_package_path, object_name)
        if os.path.isfile(object_path):
            parsing_tasks.append(loop.create_task(parse_source(object_path)))
    loop.run_until_complete(asyncio.gather(*parsing_tasks, return_exceptions=True))
    loop.close()

    tasks = []
    for parsing_task in parsing_tasks:
        try:
            task = parsing_task.result()
            tasks.append(task)
            logger.debug(f"Task `{task.title}` was successfully parsed")
        except RuntimeError as e:
            logger.warning(f"Parsing error: {e}")
    return tasks


@measure_time(logger=logger)
def to_markdown_package(input_package_path: str, output_filepath: str = None) -> None:
    if output_filepath is None:
        output_filepath = os.path.join(input_package_path, 'README.md')
    tasks = parse_package(input_package_path)
    if tasks:
        package_title = os.path.basename(input_package_path).replace('_', ' ').title()
        with open(output_filepath, 'w') as output_file:
            output_file.write(generate_package_markdown(package_title, tasks))
        logger.info(f"{len(tasks)} tasks in package `{package_title}` were parsed and added to output .md file")
    else:
        logger.warning("No correct task files found")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''Application creates markdown file for solved tasks''')
    parser.add_argument('input_path', type=str, help='Path to file or package')
    parser.add_argument('output_file', nargs='?', default=None, type=str, help='Output markdown file location')
    args = parser.parse_args()

    input_path = args.input_path
    output_filepath = args.output_file

    if os.path.isfile(input_path):
        logger.info("File markdown transform")
        to_markdown(input_path, output_filepath)
    elif os.path.isdir(input_path):
        logger.info("Package markdown transform")
        to_markdown_package(input_path, output_filepath)
    else:
        logger.error(f"Unrecognized input path")
        exit(1)
