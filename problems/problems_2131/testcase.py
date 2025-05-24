from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['lc', 'cl', 'gg'], Output=6))
		self.testcases.append(case(Input=['ab', 'ty', 'yt', 'lc', 'cl', 'ab'], Output=8))
		self.testcases.append(case(Input=['cc', 'll', 'xx'], Output=2))

	def get_testcases(self):
		return self.testcases
