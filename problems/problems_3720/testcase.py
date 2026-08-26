from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abc', 'bba'], Output="bca"))
		self.testcases.append(case(Input=['leet', 'code'], Output="eelt"))
		self.testcases.append(case(Input=['baba', 'bbaa'], Output=""))

	def get_testcases(self):
		return self.testcases
