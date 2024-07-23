import os.path
from collections import deque, defaultdict
from typing import Tuple

from python.constants import SOLUTION_TEMPLATE_JAVA
from python.lc_libs.language_writer import LanguageWriter


class JavaWriter(LanguageWriter):
    def __init__(self) -> None:
        super().__init__()
        self.solution_file = "Solution.java"
        self.main_folder = "qubhjava/test"
        self.test_file = "TestMain.java"
        self.tests_file = "ProblemsTest.java"
        self.lang_env_commands = [["mvn", "-v"]]
        self.test_commands = [["mvn", "test", "-Dtest=qubhjava.test.TestMain"]]

    def change_test(self, root_path, problem_folder: str, question_id: str):
        test_file_path = os.path.join(root_path, self.main_folder, self.test_file)
        with open(test_file_path, 'r', encoding="utf-8") as f:
            content = f.read()
        with open(test_file_path, 'w', encoding="utf-8") as f:
            appear_problem_folder = False
            lines = content.split("\n")
            for line_idx, line in enumerate(lines):
                if "private static final String PROBLEM_ID = " in line:
                    f.write(line.split("\"")[0] + f"\"{question_id}\";\n")
                    continue
                elif f"import {problem_folder}.{problem_folder}_" in line and ".Solution;" in line:
                    f.write(f"import {problem_folder}.{problem_folder}_{question_id}.Solution;\n")
                    appear_problem_folder = True
                    continue
                elif "import " in line and ".Solution;" in line and not line.startswith("//"):
                    f.write(f"// {line}\n")
                    continue
                elif line.strip() == "import qubhjava.Testcase;" and not appear_problem_folder:
                    f.write(f"import {problem_folder}.{problem_folder}_{question_id}.Solution;\n")
                    appear_problem_folder = True
                if line_idx < len(lines) - 1 or line:
                    f.write(line + "\n")

    def change_tests(self, root_path, problem_ids_folders: list):
        tests_file_path = os.path.join(root_path, self.main_folder, self.tests_file)
        with open(tests_file_path, 'r', encoding="utf-8") as f:
            content = f.read()
        with open(tests_file_path, 'w', encoding="utf-8") as f:
            lines = content.split("\n")
            for line_idx, line in enumerate(lines):
                if "private static final String[][] PROBLEMS = " in line:
                    f.write("\tprivate static final String[][] PROBLEMS = {" +
                            ", ".join(f"{{\"{pid}\", \"{pf}\"}}" for pid, pf in problem_ids_folders) + "};\n")
                    continue
                if line_idx < len(lines) - 1 or line:
                    f.write(line + "\n")

    def write_solution(self, code_default: str, code: str = None, problem_id: str = "",
                       problem_folder: str = "") -> str:
        import_packages = []
        body = []
        parse_input = []
        return_part = ""
        import_part = True
        variables = []
        code = code if code else code_default
        if "object will be instantiated and called as such:" in code:
            return_part = "ans"
            parse_input.append("String[] operators = jsonArrayToStringArray(inputJsonValues[0]);")
            parse_input.append("String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);")
            class_name = ""
            all_return_parts = []
            func_parse_input = defaultdict(list)
            for line in code.split("\n"):
                strip_line = line.strip()
                if (strip_line.startswith("class ") or strip_line.startswith("public class")) and strip_line.endswith(
                        "{"):
                    class_name = strip_line.split("{")[0].split("class ")[-1].strip()
                elif strip_line.startswith("public ") and strip_line.endswith("{"):
                    vs, pi, ai, rp, func_name, rt = JavaWriter.__parse_java_method(strip_line)
                    variables.extend(vs)
                    import_packages.extend(ai)
                    if func_name == class_name:
                        parse_input.extend([p.replace("inputJsonValues", "opValues[0]") for p in pi])
                        parse_input.append(f"{class_name} obj = new {rp};")
                    else:
                        func_parse_input[func_name].extend(
                            ["\t\t" + p.replace("inputJsonValues", "opValues[i]") for p in pi])
                        all_return_parts.append((func_name, rt, rp))
            import_packages.append("")
            import_packages.append("")
            import_packages.extend(code.split("\n"))
            parse_input.append("List<Object> ans = new ArrayList<>(operators.length);")
            parse_input.append("ans.add(null);")
            parse_input.append("for (int i = 1; i < operators.length; i++) {")
            for func_name, rt, rp in all_return_parts:
                parse_input.append("\tif (operators[i].compareTo(\"" + func_name + "\") == 0) {")
                if rt == "void":
                    parse_input.extend(func_parse_input[func_name][:-1])
                    parse_input.append(f"\t\tobj.{func_name}({rp});")
                    parse_input.append(f"\t\tans.add(null);")
                else:
                    parse_input.extend(func_parse_input[func_name])
                    parse_input.append(f"\t\tans.add(obj.{rp});")
                parse_input.append("\t\tcontinue;")
                parse_input.append("\t}")
            parse_input.append("\tans.add(null);")
            parse_input.append("}")
        else:
            for line in code_default.split("\n"):
                if "class Solution {" in line:
                    import_part = False
                    continue
                if import_part:
                    import_packages.append(line)
                else:
                    if line == "}":
                        continue
                    strip_line = line.strip()
                    additional_import = set()
                    if strip_line.startswith("public ") and strip_line.endswith("{"):
                        vs, pi, ai, rp, _, _ = JavaWriter.__parse_java_method(strip_line)
                        variables.extend(vs)
                        parse_input.extend(pi)
                        additional_import.update(ai)
                        return_part = rp
                    import_packages.extend(additional_import)
            import_part = True
            for line in code.split("\n"):
                if "class Solution {" in line:
                    import_part = False
                    continue
                if not import_part:
                    if line == "}":
                        continue
                    body.append(line)
        return SOLUTION_TEMPLATE_JAVA.format(
            problem_folder,
            problem_folder,
            problem_id,
            "\n".join(import_packages),
            "\n".join(body),
            "\n\t\t".join(parse_input),
            return_part,
        )

    def get_solution_code(self, root_path, problem_folder: str, problem_id: str) -> Tuple[str, str]:
        if not problem_id:
            with open(os.path.join(root_path, self.main_folder, self.test_file), 'r', encoding="utf-8") as f:
                lines = f.read().split("\n")
                for line in lines:
                    if "private static final String PROBLEM_ID = \"" in line:
                        problem_id = line.split('"')[1]
                        break
        if not problem_id:
            return "", problem_id
        file_path = os.path.join(root_path, problem_folder, f"{problem_folder}_{problem_id}", self.solution_file)
        if not os.path.exists(file_path):
            return "", problem_id
        final_codes = deque([])
        with open(file_path, 'r', encoding="utf-8") as f:
            content = f.read()
            is_obj_question = False
            if "object will be instantiated and called as such:" in content:
                is_obj_question = True
            lines = content.split("\n")
            solve_part = []
            for line in lines:
                if line.startswith("package "):
                    continue
                if line.startswith("import "):
                    continue
                if "public Object solve(String[] values) {" in line or \
                        "public Object solve(String[] inputJsonValues) {" in line:
                    last = final_codes.pop()
                    if last.strip() != "@Override":
                        final_codes.append(last)
                    solve_part.append(0)
                    continue
                if solve_part:
                    for _ in range(line.count("{")):
                        solve_part.append(0)
                    for _ in range(line.count("}")):
                        solve_part.pop()
                    continue
                if "public class Solution extends BaseSolution {" in line:
                    if not is_obj_question:
                        final_codes.append("class Solution {")
                    continue
                final_codes.append(line)
        while final_codes and final_codes[0].strip() == '':
            final_codes.popleft()

        if is_obj_question:
            while final_codes and final_codes[-1].strip() == '':
                final_codes.pop()
            if final_codes and final_codes[-1].strip() == "}":
                final_codes.pop()
            while final_codes and final_codes[-1].strip() == '':
                final_codes.pop()
        return "\n".join(final_codes), problem_id

    @staticmethod
    def __process_variable_type(input_name: str, variable_name: str, rt_type: str) -> str:
        match rt_type:
            case "int":
                return f"{rt_type} {variable_name} = Integer.parseInt({input_name});"
            case "float":
                return f"{rt_type} {variable_name} = Float.parseFloat({input_name});"
            case "double":
                return f"{rt_type} {variable_name} = Double.parseDouble({input_name});"
            case "int[]":
                return f"{rt_type} {variable_name} = jsonArrayToIntArray({input_name});"
            case "String":
                return f"{rt_type} {variable_name} = jsonStringToString({input_name});"
            case "String[]":
                return f"{rt_type} {variable_name} = jsonArrayToStringArray({input_name});"
            case "String[][]":
                return f"{rt_type} {variable_name} = jsonArrayToString2DArray({input_name});"
            case "int[][]":
                return f"{rt_type} {variable_name} = jsonArrayToInt2DArray({input_name});"
            case "List<Integer>":
                return f"{rt_type} {variable_name} = jsonArrayToIntList({input_name});"
            case "ListNode":
                return f"{rt_type} {variable_name} = jsonArrayToListNode({input_name});"
            case "ListNode[]":
                return f"{rt_type} {variable_name} = jsonArrayToListNodeArray({input_name});"
            case "TreeNode":
                return f"{rt_type} {variable_name} = TreeNode.ArrayToTreeNode({input_name});"
            case "TreeNode[]":
                return f"{rt_type} {variable_name} = jsonArrayToTreeNodeArray({input_name});"
            case "List<TreeNode>":
                return f"{rt_type} {variable_name} = jsonArrayToTreeNodeList({input_name});"
            case "char[]":
                return f"{rt_type} {variable_name} = jsonArrayToCharArray({input_name});"
            case "char[][]":
                return f"{rt_type} {variable_name} = jsonArrayToChar2DArray({input_name});"
            case "List<String>":
                return f"{rt_type} {variable_name} = jsonArrayToStringList({input_name});"
            case "List<List<String>>":
                return f"{rt_type} {variable_name} = jsonArrayToString2DList({input_name});"
            case "char":
                return (f"{rt_type} {variable_name} = {input_name}.length() > 1 ?"
                        f" {input_name}.charAt(1) : {input_name}.charAt(0);")
            case "":
                return ""
            case _:
                print("Java type not Implemented yet: {}".format(rt_type))
        return f"{rt_type} {variable_name} = FIXME({input_name})"

    @staticmethod
    def __parse_java_method(strip_line: str):
        variables = []
        parse_input = []
        additional_import = set()
        return_func = strip_line.split("(")[0].split(" ")[-1]
        return_type = strip_line.split("(")[0].split(" ")[1]
        input_parts = strip_line.split("(")[1].split(")")[0].strip().split(",")
        last = ""
        for i, input_part in enumerate(input_parts):
            var_split = input_part.strip().split(" ")
            if len(var_split) < 2:
                rt_type, variable = last, var_split[0]
            else:
                rt_type, variable = var_split[0], var_split[1]
                last = rt_type
            variables.append(variable)
            parse_input.append(JavaWriter.__process_variable_type(f"inputJsonValues[{i}]", variable, rt_type))
            if "ListNode" in rt_type:
                additional_import.add("import qubhjava.models.ListNode;")
            elif "TreeNode" in rt_type:
                additional_import.add("import qubhjava.models.TreeNode;")
        if "ListNode" in return_type:
            additional_import.add("import qubhjava.models.ListNode;")
            return_part = "ListNode.LinkedListToIntArray({}({}))".format(return_func, ", ".join(variables))
        elif "TreeNode" in return_type:
            additional_import.add("import qubhjava.models.TreeNode;")
            return_part = "TreeNode.TreeNodeToArray({}({}))".format(return_func, ", ".join(variables))
        elif return_type == "void":
            parse_input.append("{}({});".format(return_func, ", ".join(variables)))
            return_part = ", ".join(variables)
        else:
            return_part = "{}({})".format(return_func, ", ".join(variables))
        return variables, parse_input, additional_import, return_part, return_func, return_type
