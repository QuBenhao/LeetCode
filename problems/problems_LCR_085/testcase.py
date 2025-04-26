from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=3, Output=['((()))', '(()())', '(())()', '()(())', '()()()']))
		self.testcases.append(case(Input=1, Output=['()']))

	def get_testcases(self):
		return self.testcases
