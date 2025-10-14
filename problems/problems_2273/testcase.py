from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abba', 'baba', 'bbaa', 'cd', 'cd'], Output=['abba', 'cd']))
		self.testcases.append(case(Input=['a', 'b', 'c', 'd', 'e'], Output=['a', 'b', 'c', 'd', 'e']))
		self.testcases.append(case(Input=["a","b","a"], Output=["a","b","a"]))

	def get_testcases(self):
		return self.testcases
