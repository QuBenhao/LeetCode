from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3, 4, 5], [1, 2, 5, 7, 9], [1, 3, 4, 5, 8]], Output=[1, 5]))
		self.testcases.append(case(Input=[[197, 418, 523, 876, 1356], [501, 880, 1593, 1710, 1870], [521, 682, 1337, 1395, 1764]], Output=[]))

	def get_testcases(self):
		return self.testcases
