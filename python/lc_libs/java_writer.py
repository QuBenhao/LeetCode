import logging
import os
from collections import deque, defaultdict
import re
from pathlib import Path
from typing import List, Optional, Tuple

from python.constants import SOLUTION_TEMPLATE_JAVA
from python.lc_libs.language_writer import LanguageWriter


class JavaWriter(LanguageWriter):
    def __init__(self) -> None:
        super().__init__()
        self.solution_file = "Solution.java"
        self.main_folder = "qubhjava/test"
        mvn_exec = "mvn.cmd" if os.name == "nt" else "mvn"
        self.lang_env_commands = [[mvn_exec, "-v"]]
        self.test_commands = [[mvn_exec, "test", "-Dtest=qubhjava.test.TestMain"]]

    def write_solution(self, code_default: str, code: str = None, problem_id: str = "",
                       problem_folder: str = "") -> str:
        import_packages = []
        body = []
        parse_input = []
        end_extra = []
        return_part = ""
        import_part = True
        variables = []
        code = code or code_default
        testcases = LanguageWriter.get_test_cases(problem_folder, problem_id)
        if "object will be instantiated and called as such:" in code:
            return_part = "ans"
            parse_input.append("String[] operators = jsonArrayToStringArray(inputJsonValues[0]);")
            parse_input.append("String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);")
            class_name = ""
            all_return_parts = []
            func_parse_input = defaultdict(list)
            tmp_additional_import = set()
            for line in code.split("\n"):
                strip_line = line.strip()
                if (strip_line.startswith("class ") or strip_line.startswith("public class")) and strip_line.endswith(
                        "{"):
                    class_name = strip_line.split("{")[0].split("class ")[-1].strip()
                elif strip_line.startswith("public ") and strip_line.endswith("{"):
                    vs, pi, ai, rp, func_name, rt = JavaWriter.__parse_java_method(strip_line, code_default,
                                                                                   is_object_problem=True)
                    variables.extend(vs)
                    tmp_additional_import.update(ai)
                    if func_name == class_name:
                        parse_input.extend([p.replace("inputJsonValues", "opValues[0]") for p in pi])
                        parse_input.append(f"{class_name} obj = new {rp};")
                    else:
                        func_parse_input[func_name].extend(
                            ["\t\t" + p.replace("inputJsonValues", "opValues[i]") for p in pi])
                        all_return_parts.append((func_name, rt, rp))
            import_packages.extend(tmp_additional_import)
            import_packages.append("")
            import_packages.append("")
            import_packages.extend(code.split("\n"))
            parse_input.append("List<Object> ans = new ArrayList<>(operators.length);")
            parse_input.append("ans.add(null);")
            parse_input.append("for (int i = 1; i < operators.length; i++) {")
            logging.debug("all_return_parts: %s", all_return_parts)
            for func_name, rt, rp in all_return_parts:
                parse_input.append("\tif (operators[i].compareTo(\"" + func_name + "\") == 0) {")
                if rt == "void":
                    parse_input.extend(func_parse_input[func_name][:-1])
                    parse_input.append(f"\t\tobj.{func_name}({rp});")
                    parse_input.append(f"\t\tans.add(null);")
                elif "TreeNode" in rt:
                    parse_input.extend(func_parse_input[func_name])
                    rp = rp.replace("TreeNode.TreeNodeToArray(", "TreeNode.TreeNodeToArray(obj.")
                    parse_input.append(f"\t\tans.add({rp});")
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
                        vs, pi, ai, rp, _, _ = JavaWriter.__parse_java_method(strip_line, code_default, testcases, end_extra=end_extra)
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
            "\n\n" + "\n".join(end_extra) if end_extra else "",
        )

    def get_solution_code(self, root_path: Path, problem_folder: str, problem_id: str) -> Tuple[str, str]:
        if not problem_id:
            problem_id = self.get_test_problem_id(root_path, problem_folder)
        if not problem_id:
            return "", problem_id
        file_path = root_path / problem_folder / f"{problem_folder}_{problem_id}" / self.solution_file
        if not file_path.exists():
            return "", problem_id
        final_codes = deque([])
        with file_path.open('r', encoding="utf-8") as f:
            content = f.read()
            solution_class_idx = content.find("public class Solution extends BaseSolution {")
            logging.debug("solution_class_idx: %s", solution_class_idx)
            solve_method_idx = content.find("public Object solve(String[] ", solution_class_idx)
            logging.debug("solve_method_idx: %s", solve_method_idx)
            # if there are any method in between, add them to final_codes
            between_content = content[solution_class_idx + len("public class Solution extends BaseSolution {"):solve_method_idx]
            if between_content.strip() != "@Override":
                splits = between_content.split("\n")
                while splits and splits[-1].strip() != "@Override":
                    splits.pop()
                splits.pop()
                logging.debug(splits)
                final_codes.extend(splits)
                while final_codes and not final_codes[-1].strip():
                    final_codes.pop()
                while final_codes and not final_codes[0].strip():
                    final_codes.popleft()
                final_codes.appendleft("class Solution {")
                final_codes.append("}")
            else:
                # last import sentence
                last_import_idx = content.rfind("import ")
                start_idx = content.find("\n", last_import_idx) + 1
                final_codes.extend(content[start_idx:solution_class_idx].split("\n"))
                while final_codes and not final_codes[-1].strip():
                    final_codes.pop()
                while final_codes and not final_codes[0].strip():
                    final_codes.popleft()
        return "\n".join(final_codes), problem_id

    @staticmethod
    def __process_variable_type(input_name: str, variable_name: str, rt_type: str, code_default: str, end_extra:Optional[List]=None) -> str:
        match rt_type:
            case "int":
                return f"{rt_type} {variable_name} = Integer.parseInt({input_name});"
            case "float":
                return f"{rt_type} {variable_name} = Float.parseFloat({input_name});"
            case "double":
                return f"{rt_type} {variable_name} = Double.parseDouble({input_name});"
            case "double[]":
                return f"{rt_type} {variable_name} = jsonArrayToDoubleArray({input_name});"
            case "long":
                return f"{rt_type} {variable_name} = Long.parseLong({input_name});"
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
            case "boolean[]":
                return f"{rt_type} {variable_name} = jsonArrayToBooleanArray({input_name});"
            case "List<Integer>":
                return f"{rt_type} {variable_name} = jsonArrayToIntList({input_name});"
            case "List<List<Integer>>":
                return f"{rt_type} {variable_name} = jsonArrayTo2DIntList({input_name});"
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
            case "Node":
                if "Node left;" in code_default and "Node right;" in code_default and "Node next;" in code_default:
                    return f"{rt_type} {variable_name} = Node.ArrayToTreeNodeNext({input_name});"
                elif "List<Node> neighbors;" in code_default:
                    return (f"{rt_type} {variable_name} ="
                            f" Node.ArrayToNodeNeighbors(jsonArrayToInt2DArray({input_name}));")
                elif "Node random;" in code_default:
                    return f"{rt_type} {variable_name} = Node.JsonArrayToNodeRandom({input_name});"
                logging.debug(f"Node type not implemented yet, variable_name: {variable_name},"
                              f" rt_type: {rt_type}, code: [{code_default}]")
            case "":
                logging.debug(f"Empty Java type, variable_name: {variable_name},"
                              f" rt_type: {rt_type}, code: [{code_default}]")
                return ""
            case _:
                mit = re.finditer(r"// Definition for (\w+).", code_default)
                for m in mit:
                    if m.group(1) in rt_type:
                        class_name = m.group(1)
                        logging.debug("Match custom Class at %d-%d, Class [%s]", m.start(), m.end(), class_name)
                        start_index = m.start()
                        end_index = code_default.find("*/")
                        logging.debug("Add extra class code:\n%s", code_default[start_index:end_index])
                        end_extra.extend(code_default[start_index:end_index].split("\n"))
                        insert_pos = len(end_extra) - 1
                        while insert_pos > 0 and "}" not in end_extra[insert_pos]:
                            insert_pos -= 1
                        end_extra.insert(insert_pos, f"\tpublic static {rt_type} Constructor(String input) {{\n\t\treturn null;\n\t}}")
                        return f"{rt_type} {variable_name} = {class_name}.Constructor({input_name});"
                logging.warning("Java type not Implemented yet: {}".format(rt_type))
        return f"{rt_type} {variable_name} = FIXME({input_name})"

    @staticmethod
    def __parse_java_method(strip_line: str, code_default: str, testcases=None,
                            is_object_problem: bool = False, end_extra=None) -> Tuple:
        variables = []
        parse_input = []
        additional_import = set()
        return_func = strip_line.split("(")[0].split(" ")[-1]
        return_type = strip_line.split("(")[0].split(" ")[-2]
        input_parts = strip_line.split("(")[1].split(")")[0].strip().split(",")
        last = [""]
        i = 0
        logging.debug("input_parts: %s", input_parts)
        while i < len(input_parts):
            input_part = input_parts[i]
            var_split = input_part.strip().split(" ")
            rt_type, variable = JavaWriter._get_variable(var_split, last)
            if testcases and rt_type == "TreeNode":
                if len(input_parts) == len(testcases[0]) + 1:
                    parse_input.append("int targetVal = Integer.parseInt(inputJsonValues[1]);")
                    parse_input.append(
                        "TreeNode[] nodes = TreeNode.ArrayToTreeNodeWithTargets(inputJsonValues[0], targetVal);")
                    parse_input.append("TreeNode original = nodes[0], target = nodes[1];")
                    parse_input.append("TreeNode cloned = TreeNode.ArrayToTreeNode(inputJsonValues[0]);")
                    variables.append("original")
                    variables.append("cloned")
                    variables.append("target")
                    i += 3
                    continue
                idx = i + 1
                while all(idx < len(testcase)
                          and "TreeNode" == JavaWriter._get_variable(input_parts[idx].split(" "), last)[0]
                          and testcase[idx] is not None
                          and not isinstance(testcase[idx], list) for testcase in testcases):
                    idx += 1
                if idx != i + 1:
                    variables.append(variable)
                    for j in range(i + 1, idx):
                        parse_input.append(f"int targetVal{j} = Integer.parseInt(inputJsonValues[{j}]);")
                        variables.append(JavaWriter._get_variable(input_parts[j].split(" "), last)[1])
                    parse_input.append(
                        f"TreeNode[] nodes = TreeNode.ArrayToTreeNodeWithTargets(inputJsonValues[{i}], "
                        + ", ".join([f"targetVal{j}" for j in range(i + 1, idx)]) + ");")
                    parse_input.append(
                        f"TreeNode {JavaWriter._get_variable(input_parts[i].split(" "), last)[1]} = nodes[0], "
                        + ", ".join([f"{JavaWriter._get_variable(
                            input_parts[j].split(' '), last)[1]} = nodes[{j - i}]" for j in range(i + 1, idx)]) + ";")
                    i = idx
                    continue
            variables.append(variable)
            parse_input.append(JavaWriter.__process_variable_type(f"inputJsonValues[{i}]",
                                                                  variable, rt_type, code_default, end_extra))
            if "ListNode" in rt_type:
                if testcases:
                    if len(testcases[0]) == len(input_parts) + 1 and all(
                            isinstance(testcase[0], list)
                            and isinstance(testcase[1], int)
                            for testcase in testcases):
                        parse_input.clear()
                        parse_input.append(JavaWriter.__process_variable_type("inputJsonValues[0]", "arr", "int[]", ""))
                        parse_input.append(JavaWriter.__process_variable_type("inputJsonValues[1]", "pos", "int", ""))
                        parse_input.append("ListNode head = ListNode.IntArrayToLinkedListCycle(arr, pos);")
                        if "ListNode" in return_type:
                            parse_input.append(f"ListNode res = {return_func}({', '.join(variables)})")
                        i += 2
                        continue
                    elif (len(input_parts) == 2 and len(testcases[0]) == 5
                          and all(isinstance(testcase[0], int) and isinstance(testcase[1], list) and
                                  isinstance(testcase[2], list) and isinstance(testcase[3], int) and
                                  isinstance(testcase[4], int) for testcase in testcases)):
                        parse_input.clear()
                        parse_input.append(JavaWriter.__process_variable_type("inputJsonValues[0]", 'iv', "int", ""))
                        parse_input.append(
                            JavaWriter.__process_variable_type("inputJsonValues[1]", 'arrA', "int[]", ""))
                        parse_input.append(
                            JavaWriter.__process_variable_type("inputJsonValues[2]", 'arrB', "int[]", ""))
                        parse_input.append(JavaWriter.__process_variable_type("inputJsonValues[3]", 'skipA', "int", ""))
                        parse_input.append(JavaWriter.__process_variable_type("inputJsonValues[4]", 'skipB', "int", ""))
                        parse_input.append(
                            "ListNode[] nodes = ListNode.IntArrayToIntersectionListNode(arrA, arrB, iv, skipA, skipB);")
                        parse_input.append("ListNode headA = nodes[0], headB = nodes[1];")
                        variables.append("headB")
                        i += 5
                        continue
                    elif len(input_parts) != len(testcases[0]):
                        logging.debug(f"Testcases: {testcases}, variables: {input_parts}")
                additional_import.add("import qubhjava.models.ListNode;")
            elif "TreeNode" in rt_type:
                additional_import.add("import qubhjava.models.TreeNode;")
            i += 1
        if "ListNode" in return_type:
            if any("IntArrayToLinkedListCycle" in pi for pi in parse_input):
                return_part = "res == null ? null : res.val"
            else:
                additional_import.add("import qubhjava.models.ListNode;")
                return_part = "ListNode.LinkedListToIntArray({}({}))".format(return_func, ", ".join(variables))
        elif "TreeNode" in return_type:
            additional_import.add("import qubhjava.models.TreeNode;")
            return_part = "TreeNode.TreeNodeToArray({}({}))".format(return_func, ", ".join(variables))
        elif return_type == "void":
            parse_input.append("{}({});".format(return_func, ", ".join(variables)))
            logging.debug("Void return type, function: {}, variables: {}".format(return_func, variables))
            if not is_object_problem:
                if "ListNode" in input_parts[0]:
                    return_part = f"ListNode.LinkedListToIntArray({variables[0]})"
                elif "TreeNode" in input_parts[0]:
                    return_part = f"TreeNode.TreeNodeToArray({variables[0]})"
                else:
                    return_part = variables[0]
            else:
                return_part = ", ".join(variables)
        elif "Node" in return_type:
            if "Node left;" in code_default and "Node right;" in code_default and "Node next;" in code_default:
                additional_import.add("import qubhjava.models.node.next.Node;")
                return_part = "Node.TreeNodeNextToArray({}({}))".format(return_func, ", ".join(variables))
            elif "List<Node> neighbors;" in code_default:
                additional_import.add("import qubhjava.models.node.neighbors.Node;")
                return_part = "Node.NodeNeighborsToArray({}({}))".format(return_func, ", ".join(variables))
            elif "Node random;" in code_default:
                additional_import.add("import qubhjava.models.node.random.Node;")
                return_part = "Node.NodeRandomToJsonArray({}({}))".format(return_func, ", ".join(variables))
            else:
                return_part = "{}({})".format(return_func, ", ".join(variables))
        else:
            return_part = "{}({})".format(return_func, ", ".join(variables))
        return variables, parse_input, additional_import, return_part, return_func, return_type

    @staticmethod
    def _get_variable(var_split, last: list):
        if len(var_split) < 2:
            rt_type, variable = last[0], var_split[0]
        else:
            rt_type, variable = var_split[-2], var_split[-1]
            last[0] = rt_type
        return rt_type, variable
