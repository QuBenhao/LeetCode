from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['area', 'lead', 'wall', 'lady', 'ball'], Output=[['ball', 'area', 'lead', 'lady'], ['wall', 'area', 'lead', 'lady']]))
		self.testcases.append(case(Input=['abat', 'baba', 'atan', 'atal'], Output=[['baba', 'abat', 'baba', 'atal'], ['baba', 'abat', 'baba', 'atan']]))

	def get_testcases(self):
		return self.testcases
