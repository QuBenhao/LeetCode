from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['great', 'acting', 'skills'], ['fine', 'drama', 'talent'], [['great', 'fine'], ['drama', 'acting'], ['skills', 'talent']]], Output=True))
		self.testcases.append(case(Input=[['great'], ['great'], []], Output=True))
		self.testcases.append(case(Input=[['great'], ['doubleplus', 'good'], [['great', 'doubleplus']]], Output=False))

	def get_testcases(self):
		return self.testcases
