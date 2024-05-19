from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['writing code', 'code rocks'], Output=['writing code rocks']))
		self.testcases.append(case(Input=['mission statement', 'a quick bite to eat', 'a chip off the old block', 'chocolate bar', 'mission impossible', 'a man on a mission', 'block party', 'eat my words', 'bar of soap'], Output=['a chip off the old block party', 'a man on a mission impossible', 'a manon a mission statement', 'a quick bite to eat my words', 'chocolate bar of soap']))
		self.testcases.append(case(Input=['a', 'b', 'a'], Output=['a']))

	def get_testcases(self):
		return self.testcases
