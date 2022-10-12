# Practice 3

## Table of contents
+ [Markdown](#markdown)

<a name="markdown"><h2>Markdown</h2></a>
Создать markdown описание для выполненных задач

Входные файлы должны удовлетворять структуре
```
'# title <title>
'# description
'# <some number of lines with description>
'# end
'<code>
```


### Solution:
```python
import argparse
import logging
import os
from typing import List, NamedTuple

from hse_python.utils.errors import WrongFileStructureError

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

TITLE_MARK = "# title"
DESCRIPTION_MARK = "# description"
END_MARK = "# end"


class Task(NamedTuple):
    title: str
    description: str
    code: str


def remove_comment_mark(s: str) -> str:
    return s.lstrip(' #')


def parse_source(input_filepath: str) -> Task:
    with open(input_filepath, 'r') as input_file:
        content = input_file.readlines()

    if len(content) < 3:
        raise WrongFileStructureError("File contains few lines")

    if not content[0].startswith(TITLE_MARK):
        raise WrongFileStructureError(f"Line #1 must start with title mark `{TITLE_MARK}`")

    if not content[1].strip() == DESCRIPTION_MARK:
        raise WrongFileStructureError(f"Line #2 must contain description mark `{DESCRIPTION_MARK}`")

    end_marker_pos = -1
    for i in range(2, len(content)):
        if content[i].strip() == END_MARK:
            end_marker_pos = i
            break

    if end_marker_pos == -1:
        raise WrongFileStructureError(f"End mark `{END_MARK}` not found")

    title = content[0][len(TITLE_MARK):].strip()
    description = "".join(map(remove_comment_mark, content[2:end_marker_pos]))
    python_code = "".join(content[end_marker_pos + 1:])

    return Task(title, description, python_code)


def make_correct_link(title: str) -> str:
    return title.lower().replace(' ', '-')


def make_hyperlink(title: str) -> str:
    return f"+ [{title}](#{make_correct_link(title)})"


def make_file_title(title: str) -> str:
    return f"# {title}"


def make_table_of_contents(tasks: List[Task]) -> str:
    hyperlinks = [make_hyperlink(task.title) for task in tasks]
    return "## Table of contents\n" + "\n".join(hyperlinks)


def make_task_paragraph(task: Task) -> str:
    return f'<a name="{make_correct_link(task.title)}"><h2>{task.title}</h2></a>\n' \
           f"{task.description}\n" \
           f"### Solution:\n" \
           f"```python\n{task.code}```"


def generate_task_markdown(task: Task) -> str:
    return make_task_paragraph(task)


def generate_package_markdown(package_title: str, tasks: List[Task]) -> str:
    paragraphs = [make_task_paragraph(task) for task in tasks]
    return \
        make_file_title(package_title) + "\n\n" + \
        make_table_of_contents(tasks) + "\n\n" + \
        "\n\n".join(paragraphs)


def to_markdown(input_filepath: str, output_filepath: str) -> None:
    if output_filepath is None:
        raise ValueError('File markdown transform require output file name')
    task = parse_source(input_filepath)

    with open(output_filepath, 'w') as output_file:
        output_file.write(generate_task_markdown(task))


def to_markdown_package(input_package_path: str, output_filepath: str = None) -> None:
    if output_filepath is None:
        output_filepath = os.path.join(input_package_path, 'README.md')
    tasks = []
    for object_name in sorted(os.listdir(input_package_path)):
        object_path = os.path.join(input_package_path, object_name)
        if os.path.isfile(object_path):
            try:
                task = parse_source(object_path)
                tasks.append(task)
                logging.info(f"{object_path} was successfully parsed")
            except RuntimeError as e:
                logging.warning(f"{object_path} is not correct task file: {e}")
    if tasks:
        package_title = os.path.basename(input_package_path).replace('_', ' ').title()
        with open(output_filepath, 'w') as output_file:
            output_file.write(generate_package_markdown(package_title, tasks))
        logging.info(f"{len(tasks)} tasks were parsed and added to output .md file")
    else:
        logging.warning("No correct task files found")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''Application creates markdown file for solved tasks''')
    parser.add_argument('input_path', type=str, help='Path to file or package')
    parser.add_argument('output_file', nargs='?', default=None, type=str, help='Output markdown file location')
    args = parser.parse_args()

    input_path = args.input_path
    output_filepath = args.output_file

    if os.path.isfile(input_path):
        logging.info("File markdown transform")
        to_markdown(input_path, output_filepath)
    elif os.path.isdir(input_path):
        logging.info("Package markdown transform")
        to_markdown_package(input_path, output_filepath)
    else:
        logging.error(f"Unrecognized input path")
        exit(1)
```