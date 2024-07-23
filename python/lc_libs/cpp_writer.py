import os.path
import re
from typing import Tuple
from python.constants import SOLUTION_TEMPLATE_CPP, TESTCASE_TEMPLATE_CPP
from collections import deque

from python.lc_libs.language_writer import LanguageWriter


class CppWriter(LanguageWriter):
    def __init__(self) -> None:
        super().__init__()
        self.solution_file = "Solution.cpp"
        self.main_folder = ""
        self.test_file = "WORKSPACE"
        self.tests_files = ["WORKSPACE", "cpp/tests/BUILD"]
        self.lang_env_commands = [["bazel", "version"]]
        self.test_commands = [
            ["bazel", "test", "--cxxopt=-std=c++20", "//cpp:solution_test"]
        ]

    def change_test(self, root_path, problem_folder: str, question_id: str):
        test_file_path = os.path.join(root_path, self.test_file)
        with open(test_file_path, "r", encoding="utf-8") as f:
            content = f.read()
        with open(test_file_path, "w", encoding="utf-8") as f:
            is_problem = False
            lines = content.split("\n")
            for line_idx, line in enumerate(lines):
                if 'name = "problems",' in line:
                    is_problem = True
                elif is_problem and 'path = "' in line:
                    f.write(
                        '    path = "{}/{}_{}/",\n'.format(
                            problem_folder, problem_folder, question_id
                        )
                    )
                    is_problem = False
                    continue
                if line_idx < len(lines) - 1 or line:
                    f.write(line + "\n")

    def change_tests(self, root_path, problem_ids_folders: list):
        test_file_path0 = os.path.join(root_path, self.tests_files[0])
        with open(test_file_path0, "r", encoding="utf-8") as f:
            content = f.read()
        with open(test_file_path0, "w", encoding="utf-8") as f:
            lines = content.split("\n")
            ans = []
            idx = 0
            while idx < len(lines):
                if "new_local_repository(" in lines[idx]:
                    if 'name = "problems",' in lines[idx + 1]:
                        ans.extend(lines[idx : idx + 5])
                    idx += 5
                    while idx < len(lines) and lines[idx].strip() == "":
                        idx += 1
                    continue
                ans.append(lines[idx])
                idx += 1
            ans.append("")
            for i, (problem_id, problem_folder) in enumerate(problem_ids_folders):
                ans.append("new_local_repository(")
                ans.append(f'    name = "problem{i}",')
                ans.append(
                    f'    path = "{problem_folder}/{problem_folder}_{problem_id}/",'
                )
                ans.append('    build_file = "//cpp:solution.BUILD",')
                ans.append(")")
                ans.append("")
            f.write("\n".join(ans))
        test_file_path1 = os.path.join(root_path, self.tests_files[1])
        with open(test_file_path1, "w", encoding="utf-8") as f:
            for i, (problem_id, _) in enumerate(problem_ids_folders):
                f.write(TESTCASE_TEMPLATE_CPP.format(problem_id, i, i, i) + "\n")

    def write_solution(
        self,
        code_default: str,
        code: str = None,
        problem_id: str = "",
        problem_folder: str = "",
    ) -> str:
        code = code if code else code_default
        is_solution_code = "class Solution" in code
        functions = CppWriter._extract_functions(code_default)

        include_libs = []
        process_variables = []
        return_part = []
        comments = False
        if is_solution_code:
            for line in code.split("\n"):
                if comments and line.strip().endswith("*/"):
                    comments = False
                    continue
                elif comments or line.strip().startswith("#"):
                    continue
                if line.strip().startswith("/*"):
                    comments = True
                    continue
                if "class Solution" in line:
                    break
                include_libs.append(line)
        if " TreeNode " in code_default:
            include_libs.append('#include "cpp/models/TreeNode.h"')
        if " ListNode " in code_default:
            include_libs.append('#include "cpp/models/ListNode.h"')

        if len(functions) == 1:
            ret_type = functions[0].get("ret_type", "")
            func_name = functions[0].get("name", "")
            variables = [
                sp.strip().split(" ") for sp in functions[0].get("args", "").split(",")
            ]
            process_variables.append("\tSolution solution;")
            for i, variable in enumerate(variables):
                rt = (
                    variable[0]
                    if not variable[0].endswith("&") and not variable[0].endswith("*")
                    else variable[0][:-1]
                )
                match rt:
                    case "ListNode":
                        process_variables.append(
                            "std::vector<int> "
                            + variable[1]
                            + "_array"
                            + f" = json::parse(inputArray.at({i}));"
                        )
                        process_variables.append(
                            rt
                            + " *"
                            + variable[1]
                            + f" = IntArrayToListNode({variable[1]}_array);"
                        )
                    case "vector<ListNode*>":
                        process_variables.append(
                            "std::vector<std::vector<int>> "
                            + variable[1]
                            + "_arrays"
                            + f" = json::parse(inputArray.at({i}));"
                        )
                        process_variables.append(
                            f"auto {variable[1]} = {rt}({variable[1]}_arrays.size());"
                        )
                        process_variables.append(
                            "for (int i = 0; i < " + variable[1] + ".size(); i++) {"
                        )
                        process_variables.append(
                            "\t"
                            + variable[1]
                            + "[i] = IntArrayToListNode("
                            + variable[1]
                            + "_arrays[i]);"
                        )
                        process_variables.append("}")
                    case "TreeNode":
                        process_variables.append(
                            "json "
                            + variable[1]
                            + "_array"
                            + f" = json::parse(inputArray.at({i}));"
                        )
                        process_variables.append(
                            rt
                            + " *"
                            + variable[1]
                            + f" = JsonArrayToTreeNode({variable[1]}_array);"
                        )
                    case "vector<TreeNode*>":
                        process_variables.append(
                            "json "
                            + variable[1]
                            + "_array"
                            + f" = json::parse(inputArray.at({i}));"
                        )
                        process_variables.append(
                            rt
                            + " "
                            + variable[1]
                            + f" = JsonArrayToTreeNodeArray({variable[1]}_array);"
                        )
                    case "char":
                        process_variables.append(
                            f"string {variable[1]}_string = json::parse(inputArray.at({i}));"
                        )
                        process_variables.append(
                            f"char {variable[1]} = {variable[1]}_string.length() > 1 ?"
                            f" {variable[1]}_string[1] : {variable[1]}_string[0];"
                        )
                    case "vector<char>":
                        process_variables.append(
                            "vector<string> "
                            + variable[1]
                            + "_str"
                            + f" = json::parse(inputArray.at({i}));"
                        )
                        process_variables.append(
                            f"auto {variable[1]} = {rt}({variable[1]}_str.size());"
                        )
                        process_variables.append(
                            "for (int i = 0; i < " + variable[1] + ".size(); i++) {"
                        )
                        process_variables.append(
                            f"\t{variable[1]}[i] = {variable[1]}_str[i][0];"
                        )
                        process_variables.append("}")
                    case "vector<vector<char>>":
                        process_variables.append(
                            "vector<vector<string>> "
                            + variable[1]
                            + "_str"
                            + f" = json::parse(inputArray.at({i}));"
                        )
                        process_variables.append(
                            f"auto {variable[1]} = {rt}({variable[1]}_str.size(),"
                            f" vector<char>({variable[1]}_str[0].size()));"
                        )
                        process_variables.append(
                            "for (int i = 0; i < " + variable[1] + ".size(); i++) {"
                        )
                        process_variables.append(
                            "\tfor (int j = 0; j < "
                            + variable[1]
                            + "[i].size(); j++) {"
                        )
                        process_variables.append(
                            f"\t\t{variable[1]}[i][j] = {variable[1]}_str[i][j][0];"
                        )
                        process_variables.append("\t}")
                        process_variables.append("}")
                    case _:
                        process_variables.append(
                            rt
                            + " "
                            + variable[1]
                            + f" = json::parse(inputArray.at({i}));"
                        )
            if "ListNode" in ret_type:
                return_part.append(
                    "\treturn ListNodeToIntArray(solution.{}({}));".format(
                        func_name, ", ".join([v[1] for v in variables])
                    )
                )
            elif "TreeNode" in ret_type:
                return_part.append(
                    "\treturn TreeNodeToJsonArray(solution.{}({}));".format(
                        func_name, ", ".join([v[1] for v in variables])
                    )
                )
            elif ret_type == "char":
                return_part.append(
                    "\treturn std::string(1, solution.{}({}));".format(
                        func_name, ", ".join([v[1] for v in variables])
                    )
                )
            elif ret_type == "void":
                return_part.append(
                    "\tsolution.{}({});\n\treturn {};".format(
                        func_name, ", ".join([v[1] for v in variables]), variables[0][1]
                    )
                )
            else:
                return_part.append(
                    "\treturn solution.{}({});".format(
                        func_name, ", ".join([v[1] for v in variables])
                    )
                )
        elif len(functions) > 1:
            process_variables.append(
                "\tvector<string> operators = json::parse(inputArray[0]);"
            )
            process_variables.append(
                "vector<vector<json>> op_values = json::parse(inputArray[1]);"
            )

            class_and_functions = []
            for i, f in enumerate(functions):
                name = f.get("name", "")
                if name and name[0].isupper() and f.get("ret_type", "") == "":
                    cur = f"auto obj{i} = make_shared<{name}>("
                    variables = (
                        [sp.strip().split(" ") for sp in f.get("args", "").split(",")]
                        if f.get("args", "")
                        else []
                    )
                    tmp_vars = []
                    for j, _ in enumerate(variables):
                        tmp_vars.append(f"op_values[{i}][{j}]")
                    cur += ", ".join(tmp_vars)
                    cur += ");"
                    process_variables.append(cur)
                    class_and_functions.append([name, i])

                elif class_and_functions:
                    ret_type = f.get("ret_type", "")
                    func_name = f.get("name", "")
                    variables = (
                        [sp.strip().split(" ") for sp in f.get("args", "").split(",")]
                        if f.get("args", "")
                        else []
                    )
                    class_and_functions[-1].append((func_name, ret_type, variables))
            process_variables.append("vector<json> ans = {nullptr};")
            process_variables.append("for (size_t i = 1; i < op_values.size(); i++) {")
            list_methods = []
            for class_methods in class_and_functions:
                i = class_methods[1]
                for func_name, ret_type, variables in class_methods[2:]:
                    list_methods.append('\tif (operators[i] == "' + func_name + '") {')
                    tmp_vars = []
                    for j, _ in enumerate(variables):
                        tmp_vars.append(f"op_values[i][{j}]")
                    if not ret_type or ret_type == "void":
                        list_methods.append(
                            "\t\tobj{}->{}({});".format(
                                i, func_name, ", ".join(tmp_vars)
                            )
                        )
                        list_methods.append("\t\tans.push_back(nullptr);")
                    else:
                        list_methods.append(
                            "\t\tans.push_back(obj{}->{}({}));".format(
                                i, func_name, ", ".join(tmp_vars)
                            )
                        )
                    list_methods.append("\t\tcontinue;")
                    list_methods.append("\t}")
            process_variables.extend(list_methods)
            process_variables.append("\tans.push_back(nullptr);")
            process_variables.append("}")
            return_part = ["\treturn ans;"]
        return SOLUTION_TEMPLATE_CPP.format(
            "\n".join(include_libs),
            code,
            "\n\t".join(process_variables),
            "\n\t".join(return_part),
        )

    def get_solution_code(
        self, root_path, problem_folder: str, problem_id: str
    ) -> Tuple[str, str]:
        if not problem_id:
            with open(os.path.join(root_path, "WORKSPACE"), "r", encoding="utf-8") as f:
                lines = f.read().split("\n")
                for line in lines:
                    if f'path = "{problem_folder}/{problem_folder}_' in line:
                        problem_id = "_".join(line.split("_")[1:]).split("/")[0]
                        break
        if not problem_id:
            return "", problem_id
        file_path = os.path.join(
            root_path, problem_folder, f"{problem_folder}_{problem_id}", "Solution.cpp"
        )
        if not os.path.exists(file_path):
            return "", problem_id
        final_codes = deque([])
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.read().split("\n")
            for line in lines:
                if line.startswith("//"):
                    continue
                if line.startswith("#include "):
                    continue
                if line.startswith("using "):
                    continue
                if (
                    "json leetcode::qubh::Solve(string input)" in line
                    or "json leetcode::qubh::Solve(string input_json_values)" in line
                ):
                    break
                final_codes.append(line)
        while final_codes and final_codes[0].strip() == "":
            final_codes.popleft()
        return "\n".join(final_codes), problem_id

    @staticmethod
    def _extract_functions(code):
        # First, attempt to remove comments from the code
        no_comments_code = re.sub(r"/\*.*?\*/|//.*?\n", "", code, flags=re.DOTALL)

        # Then we define our pattern
        function_pattern = re.compile(
            r"""
                (?:(?P<access_mod>\b(public|protected|private)\b)\s*:)?     # access modifier followed by :
                \s*
                (?P<ret_type>[^\s:]*\**)?                      # return type, including * to capture pointer return types
                \s*
                (?:(?P<class_name>\b\w+\b)::)?                 # class name, followed by ::
                (?P<name>\b\w+\b)                               # function name
                \(
                (?P<args>[^\)]*)                                # function arguments within parentheses
                \)
            """,
            re.VERBOSE | re.MULTILINE,
        )

        matches = function_pattern.finditer(no_comments_code)

        # Extract and return the information for each function
        functions = []
        for match in matches:
            functions.append(match.groupdict())

        return functions
