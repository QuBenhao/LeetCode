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

func Solve(input string) {}
\tvalues := strings.Split(input, "\\n")
{}
{}
\treturn {}({})
{}
"""

SOLUTION_TEMPLATE_JAVA = """package problems.problems_{};

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
{}

public class Solution extends BaseSolution {}
{}

    @Override
    public Object solve(String[] values) {}
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

json leetcode::qubh::Solve(string input)
{}
\tvector<string> inputArray;
\tsize_t pos = input.find('\\n');
\twhile (pos != string::npos) {}
\t\tinputArray.push_back(input.substr(0, pos));
\t\tinput = input.substr(pos + 1);
\t\tpos = input.find('\\n');
\t{}
\tinputArray.push_back(input);

{}
{}
{}
"""
