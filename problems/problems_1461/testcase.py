from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['00110110', 2], Output=True))
		self.testcases.append(case(Input=['0110', 1], Output=True))
		self.testcases.append(case(Input=['0110', 2], Output=False))
		self.testcases.append(case(Input=["00110",2], Output=True))
		self.testcases.append(case(Input=["01",1], Output=True))

	def get_testcases(self):
		return self.testcases
