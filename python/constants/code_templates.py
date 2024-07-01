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

func Solve(inputJsonValues string) {}
\tinputValues := strings.Split(inputJsonValues, "\\n")
{}
{}
\treturn {}({})
{}
"""

SOLUTION_TEMPLATE_GOLANG_MODIFY_IN_PLACE = """package problem{}

import (
{}
)

{}

func Solve(inputJsonValues string) {}
\tinputValues := strings.Split(inputJsonValues, "\\n")
{}
{}
\t{}({})
\treturn {}
{}
"""

TESTCASE_TEMPLATE_GOLANG = """package golang

import (
\t{}
\t"testing"
)

func {}(t *testing.T) {}
\t{}
{}
"""

SOLUTION_TEMPLATE_JAVA = """package {}.{}_{};

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
{}

public class Solution extends BaseSolution {}
{}

    @Override
    public Object solve(String[] inputJsonValues) {}
        {}
        return JSON.toJSON({});
    {}
{}
"""

SOLUTION_TEMPLATE_CPP = """//go:build ignore
#include "cpp/common/Solution.h"
{}

using namespace std;
using json = nlohmann::json;

{}

json leetcode::qubh::Solve(string input_json_values) {}
\tvector<string> inputArray;
\tsize_t pos = input_json_values.find('\\n');
\twhile (pos != string::npos) {}
\t\tinputArray.push_back(input_json_values.substr(0, pos));
\t\tinput_json_values = input_json_values.substr(pos + 1);
\t\tpos = input_json_values.find('\\n');
\t{}
\tinputArray.push_back(input_json_values);

{}
{}
{}
"""

SOLUTION_TEMPLATE_TYPESCRIPT = """{}{}

export function Solve(inputJsonElement: string): any {}
\tconst inputValues: string[] = inputJsonElement.split(\"\\n\");
{}
\treturn {};
{}
"""
