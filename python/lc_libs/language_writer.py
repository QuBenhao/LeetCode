import abc
import json
import logging
import os
import subprocess
from pathlib import Path
from typing import Tuple, Optional, List, Dict, Set

from dotenv import load_dotenv

from python.constants import constant


# Type detection constants (immutable)
TREE_NODE_TYPES: frozenset[str] = frozenset({
    "TreeNode", "*TreeNode", "TreeNode*", "TreeNode | null",
    "Option<Rc<RefCell<TreeNode>>>", "Option<Box<TreeNode>>",
    "List[TreeNode]", "[]*TreeNode", "vector<TreeNode*>",
    "TreeNode[]", "Array<TreeNode | null>", "Vec<Option<Rc<RefCell<TreeNode>>>>",
})

LIST_NODE_TYPES: frozenset[str] = frozenset({
    "ListNode", "*ListNode", "ListNode*", "ListNode | null",
    "Option<Box<ListNode>>", "Option<Rc<RefCell<ListNode>>>",
    "List[ListNode]", "[]*ListNode", "vector<ListNode*>",
    "ListNode[]", "Array<ListNode | null>", "Vec<Option<Box<ListNode>>>",
})

# Node type (immutable) - used for all Node subtypes (next, neighbors, random)
# Note: The distinction between subtypes is determined by code content (fields),
# not by type strings, so a single constant suffices.
NODE_TYPES: frozenset[str] = frozenset({
    "Node", "*Node", "Node | null", "_Node | null", "Option<Rc<RefCell<Node>>>"
})


