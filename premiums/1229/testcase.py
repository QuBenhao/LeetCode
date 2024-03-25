from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8], Output=[60, 68]))
		self.testcases.append(case(Input=[[[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12], Output=[]))

	def get_testcases(self):
		return self.testcases
