from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[12, 28, 46, 32, 50], [50, 12, 32, 46, 28]], Output=[1, 4, 3, 2, 0]))
		self.testcases.append(case(Input=[[84, 46], [84, 46]], Output=[0, 1]))

	def get_testcases(self):
		return self.testcases