class LanguageWriter(abc.ABC):

    def __init__(self):
        self.solution_file = ""
        self.main_folder = ""
        self.test_file = ""
        self.lang_env_commands = []
        self.test_commands = []

    @staticmethod
    def _resolve_link(problem_path: Path, visited: set = None, original_link_info: dict = None) -> Tuple[Path, Optional[dict]]:
        """
        Resolve problem link if link.json exists.
        Returns (resolved_path, link_info) tuple.
        """
        if visited is None:
            visited = set()

        link_file = problem_path / "link.json"
        if not link_file.exists():
            return problem_path, original_link_info

        problem_id = problem_path.name.split("_")[-1]
        if problem_id in visited:
            raise ValueError(f"Circular link detected involving problem {problem_id}")
        visited.add(problem_id)

        with link_file.open("r", encoding="utf-8") as f:
            link_info = json.load(f)

        if original_link_info is None:
            original_link_info = link_info

        link_to = link_info.get("link_to", "")
        link_folder = link_info.get("link_folder", "problems")
        if not link_to:
            return problem_path, original_link_info

        base_path = problem_path.parent / f"{link_folder}_{link_to}"
        return LanguageWriter._resolve_link(base_path, visited, original_link_info)

    @staticmethod
    def _dump_json(data: dict, file_path: Path):
        """Helper method to dump a dictionary to a JSON file."""
        with file_path.open("w", encoding="utf-8") as f:
            # dump each key-value pair in a single line
            f.write("{\n")
            items = list(data.items())
            for i, (key, value) in enumerate(items):
                if i == len(items) - 1:
                    f.write(f'    "{key}": {json.dumps(value, ensure_ascii=False)}\n')
                else:
                    f.write(f'    "{key}": {json.dumps(value, ensure_ascii=False)},\n')
            f.write("}\n")

    def change_test(self, root_path: Path, problem_folder: str, question_id: str):
        daily_path = root_path / f"daily-{problem_folder}.json"
        json_content = {}
        if daily_path.exists():
            with daily_path.open("r", encoding="utf-8") as f:
                json_content = json.loads(f.read())
        json_content["daily"] = question_id
        LanguageWriter._dump_json(json_content, daily_path)

    def change_tests(self, root_path: Path, problem_ids_folders: list):
        if not problem_ids_folders:
            return
        try:
            load_dotenv(str(root_path / ".env"))
            folder = os.getenv(constant.PROBLEM_FOLDER, "problems")
            if not folder:
                folder = problem_ids_folders[0][1]
        except Exception:
            folder = "problems"
        daily_path = root_path / f"daily-{folder}.json"
        json_content = {}
        if daily_path.exists():
            with daily_path.open("r", encoding="utf-8") as f:
                json_content = json.loads(f.read())
        json_content["plans"] = [
            item for sublist in problem_ids_folders for item in sublist
        ]
        LanguageWriter._dump_json(json_content, daily_path)

    def get_test_problem_id(self, root_path: Path, problem_folder: str) -> Optional[str]:
        """Get the problem ID from the test file."""
        data_path = root_path / f"daily-{problem_folder}.json"
        with data_path.open("r", encoding="utf-8") as f:
            json_content = json.loads(f.read())
        if "daily" in json_content:
            return json_content["daily"]
        if "plans" in json_content and json_content["plans"]:
            return json_content["plans"][0]
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
            self, root_path: Path, problem_folder: str, problem_id: str
    ) -> Tuple[str, str]:
        pass

    def env_check(self) -> bool:
        if not self.lang_env_commands:
            return False
        env = os.environ.copy()  # Inherit shell environment
        for cmd in self.lang_env_commands:
            env_check = subprocess.run(cmd, capture_output=True, timeout=60, env=env)
            if env_check.returncode == 0:
                logging.info(f"[{cmd}] env ok")
                logging.debug(f"[{cmd}] output: {env_check.stdout.decode('utf-8', errors='replace')}")
            else:
                logging.warning(
                    "Execute language env [{}]\n"
                    "output: {}, err: {}".format(
                        " ".join(cmd),
                        env_check.stdout.decode("utf-8", errors="replace"),
                        env_check.stderr.decode("utf-8", errors="replace"),
                    )
                )
                return False
        return True

    def execute_code(self, root_path: Path) -> bool:
        if not self.test_commands:
            return False
        for cmd in self.test_commands:
            try:
                execute_res = subprocess.run(
                    cmd, capture_output=True, timeout=300, cwd=str(root_path)
                )
                if execute_res.returncode == 0:
                    logging.info("Execute [{}] success".format(" ".join(cmd)))
                    logging.debug(
                        "Execute [{}] output: {}".format(
                            " ".join(cmd), execute_res.stdout.decode("utf-8", errors="replace")
                        )
                    )
                    continue
                logging.warning(
                    "Execute failed, command: [{}],"
                    " error: {}, output: {}".format(
                        " ".join(cmd),
                        execute_res.stderr.decode("utf-8", errors="replace"),
                        execute_res.stdout.decode("utf-8", errors="replace"),
                    )
                )
            except subprocess.TimeoutExpired as _:
                logging.info("Execute code timeout, command: [{}]".format(" ".join(cmd)))
                logging.debug("Timeout command: [{}]".format(" ".join(cmd)), exc_info=True)
            return False
        return True

    def run_code(
            self,
            root_path: Path,
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
        solution_file = root_path / problem_folder / f"{problem_folder}_{problem_id}" / self.solution_file
        with solution_file.open("w", encoding="utf-8",) as f:
            code_content = self.write_solution(
                default_code, code, problem_id, problem_folder
            )
            f.writelines(code_content)
        return False

    @staticmethod
    def get_test_cases(problem_folder: str, problem_id: str) -> Optional[List[List]]:
        root_path = Path(__file__).parent.parent.parent
        test_case_path = root_path / problem_folder / f"{problem_folder}_{problem_id}" / "testcase"
        if not test_case_path.exists():
            return None
        testcases = []
        with test_case_path.open("r", encoding="utf-8") as f:
            inputs_str = f.readline()
            inputs_list = json.loads(inputs_str)
            for input_str in inputs_list:
                splits = input_str.split("\n")
                cur = []
                for ipt in splits:
                    cur.append(json.loads(ipt))
                testcases.append(cur)
        return testcases

    # ==================== Type Detection Helpers ====================

    @staticmethod
    def is_tree_node(type_str: str) -> bool:
        """Check if the type string represents a TreeNode type."""
        if not type_str:
            return False
        type_str = type_str.strip()
        # Direct match
        if type_str in TREE_NODE_TYPES:
            return True
        # Partial match for complex types
        return "TreeNode" in type_str

    @staticmethod
    def is_list_node(type_str: str) -> bool:
        """Check if the type string represents a ListNode type."""
        if not type_str:
            return False
        type_str = type_str.strip()
        if type_str in LIST_NODE_TYPES:
            return True
        return "ListNode" in type_str

    @staticmethod
    def is_node_type(type_str: str) -> bool:
        """Check if the type string represents a Node type (not TreeNode/ListNode)."""
        if not type_str:
            return False
        type_str = type_str.strip()
        # Must contain "Node" but not "TreeNode" or "ListNode"
        if "Node" not in type_str:
            return False
        if "TreeNode" in type_str or "ListNode" in type_str:
            return False
        return True

    @staticmethod
    def is_node_next(code_default: str) -> bool:
        """Check if Node has left, right, next structure (binary tree with next pointer)."""
        return ("left" in code_default and "right" in code_default and "next" in code_default and
                LanguageWriter.is_node_type_from_code(code_default, "next"))

    @staticmethod
    def is_node_neighbors(code_default: str) -> bool:
        """Check if Node has neighbors structure (graph node)."""
        return "neighbors" in code_default and LanguageWriter.is_node_type_from_code(code_default, "neighbors")

    @staticmethod
    def is_node_random(code_default: str) -> bool:
        """Check if Node has random pointer structure (linked list with random pointer)."""
        return ("next" in code_default and "random" in code_default and
                not ("left" in code_default and "right" in code_default) and
                LanguageWriter.is_node_type_from_code(code_default, "random"))

    @staticmethod
    def is_node_type_from_code(code_default: str, field: str) -> bool:
        """Helper to detect Node type from code definition."""
        # Check for common Node definition patterns
        patterns = [
            f"// Definition for a Node",
            f"class Node {{",
            f"struct Node {{",
            f"type Node struct",
            f"interface Node",
        ]
        for pattern in patterns:
            if pattern in code_default:
                return True
        return False

    @staticmethod
    def is_list_type(type_str: str) -> bool:
        """Check if the type represents a list/array of something."""
        if not type_str:
            return False
        type_str = type_str.strip()
        list_indicators = ["[]", "List[", "vector<", "Vec<", "Array<", "[]*"]
        return any(indicator in type_str for indicator in list_indicators)

    @staticmethod
    def is_modify_in_place(code_template: str) -> bool:
        """Check if the problem modifies input in place (no return value)."""
        return "Do not return anything" in code_template

    @staticmethod
    def is_cycle_linked_list(testcases: Optional[List], param_count: int) -> bool:
        """Check if testcases indicate a cycle linked list problem.

        Pattern: first param is list, second param is int (position)
        """
        if not testcases or not testcases[0]:
            return False
        first_testcase = testcases[0]
        return (len(first_testcase) == param_count + 1 and
                isinstance(first_testcase[0], list) and
                isinstance(first_testcase[1], int))

    @staticmethod
    def is_intersection_linked_list(testcases: Optional[List]) -> bool:
        """Check if testcases indicate an intersection linked list problem.

        Pattern: [int, list, list, int, int]
        """
        if not testcases or not testcases[0]:
            return False
        first_testcase = testcases[0]
        return (len(first_testcase) == 5 and
                isinstance(first_testcase[0], int) and
                isinstance(first_testcase[1], list) and
                isinstance(first_testcase[2], list) and
                isinstance(first_testcase[3], int) and
                isinstance(first_testcase[4], int))
