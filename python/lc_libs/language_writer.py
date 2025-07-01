import abc
import json
import logging
import os
import subprocess
from typing import Tuple, Optional, List

from dotenv import load_dotenv

from python.constants import constant


class LanguageWriter(abc.ABC):

    def __init__(self):
        self.solution_file = ""
        self.main_folder = ""
        self.test_file = ""
        self.lang_env_commands = []
        self.test_commands = []
    
    @staticmethod
    def _dump_json(data: dict, file_path: str):
        """Helper method to dump a dictionary to a JSON file."""
        with open(file_path, "w", encoding="utf-8") as f:
            # dump each key-value pair in a single line
            f.write("{\n")
            items = list(data.items())
            for i, (key, value) in enumerate(items):
                if i == len(items) - 1:
                    f.write(f'    "{key}": {json.dumps(value, ensure_ascii=False)}\n')
                else:
                    f.write(f'    "{key}": {json.dumps(value, ensure_ascii=False)},\n')
            f.write("}\n")

    def change_test(self, root_path, problem_folder: str, question_id: str):
        daily_path = os.path.join(root_path, f"daily-{problem_folder}.json")
        json_content = {}
        if os.path.exists(daily_path):
            with open(daily_path, "r", encoding="utf-8") as f:
                json_content = json.loads(f.read())
        json_content["daily"] = question_id
        LanguageWriter._dump_json(json_content, daily_path)

    def change_tests(self, root_path, problem_ids_folders: list):
        if not problem_ids_folders:
            return
        try:
            load_dotenv(f"{root_path}/.env")
            folder = os.getenv(constant.PROBLEM_FOLDER, "problems")
        except Exception:
            folder = "problems"
        daily_path = os.path.join(root_path, f"daily-{folder}.json")
        json_content = {}
        if os.path.exists(daily_path):
            with open(daily_path, "r", encoding="utf-8") as f:
                json_content = json.loads(f.read())
        json_content["plan"] = [
            item for sublist in problem_ids_folders for item in sublist
        ]
        LanguageWriter._dump_json(json_content, daily_path)
    
    def get_test_problem_id(self, root_path, problem_folder: str) -> Optional[str]:
        """Get the problem ID from the test file."""
        with open(f"{root_path}/daily-{problem_folder}.json", "r", encoding="utf-8") as f:
            json_content = json.loads(f.read())
        if "daily" in json_content:
            return json_content["daily"]
        if "plan" in json_content and json_content["plan"]:
            return json_content["plan"][0]
        return None

    def write_solution(
            self,
            code_default: str,
            code: str = None,
            problem_id: str = "",
            problem_folder: str = "",
    ) -> str:
        pass

    def write_contest(
            self,
            code_default: str,
            problem_id: str = "",
            contest_folder: str = "",
    ) -> str:
        pass

    def get_solution_code(
            self, root_path, problem_folder: str, problem_id: str
    ) -> Tuple[str, str]:
        pass

    def env_check(self) -> bool:
        if not self.lang_env_commands:
            return False
        for cmd in self.lang_env_commands:
            env_check = subprocess.run(cmd, capture_output=True, timeout=60)
            if env_check.returncode == 0:
                logging.info(f"[{cmd}] env ok")
                logging.debug(f"[{cmd}] output: {env_check.stdout.decode('utf-8')}")
            else:
                logging.warning(
                    "Execute language env [{}]\n"
                    "output: {}, err: {}".format(
                        " ".join(cmd),
                        env_check.stdout.decode("utf-8"),
                        env_check.stderr.decode("utf-8"),
                    )
                )
                return False
        return True

    def execute_code(self, root_path) -> bool:
        if not self.test_commands:
            return False
        for cmd in self.test_commands:
            try:
                execute_res = subprocess.run(
                    cmd, capture_output=True, timeout=300, cwd=root_path
                )
                if execute_res.returncode == 0:
                    logging.info("Execute [{}] success".format(" ".join(cmd)))
                    logging.debug(
                        "Execute [{}] output: {}".format(
                            " ".join(cmd), execute_res.stdout.decode("utf-8")
                        )
                    )
                    continue
                logging.warning(
                    "Execute failed, command: [{}],"
                    " error: {}, output: {}".format(
                        " ".join(cmd),
                        execute_res.stderr.decode("utf-8"),
                        execute_res.stdout.decode("utf-8"),
                    )
                )
            except subprocess.TimeoutExpired as _:
                logging.info("Execute code timeout, command: [{}]".format(" ".join(cmd)))
                logging.debug("Timeout command: [{}]".format(" ".join(cmd)), exc_info=True)
            return False
        return True

    def run_code(
            self,
            root_path,
            problem_folder: str,
            problem_id: str,
            write: bool,
            default_code: str,
            code: str,
    ) -> bool:
        exec_res = False
        if self.env_check():
            before = self.get_test_problem_id(root_path, problem_folder)
            try:
                if before != problem_id:
                    self.change_test(root_path, problem_folder, problem_id)
                exec_res = self.execute_code(root_path)
            finally:
                if before != problem_id:
                    self.change_test(root_path, problem_folder, before)
        if not write or exec_res:
            return exec_res
        with open(
                os.path.join(
                    root_path,
                    problem_folder,
                    f"{problem_folder}_{problem_id}",
                    self.solution_file,
                ),
                "w",
                encoding="utf-8",
        ) as f:
            code_content = self.write_solution(
                default_code, code, problem_id, problem_folder
            )
            f.writelines(code_content)
        return False

    @staticmethod
    def get_test_cases(problem_folder: str, problem_id: str) -> Optional[List[List]]:
        root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        test_case_path = os.path.join(root_path, problem_folder, f"{problem_folder}_{problem_id}", "testcase")
        if not os.path.exists(test_case_path):
            return None
        testcases = []
        with open(test_case_path, "r", encoding="utf-8") as f:
            inputs_str = f.readline()
            inputs_list = json.loads(inputs_str)
            for input_str in inputs_list:
                splits = input_str.split("\n")
                cur = []
                for ipt in splits:
                    cur.append(json.loads(ipt))
                testcases.append(cur)
        return testcases
