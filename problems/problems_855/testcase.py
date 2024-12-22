from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['ExamRoom', 'seat', 'seat', 'seat', 'seat', 'leave', 'seat'], [[10], [], [], [], [], [4], []]], Output=[None, 0, 9, 4, 2, None, 5]))

	def get_testcases(self):
		return self.testcases
