import re
from python.constants import SOLUTION_TEMPLATE_CPP


def change_test_cpp(content: str, question_id: str) -> str:
    ans = []
    is_problem = False
    for line in content.split("\n"):
        if "name = \"problems\"," in line:
            is_problem = True
        elif is_problem and "path = \"" in line:
            ans.append("    path = \"problems/problems_{}/\",".format(question_id))
            is_problem = False
            continue
        ans.append(line)
    return "\n".join(ans)


def _extract_functions(code):
    # First, attempt to remove comments from the code
    no_comments_code = re.sub(r'/\*.*?\*/|//.*?\n', '', code, flags=re.DOTALL)

    # Then we define our pattern
    function_pattern = re.compile(r"""
        (?:(?P<access_mod>\b(public|protected|private)\b)\s*:)?     # access modifier followed by :
        \s*
        (?P<ret_type>[^\s:]*\**)?                      # return type, including * to capture pointer return types
        \s*
        (?:(?P<class_name>\b\w+\b)::)?                 # class name, followed by ::
        (?P<name>\b\w+\b)                               # function name
        \(
        (?P<args>[^\)]*)                                # function arguments within parentheses
        \)
    """, re.VERBOSE | re.MULTILINE)

    matches = function_pattern.finditer(no_comments_code)

    # Extract and return the information for each function
    functions = []
    for match in matches:
        functions.append(match.groupdict())

    return functions


def write_solution_cpp(code_default: str, code: str = None, problem_id: str = "") -> str:
    code = code if code else code_default
    functions = _extract_functions(code_default)

    include_libs = []
    process_variables = []
    return_part = []
    comments = False
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
        include_libs.append("#include \"cpp/models/TreeNode.h\";")
    if " ListNode " in code_default:
        include_libs.append("#include \"cpp/models/ListNode.h\";")

    if len(functions) == 1:
        ret_type = functions[0].get("ret_type", "")
        func_name = functions[0].get("name", "")
        variables = [sp.strip().split(" ") for sp in functions[0].get("args", "").split(",")]
        process_variables.append("\tSolution solution;")
        for i, variable in enumerate(variables):
            rt = variable[0] if not variable[0].endswith("&") and not variable[0].endswith("*") else variable[0][:-1]
            if rt == "ListNode":
                process_variables.append(
                    "std::vector<int> " + variable[1] + "_array" + f" = json::parse(inputArray.at({i}));")
                process_variables.append(rt + " *" + variable[1] + f" = IntArrayToListNode({variable[1]}_array);")
            elif rt == "TreeNode":
                process_variables.append("json " + variable[1] + "_array" + f" = json::parse(inputArray.at({i}));")
                process_variables.append(rt + " *" + variable[1] + f" = JsonArrayToTreeNode({variable[1]}_array);")
            else:
                process_variables.append(rt + " " + variable[1] + f" = json::parse(inputArray.at({i}));")
        if "ListNode" in ret_type:
            return_part.append(
                "\treturn ListNodeToIntArray(solution.{}({}));"
                .format(func_name, ", ".join([v[1] for v in variables])))
        elif "TreeNode" in ret_type:
            return_part.append("\treturn TreeNodeToJsonArray(solution.{}({}));"
                               .format(func_name, ", ".join([v[1] for v in variables])))
        else:
            return_part.append("\treturn solution.{}({});"
                               .format(func_name, ", ".join([v[1] for v in variables])))
    elif len(functions) > 1:
        pass

    return SOLUTION_TEMPLATE_CPP.format(
        "\n".join(include_libs),
        code,
        "{",
        "{",
        "}",
        "\n\t".join(process_variables),
        "\n\t".join(return_part),
        "}"
    )
