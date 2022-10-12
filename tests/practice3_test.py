import os
import unittest
from hse_python.practice_3 import *
from hse_python.utils.errors import WrongFileStructureError

from tempfile import TemporaryDirectory


class MarkdownTestCase(unittest.TestCase):
    def test_file_correctness(self):
        with TemporaryDirectory() as tmp_dir:
            input_filepath = os.path.join(tmp_dir, 'input.py')
            output_filepath = os.path.join(tmp_dir, 'output.md')
            with open(input_filepath, "w") as input_file:
                input_file.write("# title Main title\n# description\n# D\n# end\nsome_code")
            to_markdown(input_filepath, output_filepath)
            with open(output_filepath, "r") as output_file:
                result = output_file.read()
            self.assertEqual(
                '<a name="main-title"><h2>Main title</h2></a>\n'
                "D\n\n"
                "### Solution:\n"
                "```python\nsome_code```",
                result
            )

    def test_package_correctness(self):
        with TemporaryDirectory() as tmp_dir:
            package_name = "my_package_1"
            package_dir = os.path.join(tmp_dir, package_name)
            os.mkdir(package_dir)
            input1_filepath = os.path.join(package_dir, 'input1.py')
            input2_filepath = os.path.join(package_dir, 'input2.py')
            output_filepath = os.path.join(package_dir, 'output.md')
            with open(input1_filepath, "w") as input_file:
                input_file.write("# title Main title1\n# description\n# D1\n# end\nsome_code1")
            with open(input2_filepath, "w") as input_file:
                input_file.write("# title Main title2\n# description\n# D2\n# end\nsome_code2")
            to_markdown_package(package_dir, output_filepath)
            with open(output_filepath, "r") as output_file:
                result = output_file.read()
            self.assertEqual(
                f"# My Package 1\n\n"
                "## Table of contents\n"
                "+ [Main title1](#main-title1)\n"
                "+ [Main title2](#main-title2)\n\n"
                '<a name="main-title1"><h2>Main title1</h2></a>\n'
                "D1\n\n"
                "### Solution:\n"
                "```python\nsome_code1```\n\n"
                '<a name="main-title2"><h2>Main title2</h2></a>\n'
                "D2\n\n"
                "### Solution:\n"
                "```python\nsome_code2```",
                result
            )

    def test_nonexistent_file(self):
        with TemporaryDirectory() as tmp_dir:
            input_filepath = os.path.join(tmp_dir, 'nonexistent.py')
            output_filepath = os.path.join(tmp_dir, 'output.md')
            self.assertRaises(FileNotFoundError, to_markdown, input_filepath, output_filepath)

    def test_incorrect_file(self):
        with TemporaryDirectory() as tmp_dir:
            input_filepath = os.path.join(tmp_dir, 'no_description.py')
            output_filepath = os.path.join(tmp_dir, 'output.md')
            with open(input_filepath, "w") as input_file:
                input_file.write("# title Main title\n# end\nsome_code")
            self.assertRaises(WrongFileStructureError, to_markdown, input_filepath, output_filepath)


if __name__ == '__main__':
    unittest.main()
