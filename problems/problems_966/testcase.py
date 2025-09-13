from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['KiTe', 'kite', 'hare', 'Hare'], ['kite', 'Kite', 'KiTe', 'Hare', 'HARE', 'Hear', 'hear', 'keti', 'keet', 'keto']], Output=['kite', 'KiTe', 'KiTe', 'Hare', 'hare', '', '', 'KiTe', '', 'KiTe']))
		self.testcases.append(case(Input=[['yellow'], ['YellOw']], Output=['yellow']))
		self.testcases.append(case(Input=[["ae","aa"],["UU"]], Output=["ae"]))

	def get_testcases(self):
		return self.testcases
