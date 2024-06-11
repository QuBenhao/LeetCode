import os.path
from collections import deque

from python.constants import SOLUTION_TEMPLATE_JAVA


def change_test_java(content: str, question_id: str) -> str:
    ans = []
    for line in content.split("\n"):
        if "private static final String PROBLEM_ID = " in line:
            ans.append(line.split("\"")[0] + f"\"{question_id}\";")
            continue
        elif "import problems.problems_" in line and ".Solution;" in line:
            ans.append("import problems.problems_" + question_id + ".Solution;")
            continue
        ans.append(line)
    return "\n".join(ans)


def __process_variable_type(input_name: str, variable_name: str, rt_type: str) -> str:
    match rt_type:
        case "int":
            return f"{rt_type} {variable_name} = Integer.parseInt({input_name});"
        case "int[]":
            return f"{rt_type} {variable_name} = jsonArrayToIntArray({input_name});"
        case "String":
            return f"{rt_type} {variable_name} = {input_name};"
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
        case _:
            print("Java type not Implemented yet: {}".format(rt_type))
    return f"{rt_type} {variable_name} = FIXME({input_name})"


def write_solution_java(code_default: str, code: str = None, problem_id: str = "") -> str:
    import_packages = []
    body = []
    parse_input = []
    return_part = ""
    import_part = True
    variables = []
    code = code if code else code_default
    for line in code.split("\n"):
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
                return_func = strip_line.split("(")[0].split(" ")[-1]
                return_type = strip_line.split("(")[0].split(" ")[1]
                input_parts = strip_line.split("(")[1].split(")")[0].strip().split(",")
                for i, input_part in enumerate(input_parts):
                    var_split = input_part.strip().split(" ")
                    rt_type, variable = var_split[0], var_split[1]
                    variables.append(variable)
                    parse_input.append(__process_variable_type(f"values[{i}]", variable, rt_type))
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
                    return_part = variables[0]
                else:
                    return_part = "{}({})".format(return_func, ", ".join(variables))
            import_packages.extend(additional_import)
            body.append(line)

    return SOLUTION_TEMPLATE_JAVA.format(
        problem_id,
        "\n".join(import_packages),
        "{",
        "\n".join(body),
        "{",
        "\n\t\t".join(parse_input),
        return_part,
        "}",
        "}"
    )


def get_solution_code_java(root_path, problem_folder: str, problem_id: str) -> (str, str):
    if not problem_id:
        with open(os.path.join(root_path, "qubhjava", "test", "TestMain.java"), 'r', encoding="utf-8") as f:
            lines = f.read().split("\n")
            for line in lines:
                if "private static final String PROBLEM_ID = \"" in line:
                    problem_id = line.split('"')[1]
                    break
    if not problem_id:
        return "", problem_id
    file_path = os.path.join(root_path, problem_folder, f"problems_{problem_id}", "Solution.java")
    if not os.path.exists(file_path):
        return "", problem_id
    final_codes = deque([])
    with open(file_path, 'r', encoding="utf-8") as f:
        lines = f.read().split("\n")
        solve_part = False
        for line in lines:
            if line.startswith("package "):
                continue
            if line.startswith("import "):
                continue
            if "public Object solve(String[] values) {" in line:
                last = final_codes.pop()
                if last.strip() != "@Override":
                    final_codes.append(last)
                solve_part = True
                continue
            if solve_part and line.strip() != "}":
                continue
            elif solve_part:
                solve_part = False
                continue
            if "public class Solution extends BaseSolution {" in line:
                final_codes.append("class Solution {")
                continue
            final_codes.append(line)
    while final_codes and final_codes[0].strip() == '':
        final_codes.popleft()
    return "\n".join(final_codes), problem_id
