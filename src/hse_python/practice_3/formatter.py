from typing import List

from hse_python.practice_3.utils import Task


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
