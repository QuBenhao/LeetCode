from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 4], [2, 3]], Output=True))
		self.testcases.append(case(Input=[[1, 2], [3, 4]], Output=True))
		self.testcases.append(case(Input=[[1, 2, 4], [2, 3, 5]], Output=False))
		self.testcases.append(case(Input=[[4, 1, 8], [3, 2, 6]], Output=False))
		self.testcases.append(case(Input=[[25372],[100000],[100000]], Output=True))

	def get_testcases(self):
		return self.testcases
