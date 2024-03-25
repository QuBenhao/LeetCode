from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['cooler', 'lock', 'touch'], ['i like cooler cooler', 'lock touch cool', 'locker like touch']], Output=['touch', 'cooler', 'lock']))
		self.testcases.append(case(Input=[['a', 'aa', 'b', 'c'], ['a', 'a aa', 'a a a a a', 'b a']], Output=['a', 'aa', 'b', 'c']))

	def get_testcases(self):
		return self.testcases
