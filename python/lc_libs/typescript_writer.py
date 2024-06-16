import os.path

from python.constants import SOLUTION_TEMPLATE_TYPESCRIPT


def change_test_typescript(content: str, question_id: str) -> str:
    pass


def write_solution_typescript(code_default: str, code: str = None, problem_id: str = "") -> str:
    return SOLUTION_TEMPLATE_TYPESCRIPT.format("import part\n", code_default, "{", "\tprocess input", "return", "}")


def get_solution_code_typescript(root_path, problem_folder: str, problem_id: str) -> (str, str):
    pass
