from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[12, 345, 2, 6, 7896], Output=2))
		self.testcases.append(case(Input=[555, 901, 482, 1771], Output=1))

	def get_testcases(self):
		return self.testcases
