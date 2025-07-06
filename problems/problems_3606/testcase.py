from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=None, Output=['PHARMA5', 'SAVE20']))
		self.testcases.append(case(Input=None, Output=['ELECTRONICS_50']))

	def get_testcases(self):
		return self.testcases
