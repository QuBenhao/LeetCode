from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['joe', 'joe', 'joe', 'james', 'james', 'james', 'james', 'mary', 'mary', 'mary'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['home', 'about', 'career', 'home', 'cart', 'maps', 'home', 'home', 'about', 'career']], Output=['home', 'about', 'career']))
		self.testcases.append(case(Input=[['ua', 'ua', 'ua', 'ub', 'ub', 'ub'], [1, 2, 3, 4, 5, 6], ['a', 'b', 'a', 'a', 'b', 'c']], Output=['a', 'b', 'a']))

	def get_testcases(self):
		return self.testcases
