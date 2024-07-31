import logging
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
        self._NODE_NEXT_PATH = "\"../../typescript/models/node.next\";"
        self._NODE_NEIGHBORS_PATH = "\"../../typescript/models/node.neighbors\";"
        self._NODE_RANDOM_PATH = "\"../../typescript/models/node.random\";"
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
        testcases = LanguageWriter.get_test_cases(problem_folder, problem_id)
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
            self._process_variables(func, process_inputs, var_names, import_part, code_default, testcases)
            return_part = self._process_return(func, process_inputs, var_names, import_part, code_default)
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

    def _process_variables(self, func, process_inputs, var_names, import_part, code_default: str, testcases=None):
        i = 0
        while i < len(func[1]):
            variable = func[1][i]
            var_name = variable.split(":")[0]
            var_names.append(var_name)
            var_type = variable.split(":")[-1].strip()
            match var_type:
                case "ListNode | null":
                    if testcases:
                        if len(testcases[0]) == len(func[1]) + 1 and all(
                                isinstance(testcase[0], list)
                                and isinstance(testcase[1], int)
                                for testcase in testcases):
                            import_part[self._LIST_NODE_PATH].add("ListNode")
                            import_part[self._LIST_NODE_PATH].add("IntArrayToLinkedListWithCycle")
                            process_inputs.append("const inputArray: number[] = JSON.parse(inputValues[0]);")
                            process_inputs.append("const cyclePos: number = JSON.parse(inputValues[1]);")
                            process_inputs.append(f"const {variable} ="
                                                  f" IntArrayToLinkedListWithCycle(inputArray, cyclePos);")
                            i += 2
                            continue
                        elif (len(func[1]) == 2 and len(testcases[0]) == 5
                              and all(isinstance(testcase[0], int) and isinstance(testcase[1], list) and
                                      isinstance(testcase[2], list) and isinstance(testcase[3], int) and
                                      isinstance(testcase[4], int) for testcase in testcases)):
                            import_part[self._LIST_NODE_PATH].add("ListNode")
                            import_part[self._LIST_NODE_PATH].add("IntArrayToIntersectionLinkedList")
                            process_inputs.append("const iv: number = JSON.parse(inputValues[0]);")
                            process_inputs.append("const inputArray1: number[] = JSON.parse(inputValues[1]);")
                            process_inputs.append("const inputArray2: number[] = JSON.parse(inputValues[2]);")
                            process_inputs.append("const skipA: number = JSON.parse(inputValues[3]);")
                            process_inputs.append("const skipB: number = JSON.parse(inputValues[4]);")
                            next_var_name = func[1][i + 1].split(":")[0]
                            process_inputs.append(f"const [{var_name}, {next_var_name}] = "
                                                  "IntArrayToIntersectionLinkedList("
                                                  "iv, inputArray1, inputArray2, skipA, skipB);")
                            var_names.append(next_var_name)
                            i += 5
                            continue
                        elif len(func[1]) != len(testcases[0]):
                            logging.debug(f"Testcases: {testcases}, variables: {func[1]}")
                    import_part[self._LIST_NODE_PATH].add("ListNode")
                    import_part[self._LIST_NODE_PATH].add("IntArrayToLinkedList")
                    process_inputs.append(f"const {variable} = IntArrayToLinkedList(JSON.parse(inputValues[{i}]));")
                case "TreeNode | null":
                    if testcases:
                        if len(func[1]) == len(testcases[0]) + 1:
                            import_part[self._TREE_NODE_PATH].add("TreeNode")
                            import_part[self._TREE_NODE_PATH].add("JSONArrayToTreeNode")
                            import_part[self._TREE_NODE_PATH].add("JsonArrayToTreeNodeWithTargets")
                            process_inputs.append("const targetVal: number = JSON.parse(inputValues[1]);")
                            process_inputs.append("const nodes: Array<TreeNode | null> = JsonArrayToTreeNodeWithTargets"
                                                  "(JSON.parse(inputValues[0]), targetVal);")
                            process_inputs.append(f"const {var_name}: TreeNode = nodes[0],"
                                                  " target: TreeNode = nodes[1];")
                            process_inputs.append("const cloned: TreeNode = "
                                                  "JSONArrayToTreeNode(JSON.parse(inputValues[0]));")
                            var_names.append("cloned")
                            var_names.append("target")
                            i += 3
                            continue
                        idx = i + 1
                        while all(idx < len(testcase)
                                  and "TreeNode | null" == func[1][idx].split(":")[-1].strip()
                                  and testcase[idx] is not None
                                  and not isinstance(testcase[idx], list) for testcase in testcases):
                            idx += 1
                        if idx != i + 1:
                            import_part[self._TREE_NODE_PATH].add("TreeNode")
                            import_part[self._TREE_NODE_PATH].add("JsonArrayToTreeNodeWithTargets")
                            for j in range(i + 1, idx):
                                process_inputs.append(f"const targetVal{j}: number = JSON.parse(inputValues[{j}]);")
                                var_names.append(func[1][j].split(":")[0])
                            process_inputs.append(
                                f"const nodes: Array<TreeNode | null> = "
                                f"JsonArrayToTreeNodeWithTargets(JSON.parse(inputValues[{i}]), "
                                + ", ".join([f"targetVal{j}" for j in range(i + 1, idx)]) + ");")
                            process_inputs.append(
                                f"const {var_name}: TreeNode = nodes[0], "
                                + ", ".join([f"{var_names[j - i]}: TreeNode = nodes[{j - i}]"
                                             for j in range(i + 1, idx)]) + ";")
                            i = idx
                            continue
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
                case "_Node | null":
                    if "left: _Node | null" in code_default and "right: _Node | null" in code_default and \
                            "next: _Node | null" in code_default:
                        import_part[self._NODE_NEXT_PATH].add("NodeNext as _Node")
                        import_part[self._NODE_NEXT_PATH].add("JSONArrayToTreeNodeNext")
                        process_inputs.append(
                            f"const {variable} = JSONArrayToTreeNodeNext(JSON.parse(inputValues[{i}]));")
                    elif "neighbors: _Node[]" in code_default:
                        import_part[self._NODE_NEIGHBORS_PATH].add("NodeNeighbors as _Node")
                        import_part[self._NODE_NEIGHBORS_PATH].add("JsonArrayToNodeNeighbors")
                        process_inputs.append(
                            f"const intArray{i}: Array<Array<number>> = JSON.parse(inputValues[{i}]);")
                        process_inputs.append(f"const {variable} = JsonArrayToNodeNeighbors(intArray{i});")
                    elif "next: _Node | null" in code_default:
                        import_part[self._NODE_RANDOM_PATH].add("NodeRandom as _Node")
                        import_part[self._NODE_RANDOM_PATH].add("JSONArrayToNodeRandom")
                        process_inputs.append(
                            f"const {variable} = JSONArrayToNodeRandom(JSON.parse(inputValues[{i}]));")
                    else:
                        logging.debug(f"Please implement the conversion function for _Node, {code_default}")
                        process_inputs.append(f"const {variable} = JSON.parse(inputValues[{i}]);")
                case _:
                    process_inputs.append(f"const {variable} = JSON.parse(inputValues[{i}]);")
            i += 1

    def _process_return(self, func, process_inputs, var_names, import_part, code_default: str) -> str:
        match func[2]:
            case "ListNode | null":
                import_part[self._LIST_NODE_PATH].add("ListNode")
                import_part[self._LIST_NODE_PATH].add("LinkedListToIntArray")
                return_part = "LinkedListToIntArray({}({}))".format(func[0], ", ".join(var_names))
            case "TreeNode | null":
                import_part[self._TREE_NODE_PATH].add("TreeNode")
                import_part[self._TREE_NODE_PATH].add("TreeNodeToJSONArray")
                return_part = "TreeNodeToJSONArray({}({}))".format(func[0], ", ".join(var_names))
            case "_Node | null":
                if "left: _Node | null" in code_default and "right: _Node | null" in code_default and \
                        "next: _Node | null" in code_default:
                    import_part[self._NODE_NEXT_PATH].add("NodeNext as _Node")
                    import_part[self._NODE_NEXT_PATH].add("TreeNodeNextToJSONArray")
                    return_part = "TreeNodeNextToJSONArray({}({}))".format(func[0], ", ".join(var_names))
                elif "neighbors: _Node[]" in code_default:
                    import_part[self._NODE_NEIGHBORS_PATH].add("NodeNeighbors as _Node")
                    import_part[self._NODE_NEIGHBORS_PATH].add("NodeNeighborsToJsonArray")
                    return_part = "NodeNeighborsToJsonArray({}({}))".format(func[0], ", ".join(var_names))
                elif "next: _Node | null" in code_default:
                    import_part[self._NODE_RANDOM_PATH].add("NodeRandom as _Node")
                    import_part[self._NODE_RANDOM_PATH].add("NodeRandomToJSONArray")
                    return_part = "NodeRandomToJSONArray({}({}))".format(func[0], ", ".join(var_names))
                else:
                    return_part = "{}({})".format(func[0], ", ".join(var_names))
                    logging.debug(f"Please implement the return part for _Node, {code_default}")
            case "void":
                process_inputs.append("{}({})".format(func[0], ", ".join(var_names)))
                return_part = ", ".join(var_names)
            case _:
                return_part = "{}({})".format(func[0], ", ".join(var_names))
        return return_part
