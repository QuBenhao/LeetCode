TESTCASE_TEMPLATE_PYTHON = """from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
\tdef __init__(self):
\t\tself.testcases = []
{}
\tdef get_testcases(self):
\t\treturn self.testcases
"""

TESTCASE_TEMPLATE_PYTHON_TESTCASES = "\t\tself.testcases.append(case(Input={}, Output={}))\n"

SOLUTION_TEMPLATE_PYTHON = """import solution
from typing import *
{}

class Solution(solution.Solution):
    def solve(self, test_input=None):
        {}

{}
"""

SOLUTION_TEMPLATE_GOLANG = """package problem{}

import (
{}
)

{}

func Solve(inputJsonValues string) any {{
\tinputValues := strings.Split(inputJsonValues, "\\n")
{}
{}
\t{}return {}
}}{}
"""

SOLUTION_TEMPLATE_GOLANG_MODIFY_IN_PLACE = """package problem{}

import (
{}
)

{}

func Solve(inputJsonValues string) any {{
\tinputValues := strings.Split(inputJsonValues, "\\n")
{}
{}
\t{}({})
\treturn {}
}}{}
"""

TESTCASE_TEMPLATE_GOLANG = """package golang

import (
\t{}
\t"testing"
)

func {}(t *testing.T) {{
\t{}
}}
"""

SOLUTION_TEMPLATE_JAVA = """package {}.{}_{};

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
{}

public class Solution extends BaseSolution {{
{}

    @Override
    public Object solve(String[] inputJsonValues) {{
        {}
        return JSON.toJSON({});
    }}
}}{}
"""

SOLUTION_TEMPLATE_CPP = """//go:build ignore
#include "cpp/common/Solution.h"
{}

using namespace std;
using json = nlohmann::json;

{}

json leetcode::qubh::Solve(string input_json_values) {{
\tvector<string> inputArray;
\tsize_t pos = input_json_values.find('\\n');
\twhile (pos != string::npos) {{
\t\tinputArray.push_back(input_json_values.substr(0, pos));
\t\tinput_json_values = input_json_values.substr(pos + 1);
\t\tpos = input_json_values.find('\\n');
\t}}
\tinputArray.push_back(input_json_values);

{}
{}
}}
"""

TESTCASE_TEMPLATE_CPP = """cc_test(
    name = "test_problem_{}",
    size = "small",
    srcs = [
        "//cpp:TestMain.cpp",
        "//cpp:TestMain.h",
        "//cpp/common:Solution.h",
        "@problem{}//:Solution.cpp"
    ],
    args = [
        "$(rlocationpath @problem{}//:testcase)",
    ],
    data = ["@problem{}//:testcase"],
    deps = [
        "//cpp/models:models",
        "@bazel_tools//tools/cpp/runfiles",
        "@googletest//:gtest_main",
        "@nlohmann_json//:json",
    ],
)
"""

SOLUTION_TEMPLATE_TYPESCRIPT = """{}{}

export function Solve(inputJsonElement: string): any {{
\tconst inputValues: string[] = inputJsonElement.split(\"\\n\");
{}
\treturn {};
}}{}
"""

SOLUTION_TEMPLATE_RUST = """{}use serde_json::{{json, Value}};
{}
{}
{}

#[cfg(feature = "solution_{}")]
pub fn solve(input_string: String) -> Value {{
\tlet input_values: Vec<String> = input_string.split('\\n').map(|x| x.to_string()).collect();
\t{}
}}
"""

SOLUTIONS_TEMPLATE_RUST = """const PROBLEMS: [[&str; 2]; {}] = [{}];

#[cfg(test)]
mod test {{
\tuse test_executor::run_test::run_test;
\tuse crate::PROBLEMS;

\t{}

\t#[test]
\tfn test_solutions() {{
\t\tfor (i, problem) in PROBLEMS.iter().enumerate() {{
\t\t\tlet (folder, id) = (problem[0], problem[1]);
\t\t\tprintln!("Testing problem {{}}", id);
\t\t\trun_test(id, folder, match i {{
\t\t\t\t{}
\t\t\t\t_ => panic!("Unknown solution"),
\t\t\t}});
\t\t}}
\t}}
}}
"""

CARGO_TOML_TEMPLATE_SOLUTION = """[package]
name = "solution_{}"
version = "0.1.0"
edition = "2021"
rust-version = "1.79.0"
authors = ["benhao"]
description = "LeetCode Solution {} in Rust"
readme = "../../README.md"

[features]
solution_{} = []

[dependencies]
serde_json = "1.0"
rand = "0.8.4"
regex = "1.10.5"
library = {{ path = "../../rust/library", features = ["model"] }}

[lib]
name = "solution_{}"
path = "solution.rs"
"""

CONTEST_TEMPLATE_PYTHON = """# Add all common imports.
import heapq
from bisect import *
from typing import *
from functools import *
from itertools import *
from sortedcontainers import *
from collections import *
from heapq import *
from math import *

# Add all common object libraries.
from python.object_libs.linked_list import ListNode
from python.object_libs.tree import TreeNode

############################# USER CODE STARTS HERE #############################

{}

############################### USER CODE ENDS HERE #############################

if __name__ == '__main__':
    import json
    
    with open("input.json", "r") as f:
        input_json = json.load(f)
    with open("output.json", "r") as f:
        output_json = json.load(f)
    sol = Solution()
    
    # find and call the function and pass the input_json as argument, compare the output with output_json
    function_name = "" # Fill in the function name or find by default attr
    if not function_name:
        function_name = [name for name in dir(sol) if not name.startswith("__") and callable(getattr(sol, name))][0]
    print(f"Function name: {{function_name}}")

    for i, (it, ot) in enumerate(zip(input_json, output_json)):
        result = getattr(sol, function_name)(*it)
        assert result == ot, f"[Testcase#{{i}}] {{it}}:Expected {{ot}}, but got {{result}}"

    print("All tests passed")
"""
