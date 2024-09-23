from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abdcdbc', 'ac'], Output=4))
		self.testcases.append(case(Input=['aabb', 'ab'], Output=6))

	def get_testcases(self):
		return self.testcases
