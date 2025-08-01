from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['with', 'example', 'science'], 'thehat'], Output=3))
		self.testcases.append(case(Input=[['notice', 'possible'], 'basicbasic'], Output=-1))

	def get_testcases(self):
		return self.testcases
