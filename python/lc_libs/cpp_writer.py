import re
from python.constants import SOLUTION_TEMPLATE_CPP


def change_test_cpp(content: str, question_id: str) -> str:
    # ans = []
    # for line in content.split("\n"):
    #     if "problem \"leetCode/problems/" in line:
    #         ans.append(f'\tproblem "leetCode/problems/problems_{question_id}"')
    #         continue
    #     elif "var problemId string =" in line:
    #         ans.append(f'var problemId string = "{question_id}"')
    #         continue
    #     ans.append(line)
    # return "\n".join(ans)
    return ""


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
    """#include "cpp/common/Solution.h"
    {}

    using namespace std;
    using json = nlohmann::json;

    {}

    json leetcode::qubh::Solve(string input)
    {}
    {}
    {}
    {}
    """
    code = code if code else code_default
    functions = _extract_functions(code)

    include_libs = []
    process_variables = []
    return_part = []
    for line in code.split("\n"):
        if "class Solution" in line:
            break
        include_libs.append(line)

    if len(functions) == 1:
        ret_type = functions[0].get("ret_type", "")
        func_name = functions[0].get("name", "")
        variables = [sp.strip().split(" ") for sp in functions[0].get("args", "").split(",")]
        process_variables.append("\tSolution solution;")
        for i, variable in enumerate(variables):
            process_variables.append(variable[0] + " " + variable[1] + f" = json::parse(inputArray.at({i}));")

        return_part.append("\treturn solution.{}({});".format(func_name, ", ".join([v[1] for v in variables])))
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
