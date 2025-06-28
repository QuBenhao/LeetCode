from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['leet', 3, 'e', 1], Output="eet"))
		self.testcases.append(case(Input=['leetcode', 4, 'e', 2], Output="ecde"))
		self.testcases.append(case(Input=['bb', 2, 'b', 2], Output="bb"))
		self.testcases.append(case(Input=["aaabbbcccddd",3,"b",2], Output="abb"))
		self.testcases.append(case(Input=["mmmxmxymmm",8,"m",4], Output="mmmmxmmm"))

	def get_testcases(self):
		return self.testcases
