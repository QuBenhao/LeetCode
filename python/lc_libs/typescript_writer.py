import os.path
from collections import defaultdict, deque
from typing import Tuple

from python.constants import SOLUTION_TEMPLATE_TYPESCRIPT
from python.lc_libs.language_writer import LanguageWriter


class TypescriptWriter(LanguageWriter):
    def __init__(self) -> None:
        super().__init__()
        self.solution_file = "solution.ts"
        self.main_folder = "typescript"
        self.test_file = "test.ts"
        self.tests_file = "problems.test.ts"
        self._LIST_NODE_PATH = "\"../../typescript/models/listnode\";"
        self._TREE_NODE_PATH = "\"../../typescript/models/treenode\";"
        self.lang_env_commands = [["npm", "--version"]]
        self.test_commands = [["npm", "test", "--alwaysStrict", "--strictBindCallApply",
                               "--strictFunctionTypes", "--target ES202",
                               str(os.path.join(self.main_folder, self.test_file))]]

    def change_test(self, root_path, problem_folder: str, question_id: str):
        test_file_path = os.path.join(root_path, self.main_folder, self.test_file)
        with open(test_file_path, 'r', encoding="utf-8") as f:
            content = f.read()
        with open(test_file_path, 'w', encoding="utf-8") as f:
            lines = content.split("\n")
            for line_idx, line in enumerate(lines):
                if "const PROBLEM_ID: string = \"" in line:
                    f.write(line.split("\"")[0] + f"\"{question_id}\";\n")
                    continue
                elif ("let problemFolder: string = (process.env.PROBLEM_FOLDER && process.env.PROBLEM_FOLDER.length > "
                      "0) ? process.env.PROBLEM_FOLDER : \"") in line:
                    f.write(line.split("\"")[0] + f"\"{problem_folder}\";\n")
                    continue
                if line_idx < len(lines) - 1 or line:
                    f.write(line + "\n")

    def change_tests(self, root_path, problem_ids_folders: list):
        tests_file_path = os.path.join(root_path, self.main_folder, self.tests_file)
        with open(tests_file_path, 'r', encoding="utf-8") as f:
            content = f.read()
        with open(tests_file_path, 'w', encoding="utf-8") as f:
            lines = content.split("\n")
            for line_idx, line in enumerate(lines):
                if "const PROBLEMS: string[][] = " in line:
                    f.write("const PROBLEMS: string[][] = {};\n".format(str(problem_ids_folders)))
                    continue
                if line_idx < len(lines) - 1 or line:
                    f.write(line + "\n")

    def write_solution(self, code_default: str, code: str = None, problem_id: str = "",
                       problem_folder: str = "") -> str:
        import_part = defaultdict(set)
        code = code if code else code_default
        comment = False
        functions = []
        for line in code_default.split("\n"):
            strip_line = line.strip()
            if strip_line.startswith("/**"):
                comment = True
                continue
            if comment:
                if strip_line.endswith("*/"):
                    comment = False
                continue
            if strip_line.startswith("function "):
                func_name = strip_line.split("(")[0].split("function ")[-1].strip()
                variables = list(map(str.strip, strip_line.split("(")[1].split(")")[0].split(",")))
                return_type = strip_line.split("{")[0].split(")")[-1].split(":")[-1].strip()
                functions.append((func_name, variables, return_type))

        if len(functions) == 1:
            process_inputs = []
            var_names = []
            func = functions[0]
            for i, variable in enumerate(func[1]):
                var_name = variable.split(":")[0]
                var_names.append(var_name)
                var_type = variable.split(":")[-1].strip()
                match var_type:
                    case "ListNode | null":
                        import_part[self._LIST_NODE_PATH].add("ListNode")
                        import_part[self._LIST_NODE_PATH].add("IntArrayToLinkedList")
                        process_inputs.append(f"const {variable} = IntArrayToLinkedList(JSON.parse(inputValues[{i}]));")
                    case "TreeNode | null":
                        import_part[self._TREE_NODE_PATH].add("TreeNode")
                        import_part[self._TREE_NODE_PATH].add("JSONArrayToTreeNode")
                        process_inputs.append(f"const {variable} = JSONArrayToTreeNode(JSON.parse(inputValues[{i}]));")
                    case "Array<ListNode | null>":
                        import_part[self._LIST_NODE_PATH].add("ListNode")
                        import_part[self._LIST_NODE_PATH].add("IntArrayToLinkedList")
                        process_inputs.append(f"const jsonArray{i}: any = JSON.parse(inputValues[{i}]);")
                        process_inputs.append(f"const {variable} = [];")
                        process_inputs.append(f"for (let i = 0; i < jsonArray{i}.length; i++) {{")
                        process_inputs.append(f"\t{var_name}.push(IntArrayToLinkedList(jsonArray{i}[i]));")
                        process_inputs.append("}")
                    case "Array<TreeNode | null>":
                        import_part[self._TREE_NODE_PATH].add("TreeNode")
                        import_part[self._TREE_NODE_PATH].add("JSONArrayToTreeNodeArray")
                        process_inputs.append(
                            f"const {variable} = JSONArrayToTreeNodeArray(JSON.parse(inputValues[{i}]));")
                    case _:
                        process_inputs.append(f"const {variable} = JSON.parse(inputValues[{i}]);")
            match func[2]:
                case "ListNode | null":
                    import_part[self._LIST_NODE_PATH].add("ListNode")
                    import_part[self._LIST_NODE_PATH].add("LinkedListToIntArray")
                    return_part = "LinkedListToIntArray({}({}))".format(func[0], ", ".join(var_names))
                case "TreeNode | null":
                    import_part[self._TREE_NODE_PATH].add("TreeNode")
                    import_part[self._TREE_NODE_PATH].add("TreeNodeToJSONArray")
                    return_part = "TreeNodeToJSONArray({}({}))".format(func[0], ", ".join(var_names))
                case "void":
                    process_inputs.append("{}({})".format(func[0], ", ".join(var_names)))
                    return_part = ", ".join(var_names)
                case _:
                    return_part = "{}({})".format(func[0], ", ".join(var_names))
            return SOLUTION_TEMPLATE_TYPESCRIPT.format(
                "" if not import_part else "\n".join(
                    ["import {" + ",".join(v) + "} from " + k for k, v in import_part.items()]) + "\n\n",
                code,
                "\t" + "\n\t".join(process_inputs),
                return_part)
        process_inputs = ["const operators: string[] = JSON.parse(inputValues[0]);",
                          "const opValues: any[][] = JSON.parse(inputValues[1]);",
                          "const ans: any[] = [null];"]
        stack = []
        class_name = ""
        comment = False
        class_methods = defaultdict(list)
        for line in code_default.split("\n"):
            strip_line = line.strip()
            if strip_line.startswith("/**"):
                comment = True
                continue
            if comment:
                if strip_line.endswith("*/"):
                    comment = False
                continue
            if strip_line.startswith("class ") and strip_line.endswith("{"):
                stack.append(0)
                class_name = strip_line.split("{")[0].split("class ")[-1].strip()
                continue
            if "{" in line:
                stack.append(0)
            elif "}" in line:
                stack.pop()
            if len(stack) == 2 and "(" in strip_line:
                func_name = strip_line.split("(")[0].strip()
                return_type = strip_line.split("{")[0].split(")")[-1].split(":")[-1].strip()
                variables = [s for s in map(str.strip, strip_line.split("(")[1].split(")")[0].split(",")) if s != ""]
                if func_name == "constructor" and return_type == "":
                    process_inputs.append("const obj: {} = new {}({});".format(
                        class_name,
                        class_name,
                        ", ".join("opValues[0][{}]".format(i) for i in range(len(variables)))
                    ))
                else:
                    class_methods[class_name].append((func_name, variables, return_type))
        for cs, methods in class_methods.items():
            process_inputs.append("for (let i: number = 1; i < operators.length; i++) {")
            for func_name, variables, return_type in methods:
                process_inputs.append(f"\tif (operators[i] == \"{func_name}\")" + " {")
                if return_type != "" and return_type != "void":
                    process_inputs.append("\t\tans.push(obj.{}({}));".format(
                        func_name,
                        ", ".join("opValues[i][{}]".format(i) for i in range(len(variables)))))
                else:
                    process_inputs.append("\t\tobj.{}({});".format(func_name,
                                                                   ", ".join("opValues[i][{}]".format(i) for i in
                                                                             range(len(variables)))))
                    process_inputs.append("\t\tans.push(null);")
                process_inputs.append("\t\tcontinue;")
                process_inputs.append("\t}")
            process_inputs.append("\tans.push(null);")
            process_inputs.append("}")

        return SOLUTION_TEMPLATE_TYPESCRIPT.format(
            "" if not import_part else "\n".join(
                ["import {" + ",".join(v) + "} from " + k for k, v in import_part.items()]) + "\n\n",
            code,
            "\t" + "\n\t".join(process_inputs),
            "ans"
        )

    def get_solution_code(self, root_path, problem_folder: str, problem_id: str) -> Tuple[str, str]:
        if not problem_id:
            with open(os.path.join(root_path, "typescript", "test.ts"), 'r', encoding="utf-8") as f:
                lines = f.read().split("\n")
                for line in lines:
                    if "const PROBLEM_ID: string = \"" in line:
                        problem_id = line.split('"')[1]
                        break
        if not problem_id:
            return "", problem_id
        file_path = os.path.join(root_path, problem_folder, f"{problem_folder}_{problem_id}", "solution.ts")
        if not os.path.exists(file_path):
            return "", problem_id
        final_codes = deque([])
        with open(file_path, 'r', encoding="utf-8") as f:
            lines = f.read().split("\n")
            for line in lines:
                strip_line = line.strip()
                if strip_line.startswith("import "):
                    continue
                if strip_line == "export function Solve(inputJsonElement: string): any {":
                    break
                final_codes.append(line)
        while final_codes and final_codes[0].strip() == '':
            final_codes.popleft()
        while final_codes and final_codes[-1].strip() == '':
            final_codes.pop()
        return "\n".join(final_codes), problem_id
