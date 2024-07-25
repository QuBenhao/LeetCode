import os
from collections import deque
from typing import Tuple, List

from python.constants import CARGO_TOML_TEMPLATE_SOLUTION, SOLUTION_TEMPLATE_RUST, \
    SOLUTIONS_TEMPLATE_RUST
from python.lc_libs.language_writer import LanguageWriter


class RustWriter(LanguageWriter):

    def __init__(self):
        super().__init__()
        self.solution_file = "solution.rs"
        self.main_folder = "rust"
        self.test_executor_folder = "test_executor"
        self.test_file = "tests/test.rs"
        self.tests_file = "tests/solutions_test.rs"
        self.cargo_file = "Cargo.toml"
        self.lang_env_commands = [["rustc", "--version"], ["cargo", "--version"]]
        self.test_commands = [["cargo", "test", "--test", "solution_test"]]

    def change_test(self, root_path, problem_folder: str, question_id: str):
        test_file_path = os.path.join(root_path, self.main_folder, self.test_executor_folder, self.test_file)
        with open(test_file_path, "r", encoding="utf-8") as f:
            content = f.read()
        with open(test_file_path, "w", encoding="utf-8") as f:
            lines = content.split("\n")
            for line_idx, line in enumerate(lines):
                if "const PROBLEM_FOLDER: &str = \"" in line:
                    f.write(f'const PROBLEM_FOLDER: &str = "{problem_folder}";\n')
                    continue
                if "const PROBLEM_ID: &str = \"" in line:
                    f.write(f'const PROBLEM_ID: &str = "{question_id}";\n')
                    continue
                if " as solution;" in line:
                    f.write(f"\tuse solution_{question_id} as solution;\n")
                    continue
                if line_idx < len(lines) - 1 or line:
                    f.write(f"{line}\n")
        root_cargo_path = os.path.join(root_path, self.cargo_file)
        RustWriter.__cargo_add_problems(root_cargo_path, [[question_id, problem_folder]])

    def change_tests(self, root_path, problem_ids_folders: list):
        root_cargo_path = os.path.join(root_path, self.cargo_file)
        RustWriter.__cargo_add_problems(root_cargo_path, problem_ids_folders)
        tests_file_path = os.path.join(root_path, self.main_folder, self.test_executor_folder, self.tests_file)
        with open(tests_file_path, "w", encoding="utf-8") as f:
            f.write(SOLUTIONS_TEMPLATE_RUST.format(
                len(problem_ids_folders),
                ", ".join([f"[\"{problem_folder}\", \"{problem_id}\"]"
                           for problem_id, problem_folder in problem_ids_folders]),
                "\n\t".join([f"use solution_{problem_id} as solution{i};"
                             for i, (problem_id, _) in enumerate(problem_ids_folders)]),
                "\n\t\t\t\t".join([f"{i} => solution{i}::solve," for i in range(len(problem_ids_folders))]),
            ))

    def write_solution(
            self,
            code_default: str,
            code: str = None,
            problem_id: str = "",
            problem_folder: str = "",
    ) -> str:
        code = code or code_default
        if "impl Solution" not in code:
            raise NotImplementedError("RustWriter does not support problem without Solution yet!")
        if "impl Solution {\n\n    fn new(" in code:
            raise NotImplementedError("RustWriter does not support problem with Solution new function yet!")
        import_libs = []
        solve_part = []
        return_part = []
        fn_count = 0
        for line in code.split("\n"):
            if line.startswith("//"):
                continue
            if "fn " in line:
                function_name, variables, return_type = self.__parse_function(line)
                for i, (var_name, var_type) in enumerate(variables):
                    self.__parse_type(i, var_name, var_type, import_libs, solve_part, return_part)
                if return_type:
                    self.__parse_type(0, "", return_type,
                                      import_libs, solve_part, return_part, True)
                    return_part[-1] = return_part[-1].format(
                        "Solution::{}({})".format(function_name, ", ".join([v[0] for v in variables]))
                    )
                else:
                    return_part.append("Solution::{}({});".format(function_name,
                                                                  ", ".join([v[0] for v in variables])))
                    return_part.append(variables[0][0])
                fn_count += 1
        if fn_count != 1:
            raise NotImplementedError("RustWriter does not support multiple functions yet!")
        solve_part.extend(return_part)
        return SOLUTION_TEMPLATE_RUST.format("\n".join(import_libs), code, problem_id, "\n\t".join(solve_part))

    def write_cargo_toml(self, dir_path, problem_id: str):
        cargo_file_path = os.path.join(dir_path, self.cargo_file)
        if not os.path.exists(cargo_file_path):
            with open(cargo_file_path, "w", encoding="utf-8") as f:
                f.write(CARGO_TOML_TEMPLATE_SOLUTION.format(problem_id, problem_id, problem_id, problem_id))

    def get_solution_code(
            self, root_path, problem_folder: str, problem_id: str
    ) -> Tuple[str, str]:
        if not problem_id:
            test_file_path = os.path.join(root_path, self.main_folder, self.test_executor_folder, self.test_file)
            with open(test_file_path, "r", encoding="utf-8") as f:
                content = f.read()
                for line in content.split("\n"):
                    if "const PROBLEM_ID: &str = \"" in line:
                        problem_id = line.split("\"")[1]
                        break
        if not problem_id:
            return "", problem_id
        file_path = os.path.join(root_path, problem_folder, f"{problem_folder}_{problem_id}", self.solution_file)
        if not os.path.exists(file_path):
            return "", problem_id
        final_codes = deque([])
        with open(file_path, 'r', encoding="utf-8") as f:
            content = f.read()
            start = False
            for line in content.split("\n"):
                if "pub struct Solution;" in line:
                    start = True
                    continue
                if "#[cfg(feature = \"solution\")]" in line or f"#[cfg(feature = \"solution_{problem_id}\")]" in line:
                    break
                if start:
                    final_codes.append(line)
        while final_codes and final_codes[0].strip() == '':
            final_codes.popleft()
        while final_codes and final_codes[-1].strip() == '':
            final_codes.pop()
        return "\n".join(final_codes), problem_id

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
            _, original_problem_id = self.get_solution_code(root_path, "not_exist", "")
            try:
                self.change_test(root_path, problem_folder, problem_id)
                exec_res = self.execute_code(root_path)
            finally:
                if original_problem_id:
                    self.change_test(root_path, problem_folder, original_problem_id)
        if not write:
            return exec_res
        if not exec_res:
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
    def __parse_function(line: str) -> Tuple[str, List[Tuple[str, str]], str]:
        """
        Parse function line to get function name, variables and return type
        :param line: str
        :return: Tuple[str, str, str]
        """
        line = line.strip()
        function_name = line.split("fn ")[-1].strip().split("(")[0]
        variables = line.split("(")[1].split(")")[0]
        var_list = []
        for i, var in enumerate(variables.split(",")):
            var_name, var_type = var.split(":")
            var_list.append((var_name.strip(), var_type.strip()))
        rts = line.split("->")
        return_type = line.split("->")[1].split("{")[0].strip() if len(rts) > 1 else None
        return function_name, var_list, return_type

    @staticmethod
    def __parse_type(var_idx: int, var_name: str, var_type: str, import_libs: List[str], solve_part: List[str],
                     return_parts: List[str], is_return: bool = False):
        """
        Parse variable type to get the corresponding Rust type
        :param var_idx: int
        :param var_name: str, variable name
        :param var_type: str
        :param import_libs: List[str]
        :param solve_part: List[str]
        :param return_parts: List[str]
        :param is_return: bool
        """
        match var_type:
            case "Option<Box<ListNode>>" | "Vec<Option<Box<ListNode>>>":
                idx = -1
                for i, lib in enumerate(import_libs):
                    if "use library::lib::list_node::" in lib:
                        idx = i
                        break
                if idx != -1:
                    before = import_libs[idx].split("::")[-1].split("}")[0].split(";")[0].split("{")[-1].split(",")
                    if "ListNode" not in import_libs[idx]:
                        before.insert(0, "ListNode")
                    if not is_return and "int_array_to_list_node" not in import_libs[idx]:
                        before.append("int_array_to_list_node")
                    elif is_return and "list_node_to_int_array" not in import_libs[idx]:
                        before.append("list_node_to_int_array")
                    import_libs[idx] = "use library::lib::list_node::{" + ", ".join(before) + "};"
                else:
                    if not is_return:
                        import_libs.append("use library::lib::list_node::{ListNode, int_array_to_list_node};")
                    else:
                        import_libs.append("use library::lib::list_node::{ListNode, list_node_to_int_array};")
                if is_return:
                    if var_type == "Vec<Option<Box<ListNode>>>":
                        return_parts.append("let mut res = vec![];")
                        return_parts.append("for node in " + var_name + " {")
                        return_parts.append("\tres.push(list_node_to_int_array(&node));")
                        return_parts.append("}")
                        return_parts.append("json!(res)")
                    else:
                        return_parts.append("json!(list_node_to_int_array(&{}))")
                else:
                    if var_type == "Vec<Option<Box<ListNode>>>":
                        solve_part.append(f"let input_nums{var_idx}: Vec<Vec<i32>> = serde_json::from_str("
                                          f"&input_values[{var_idx}]).expect(\"Failed to parse input\");")
                        solve_part.append(f"let {var_name}: Vec<Option<Box<ListNode>>> = input_nums{var_idx}."
                                          f"into_iter().map(|nums| int_array_to_list_node(&nums)).collect();")
                    else:
                        solve_part.append(f"let input_nums{var_idx}: Vec<i32> = serde_json::from_str("
                                          f"&input_values[{var_idx}]).expect(\"Failed to parse input\");")
                        solve_part.append(f"let {var_name}: Option<Box<ListNode>> ="
                                          f" int_array_to_list_node(&input_nums{var_idx});")

            case "Option<Rc<RefCell<TreeNode>>>" | "Vec<Option<Rc<RefCell<TreeNode>>>>":
                idx = -1
                for i, lib in enumerate(import_libs):
                    if "use library::lib::tree_node::" in lib:
                        idx = i
                        break
                if idx != -1:
                    before = import_libs[idx].split("::")[-1].split("}")[0].split(";")[0].split("{")[-1].split(",")
                    if "TreeNode" not in import_libs[idx]:
                        before.insert(0, "TreeNode")
                    if not is_return and "array_to_tree" not in import_libs[idx]:
                        before.append("array_to_tree")
                    elif is_return and "tree_to_array" not in import_libs[idx]:
                        before.append("tree_to_array")
                    import_libs[idx] = "use library::lib::tree_node::{" + ", ".join(before) + "};"
                else:
                    if not is_return:
                        import_libs.append("use library::lib::tree_node::{TreeNode, array_to_tree};")
                    else:
                        import_libs.append("use library::lib::tree_node::{TreeNode, tree_to_array};")
                if is_return:
                    return_parts.append("json!(tree_to_array(&{}))")
                else:
                    if var_type == "Vec<Option<Rc<RefCell<TreeNode>>>>":
                        solve_part.append(f"let input_values{var_idx}: Vec<String> = serde_json::from_str("
                                          f"&input_values[{var_idx}]).expect(\"Failed to parse input\");")
                        solve_part.append(f"let {var_name}: Vec<Option<Rc<RefCell<TreeNode>>> ="
                                          f" input_values{var_idx}.into_iter().map(|s| array_to_tree(&s)).collect();")
                    else:
                        solve_part.append(f"let input_vec{var_idx}: Vec<Option<i32>> = serde_json::from_str("
                                          f"&input_values[{var_idx}]).expect(\"Failed to parse input\");")
                        solve_part.append(f"let {var_name}: Option<Rc<RefCell<TreeNode>>> ="
                                          f" array_to_tree(&input_vec{var_idx});")
            case _:
                if is_return:
                    return_parts.append("json!({})")
                else:
                    solve_part.append("let {}: {} = serde_json::from_str(&input_values[{}])"
                                      ".expect(\"Failed to parse input\");"
                                      .format(var_name, var_type, var_idx))

    @staticmethod
    def __cargo_add_problems(file_path, problem_ids_folders: list):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        remain = set((problem_id, problem_folder) for problem_id, problem_folder in problem_ids_folders)
        remain_dependencies = set(remain)
        with open(file_path, "w", encoding="utf-8") as f:
            member_start = False
            dependencies_start = False
            splits = content.split("\n")
            for line_idx, line in enumerate(splits):
                if "members = [" in line:
                    f.write(line + "\n")
                    member_start = True
                    continue
                if member_start:
                    if "]" in line:
                        member_start = False
                        for problem_id, problem_folder in remain:
                            f.write(f"\t\"{problem_folder}/{problem_folder}_{problem_id}\",\n")
                        f.write(line + "\n")
                        continue
                    if "rust/" not in line:
                        pf = line.split("/")[0].split("\"")[-1].strip()
                        pi = line.split("_")[-1].split("\"")[0].strip()
                        if (pi, pf) in remain:
                            remain.remove((pi, pf))
                    f.write(line + "\n")
                    continue
                if "[dependencies]" in line:
                    dependencies_start = True
                    f.write(line + "\n")
                    continue
                if dependencies_start:
                    if "path =" in line and "rust/" not in line:
                        pf = line.split("/")[0].split("\"")[-1].strip()
                        pi = line.split("_")[-1].split("\"")[0].strip()
                        if (pi, pf) in remain_dependencies:
                            remain_dependencies.remove((pi, pf))
                if line_idx < len(splits) - 1 or line:
                    f.write(line + "\n")
            for problem_id, problem_folder in remain_dependencies:
                f.write(f"solution_{problem_id} = {{ path = \"{problem_folder}/{problem_folder}_{problem_id}\", "
                        f"features = [\"solution_{problem_id}\"] }}\n")
