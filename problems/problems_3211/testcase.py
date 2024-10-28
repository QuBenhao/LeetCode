from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=3, Output=['010', '011', '101', '110', '111']))
		self.testcases.append(case(Input=1, Output=['0', '1']))

	def get_testcases(self):
		return self.testcases
