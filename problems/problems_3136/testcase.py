from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="234Adas", Output=True))
		self.testcases.append(case(Input="b3", Output=False))
		self.testcases.append(case(Input="a3$e", Output=False))
		self.testcases.append(case(Input="IS", Output=False))

	def get_testcases(self):
		return self.testcases
