from hse_python.practice_3.utils import Task
from hse_python.utils.errors import WrongFileStructureError


TITLE_MARK = "# title"
DESCRIPTION_MARK = "# description"
END_MARK = "# end"


def remove_comment_mark(s: str) -> str:
    return s.lstrip(' #')


async def parse_source(input_filepath: str) -> Task:
    with open(input_filepath, 'r') as input_file:
        content = input_file.readlines()

    if len(content) < 3:
        raise WrongFileStructureError(f"File {input_file} contains few lines")

    if not content[0].startswith(TITLE_MARK):
        raise WrongFileStructureError(f"Line #1 of {input_file} must start with title mark `{TITLE_MARK}`")

    if not content[1].strip() == DESCRIPTION_MARK:
        raise WrongFileStructureError(f"Line #2 of {input_file} must contain description mark `{DESCRIPTION_MARK}`")

    end_marker_pos = -1
    for i in range(2, len(content)):
        if content[i].strip() == END_MARK:
            end_marker_pos = i
            break

    if end_marker_pos == -1:
        raise WrongFileStructureError(f"End mark `{END_MARK}` not found in {input_file}")

    title = content[0][len(TITLE_MARK):].strip()
    description = "".join(map(remove_comment_mark, content[2:end_marker_pos]))
    python_code = "".join(content[end_marker_pos + 1:])

    return Task(title, description, python_code)
