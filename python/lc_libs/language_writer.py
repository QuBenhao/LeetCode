import abc


class LanguageWriter(abc.ABC):
    def change_test(self, content: str, problem_folder: str, question_id: str) -> str:
        pass

    def write_solution(self, code_default: str, code: str = None,
                       problem_id: str = "", problem_folder: str = "") -> str:
        pass

    def get_solution_code(self, root_path, problem_folder: str, problem_id: str) -> (str, str):
        pass
