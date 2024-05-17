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
