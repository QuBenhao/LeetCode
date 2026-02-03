from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[0, -2, -1, -3, 0, 2, -1], Output=-4))
		self.testcases.append(case(Input=[1, 4, 2, 7], Output=14))
		self.testcases.append(case(Input=[2,993,-791,-635,-569], Output=-431))
		self.testcases.append(case(Input=[286,528,-900,327,536,625,547,997], Output=3032))
		self.testcases.append(case(Input=[1,4,2,2,3,1,2], Output=8))

	def get_testcases(self):
		return self.testcases
