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
    include_libs = []
    return SOLUTION_TEMPLATE_CPP.format(
        "\n".join(include_libs),
        code_default if not code else code,
        "{",
        "\t\n",
        "\t\n",
        "}"
    )
