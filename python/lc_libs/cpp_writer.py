import logging
import os.path
import re
from typing import Optional, Tuple
from python.constants import SOLUTION_TEMPLATE_CPP, TESTCASE_TEMPLATE_CPP
from collections import deque

from python.lc_libs.language_writer import LanguageWriter


class CppWriter(LanguageWriter):
    def __init__(self) -> None:
        super().__init__()
        self.solution_file = "Solution.cpp"
        self.main_folder = ""
        self.test_file = "MODULE.bazel"
        self.tests_files = ["MODULE.bazel", "cpp/tests/BUILD"]
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
                        ans.extend(lines[idx: idx + 5])
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
        code = code or code_default
        is_solution_code = "class Solution" in code
        functions = CppWriter._extract_functions(code_default)
        testcases = LanguageWriter.get_test_cases(problem_folder, problem_id)

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

        if len(functions) == 1:
            ret_type = functions[0].get("ret_type", "").strip()
            func_name = functions[0].get("name", "")
            variables = [
                [" ".join(sp.strip().split(" ")[:-1]), sp.strip().split(" ")[-1]]
                for sp in functions[0].get("args", "").split(",")
            ]
            process_variables.append("\tSolution solution;")
            if_modify_in_place = CppWriter._process_variables(variables, process_variables, include_libs, code_default,
                                                              testcases)
            CppWriter._process_return_part(ret_type, func_name, variables, code_default, return_part, include_libs,
                                           if_modify_in_place, process_variables)
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
                        [[" ".join(sp.strip().split(" ")[:-1]), sp.strip().split(" ")[-1]]
                         for sp in f.get("args", "").split(",")]
                        if f.get("args", "")
                        else []
                    )
                    logging.debug("variables: %s", variables)
                    tmp_vars = []
                    for j, (var_tp, var_nm) in enumerate(variables):
                        rt = CppWriter._simplify_variable_type([var_tp])
                        logging.debug("Processing variable: \"%s\", return type: \"%s\"", var_tp, rt)
                        match rt:
                            case "vector<int>":
                                process_variables.insert(2, f"vector<int> {var_nm}_array"
                                                            f" = op_values[{i}][{j}].get<vector<int>>();")
                                tmp_vars.append(f"{var_nm}_array")
                            case "TreeNode":
                                if '#include "cpp/models/TreeNode.h"' not in include_libs:
                                    include_libs.append('#include "cpp/models/TreeNode.h"')
                                tmp_vars.append(f"JsonArrayToTreeNode(op_values[{i}][{j}])")
                            case _:
                                logging.debug("Unhandled variable type: %s", rt)
                                tmp_vars.append(f"op_values[{i}][{j}]")
                    cur += ", ".join(tmp_vars)
                    cur += ");"
                    process_variables.append(cur)
                    class_and_functions.append([name, i])

                elif class_and_functions:
                    ret_type = f.get("ret_type", "").strip()
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
                    logging.debug("ret_type: %s", ret_type)
                    if not ret_type or ret_type == "void":
                        list_methods.append(
                            "\t\tobj{}->{}({});".format(
                                i, func_name, ", ".join(tmp_vars)
                            )
                        )
                        list_methods.append("\t\tans.push_back(nullptr);")
                    elif "TreeNode" in ret_type:
                        if '#include "cpp/models/TreeNode.h"' not in include_libs:
                            include_libs.append('#include "cpp/models/TreeNode.h"')
                        list_methods.append(
                            "\t\tans.push_back(TreeNodeToJsonArray(obj{}->{}({})));".format(
                                i, func_name, ", ".join(tmp_vars)
                            )
                        )
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
            with open(os.path.join(root_path, "MODULE.bazel"), "r", encoding="utf-8") as f:
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
            content = f.read()
            end_index = content.find("json leetcode::qubh::Solve(string ")
            start_index = content.find("using json = nlohmann::json;")
            start_index = content.find("\n", start_index) + 1
            logging.debug("start_index: %d, end_index: %d", start_index, end_index)
            final_codes.extend(content[start_index:end_index].strip().split("\n"))
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
                (?P<ret_type>[^\s:]*\s*\*?)?                                # return type, including * with optional space
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
            logging.debug("ret_type: \"%s\"", match.group("ret_type"))
            logging.debug("args: \"%s\"", match.group("args"))
            functions.append(match.groupdict())

        return functions

    @staticmethod
    def _process_variables(variables, process_variables: list, include_libs: list, code_default: str, testcases=None) -> \
            Optional[str]:
        i = 0
        if_modify_in_place = None
        extra_parts = []
        while i < len(variables):
            variable = variables[i]
            rt = CppWriter._simplify_variable_type(variable)
            logging.debug(f"Processing variable: \"%s\", return type: \"%s\"", variable, rt)
            match rt:
                case "ListNode":
                    if '#include "cpp/models/ListNode.h"' not in include_libs:
                        include_libs.append('#include "cpp/models/ListNode.h"')
                    if testcases:
                        if len(testcases[0]) == len(variables) + 1 and all(
                                isinstance(testcase[0], list)
                                and isinstance(testcase[1], int)
                                for testcase in testcases):
                            variable[-1] = variable[-1][1:]
                            process_variables.append(
                                f"std::vector<int> {variable[1]}_array = json::parse(inputArray.at({i}));"
                            )
                            process_variables.append(
                                f"int position = json::parse(inputArray.at({i + 1}));"
                            )
                            process_variables.append(
                                f"ListNode* {variable[1]} = IntArrayToListNodeCycle({variable[1]}_array, position);"
                            )
                            i += 2
                            continue
                        elif (len(variables) == 2 and len(testcases[0]) == 5
                              and all(isinstance(testcase[0], int) and isinstance(testcase[1], list) and
                                      isinstance(testcase[2], list) and isinstance(testcase[3], int) and
                                      isinstance(testcase[4], int) for testcase in testcases)):
                            variables[0][-1] = variables[0][-1][1:]
                            variables[1][-1] = variables[1][-1][1:]
                            process_variables.append(f"int iv = json::parse(inputArray.at({i}));")
                            process_variables.append(
                                f"std::vector<int> {variables[0][1]}_array = json::parse(inputArray.at({i + 1}));")
                            process_variables.append(
                                f"std::vector<int> {variables[1][1]}_array = json::parse(inputArray.at({i + 2}));")
                            process_variables.append(f"int skip_a = json::parse(inputArray.at({i + 3}));")
                            process_variables.append(f"int skip_b = json::parse(inputArray.at({i + 4}));")
                            process_variables.append(
                                f"auto tp = IntArrayToIntersectionListNode(iv, {variables[0][1]}_array, {variables[1][1]}_array, skip_a, skip_b);")
                            process_variables.append(f"ListNode *{variables[0][1]} = get<0>(tp);")
                            process_variables.append(f"ListNode *{variables[1][1]} = get<1>(tp);")
                            i += 5
                            continue
                        elif len(variables) != len(testcases[0]):
                            logging.debug(f"Testcases: {testcases}, variables: {variables}")
                    process_variables.append(
                        "std::vector<int> "
                        + variable[-1]
                        + "_array"
                        + f" = json::parse(inputArray.at({i}));"
                    )
                    process_variables.append(
                        rt
                        + " *"
                        + variable[-1]
                        + f" = IntArrayToListNode({variable[1]}_array);"
                    )
                    if not if_modify_in_place:
                        if_modify_in_place = f"ListNodeToIntArray({variable[-1]})"
                case "vector<ListNode*>":
                    if '#include "cpp/models/ListNode.h"' not in include_libs:
                        include_libs.append('#include "cpp/models/ListNode.h"')
                    process_variables.append(
                        "std::vector<std::vector<int>> "
                        + variable[1]
                        + "_arrays"
                        + f" = json::parse(inputArray.at({i}));"
                    )
                    process_variables.append(
                        f"auto {variable[-1]} = {rt}({variable[-1]}_arrays.size());"
                    )
                    process_variables.append(
                        "for (int i = 0; i < " + variable[-1] + ".size(); i++) {"
                    )
                    process_variables.append(
                        "\t"
                        + variable[-1]
                        + "[i] = IntArrayToListNode("
                        + variable[-1]
                        + "_arrays[i]);"
                    )
                    process_variables.append("}")
                    if not if_modify_in_place:
                        if_modify_in_place = f"ListNodeToIntArray({variable[-1]}[0])"
                case "TreeNode":
                    if '#include "cpp/models/TreeNode.h"' not in include_libs:
                        include_libs.append('#include "cpp/models/TreeNode.h"')
                    if testcases:
                        if len(variables) == len(testcases[0]) + 1:
                            process_variables.append(
                                f"json {variable[1]}_array = json::parse(inputArray.at({i}));")
                            process_variables.append("int target_val = json::parse(inputArray.at(1));")
                            process_variables.append(f"auto nodes = JsonArrayToTreeNodeWithTargets("
                                                     f"{variable[-1]}_array, {{target_val}});")
                            process_variables.append("TreeNode *original = nodes[0];")
                            process_variables.append("TreeNode *target = nodes[1];")
                            process_variables.append(
                                f"TreeNode *cloned = JsonArrayToTreeNode({variable[-1]}_array);")
                            i += 3
                            continue
                        idx = i + 1
                        while all(idx < len(testcase)
                                  and "TreeNode" == CppWriter._simplify_variable_type(variables[idx])
                                  and testcase[idx] is not None
                                  and not isinstance(testcase[idx], list) for testcase in testcases):
                            idx += 1
                        if idx != i + 1:
                            process_variables.append(
                                f"json {variable[-1]}_array = json::parse(inputArray.at({i}));")
                            for j in range(i + 1, idx):
                                process_variables.append(
                                    f"int {variables[j][-1]}_val = json::parse(inputArray.at({j}));")
                            process_variables.append(
                                f"auto nodes = JsonArrayToTreeNodeWithTargets({variable[-1]}_array, {{"
                                + ", ".join([f"{variables[j][-1]}_val" for j in range(i + 1, idx)]) + "});")
                            process_variables.append(f"TreeNode *{variable[-1]} = nodes[0], "
                                                     + ", ".join([f"*{variables[j][-1]} = nodes[{j - i}]"
                                                                  for j in range(i + 1, idx)]) + ";")
                            i = idx
                            continue
                    process_variables.append(
                        "json "
                        + variable[-1]
                        + "_array"
                        + f" = json::parse(inputArray.at({i}));"
                    )
                    process_variables.append(
                        rt
                        + " *"
                        + variable[-1]
                        + f" = JsonArrayToTreeNode({variable[-1]}_array);"
                    )
                    if not if_modify_in_place:
                        if_modify_in_place = f"TreeNodeToJsonArray({variable[-1]})"
                case "vector<TreeNode*>":
                    if '#include "cpp/models/TreeNode.h"' not in include_libs:
                        include_libs.append('#include "cpp/models/TreeNode.h"')
                    process_variables.append(
                        "json "
                        + variable[-1]
                        + "_array"
                        + f" = json::parse(inputArray.at({i}));"
                    )
                    process_variables.append(
                        rt
                        + " "
                        + variable[-1]
                        + f" = JsonArrayToTreeNodeArray({variable[-1]}_array);"
                    )
                    if not if_modify_in_place:
                        if_modify_in_place = f"TreeNodeToJsonArray({variable[-1]}_array[0])"
                case "char":
                    process_variables.append(
                        f"string {variable[-1]}_string = json::parse(inputArray.at({i}));"
                    )
                    process_variables.append(
                        f"char {variable[-1]} = {variable[-1]}_string.length() > 1 ?"
                        f" {variable[-1]}_string[1] : {variable[-1]}_string[0];"
                    )
                case "vector<char>":
                    process_variables.append(
                        "vector<string> "
                        + variable[-1]
                        + "_str"
                        + f" = json::parse(inputArray.at({i}));"
                    )
                    process_variables.append(
                        f"auto {variable[-1]} = {rt}({variable[-1]}_str.size());"
                    )
                    process_variables.append(
                        "for (int i = 0; i < " + variable[-1] + ".size(); i++) {"
                    )
                    process_variables.append(
                        f"\t{variable[-1]}[i] = {variable[-1]}_str[i][0];"
                    )
                    process_variables.append("}")
                case "vector<vector<char>>":
                    process_variables.append(
                        "vector<vector<string>> "
                        + variable[-1]
                        + "_str"
                        + f" = json::parse(inputArray.at({i}));"
                    )
                    process_variables.append(
                        f"auto {variable[-1]} = {rt}({variable[-1]}_str.size(),"
                        f" vector<char>({variable[-1]}_str[0].size()));"
                    )
                    process_variables.append(
                        "for (int i = 0; i < " + variable[-1] + ".size(); i++) {"
                    )
                    process_variables.append(
                        "\tfor (int j = 0; j < "
                        + variable[-1]
                        + "[i].size(); j++) {"
                    )
                    process_variables.append(
                        f"\t\t{variable[-1]}[i][j] = {variable[-1]}_str[i][j][0];"
                    )
                    process_variables.append("\t}")
                    process_variables.append("}")
                case "Node":
                    if ("Node* left;" in code_default and "Node* right;" in code_default
                            and "Node* next;" in code_default):
                        include_libs.append('#include "cpp/models/TreeNodeNext.h"')
                        process_variables.append(
                            "json "
                            + variable[-1]
                            + "_array"
                            + f" = json::parse(inputArray.at({i}));"
                        )
                        process_variables.append(
                            rt
                            + " *"
                            + variable[-1]
                            + f" = JsonArrayToTreeNodeNext({variable[-1]}_array);"
                        )
                    elif "vector<Node*> neighbors;" in code_default:
                        include_libs.append('#include "cpp/models/NodeNeighbors.h"')
                        process_variables.append(f"vector<vector<int>> {variable[-1]}_arrays ="
                                                 f" json::parse(inputArray.at({i}));")
                        process_variables.append(f"{rt}* {variable[-1]} ="
                                                 f" JsonArrayToNodeNeighbors({variable[-1]}_arrays);")
                    elif "Node* random;" in code_default:
                        include_libs.append('#include "cpp/models/NodeRandom.h"')
                        process_variables.append(
                            rt
                            + " *"
                            + variable[-1]
                            + f" = JsonArrayToNodeRandom(json::parse(inputArray.at({i})));"
                        )
                    else:
                        logging.debug(f"Unhandled Node Type variable: {variable}, code: [{code_default}]")
                case _:
                    logging.debug("Unhandled variable type: %s", rt)
                    found_defination = False
                    mit = re.finditer(r"// Definition for (\w+).", code_default)
                    for m in mit:
                        if m.group(1) in rt:
                            class_name = m.group(1)
                            logging.debug("Match custom Class at %d-%d, %s", m.start(), m.end(), class_name)
                            start_index = m.start()
                            end_index = code_default.find("*/")
                            logging.debug("Add extra class code:\n%s", code_default[start_index:end_index])
                            extra_parts.extend(code_default[start_index:end_index].split("\n"))
                            extra_parts.append("")
                            extra_parts.append(f"static {class_name}* {class_name.lower()}_from_input(json input) {{")
                            extra_parts.append("\treturn nullptr;")
                            extra_parts.append("}")
                            found_defination = True
                            process_variables.append(f"{rt} {variable[-1]};")
                            if "vector" in rt:
                                process_variables.append(f"vector<json> {variable[-1]}_input = json::parse(inputArray.at({i}));")
                                process_variables.append(f"for (json ipt: {variable[-1]}_input) {{")
                                process_variables.append(f"\t{variable[-1]}.emplace_back({class_name.lower()}_from_input(ipt));")
                                process_variables.append("}")
                            else:
                                process_variables.append(f"{variable[-1]} = {class_name.lower()}_from_input(inputArray.at({i}))")
                    if not found_defination:
                        process_variables.append(
                            rt
                            + " "
                            + variable[-1]
                            + f" = json::parse(inputArray.at({i}));"
                        )
            i += 1
        if extra_parts:
            include_libs.append("")
            include_libs.extend(extra_parts)
        return if_modify_in_place

    @staticmethod
    def _process_return_part(ret_type: str, func_name: str, variables: list, code_default: str, return_part: list,
                             include_libs: list, if_modify_in_place: Optional[str], process_variables: list):
        if "ListNode" in ret_type:
            # IntArrayToListNodeCycle
            logging.debug(f"Process variables: {process_variables}")
            if any("IntArrayToListNodeCycle" in pv for pv in process_variables):
                return_part.append(
                    "\tListNode *res = solution.{}({});".format(
                        func_name, ", ".join([v[-1] for v in variables])
                    )
                )
                return_part.append("return res ? res->val : nullptr;")
            else:
                if '#include "cpp/models/ListNode.h"' not in include_libs:
                    include_libs.append('#include "cpp/models/ListNode.h"')
                return_part.append(
                    "\treturn ListNodeToIntArray(solution.{}({}));".format(
                        func_name, ", ".join([v[-1] for v in variables])
                    )
                )
        elif "TreeNode" in ret_type:
            if '#include "cpp/models/TreeNode.h"' not in include_libs:
                include_libs.append('#include "cpp/models/TreeNode.h"')
            return_part.append(
                "\treturn TreeNodeToJsonArray(solution.{}({}));".format(
                    func_name, ", ".join([v[-1] for v in variables])
                )
            )
        elif "Node" in ret_type:
            if ("Node* left;" in code_default and "Node* right;" in code_default
                    and "Node* next;" in code_default):
                return_part.append(
                    "\treturn TreeNodeNextToJsonArray(solution.{}({}));".format(
                        func_name, ", ".join([v[-1] for v in variables])
                    )
                )
            elif "vector<Node*> neighbors;" in code_default:
                return_part.append(
                    "\treturn NodeNeighborsToJsonArray(solution.{}({}));".format(
                        func_name, ", ".join([v[-1] for v in variables])
                    )
                )
            elif "Node* random;" in code_default:
                return_part.append(
                    "\treturn NodeRandomToJsonArray(solution.{}({}));".format(
                        func_name, ", ".join([v[-1] for v in variables])
                    )
                )
            else:
                logging.debug(f"Unhandled Node Type return: {ret_type}, code: [{code_default}]")
                return_part.append(
                    "\treturn solution.{}({});".format(
                        func_name, ", ".join([v[-1] for v in variables])
                    )
                )
        elif ret_type == "char":
            return_part.append(
                "\treturn std::string(1, solution.{}({}));".format(
                    func_name, ", ".join([v[-1] for v in variables])
                )
            )
        elif ret_type == "void":
            return_part.append(
                "\tsolution.{}({});\n\treturn {};".format(
                    func_name, ", ".join([v[-1] for v in variables]), if_modify_in_place or variables[0][1]
                )
            )
        else:
            return_part.append(
                "\treturn solution.{}({});".format(
                    func_name, ", ".join([v[-1] for v in variables])
                )
            )

    @staticmethod
    def _simplify_variable_type(variable: list[str]) -> str:
        logging.debug("Simplifying variable type: \"%s\"", variable)
        if len(variable) > 2:
            return " ".join(variable[:-1])
        return variable[0] if not variable[0].endswith("&") and not variable[0].endswith("*") else variable[0][:-1]
