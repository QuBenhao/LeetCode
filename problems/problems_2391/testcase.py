from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['G', 'P', 'GP', 'GG'], [2, 4, 3]], Output=21))
		self.testcases.append(case(Input=[['MMM', 'PGM', 'GP'], [3, 10]], Output=37))

	def get_testcases(self):
		return self.testcases
