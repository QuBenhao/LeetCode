from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 1, 2, [5], [1.0, 1.3]], Output=5.0))
		self.testcases.append(case(Input=[3, 2, 3, [2, 5, 8], [1.0, 1.5, 0.75]], Output=14.5))
		self.testcases.append(case(Input=[2, 1, 2, [10, 10], [2.0, 2.0]], Output=-1.0))
		self.testcases.append(case(Input=[3,2,1,[70,100,90],[0.52]], Output=135.20000))

	def get_testcases(self):
		return self.testcases
