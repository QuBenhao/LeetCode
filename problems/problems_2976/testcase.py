from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abcd', 'acbe', ['a', 'b', 'c', 'c', 'e', 'd'], ['b', 'c', 'b', 'e', 'b', 'e'], [2, 5, 5, 1, 2, 20]], Output=28))
		self.testcases.append(case(Input=['aaaa', 'bbbb', ['a', 'c'], ['c', 'b'], [1, 2]], Output=12))
		self.testcases.append(case(Input=['abcd', 'abce', ['a'], ['e'], [10000]], Output=-1))
		self.testcases.append(case(Input=["edaaddbeeddbedcdcccbdceaacacceaaacadbebadacebdceddbaccaedddebcddbccacbccededaaaabdaaebdaaececadabbdbacaeadeeacedecdccdabddaaceaceacbcccbabaecedbcdedbbeedacaadbecaddbcdececeddcdbeeabbccbceababbcccddbadccabbdebebcaadbaccceacecbddacadbbcbdcaccdbeaddecedaedaababbeedbebccebdeecaeaedbaeaceddaaeacbedcecaddcccbadedbbadabddaadbeeedaaadbacbeecaddcbbeababbcbddceebadeccbbaddeedecadaadcebbbcbcadecbebbaeededacecadbdcbcdeadacdedaaccbabbccaaeccbcbbdaacdaecbeedbcaabaaadceaacbeebbebedbccabaebedbbaecbbebbbaaeecdea","bccdeacaebeecedcdcdcbaebabeebaeadaaaeedabadbbbeadccaedaabebdacdddcccddcaccedecacdbbceaadddbcceddccaecadacecabcceecebcddacdbebcadeeabeaabbaccaeddbdbdcbeccddedecabdaeddbbeddbccacabdabacaadbbccecedcdadbecadcaecaddbaeecaecccaecebdddeebeaadeeadedacbbeecaeaeecedcdeedbacdedcdcecbcbeddacadaadceeaecdabbaeddbabeadbcbcbbceebeaccaaccaadaddbcaaaeabccdbeedcdbbbadcbbadeaeadbbcaabcebebeddebaaeabdedbddcdbedcebdcabdbcecbacdbeddaeaebccaaabcddebecbbaadacebbadebbacdeaabcbbeeeeedaacaabdeedbccebdedcdcebabbbdccbcdaeaad",["a","b","a","b","d","e","d","e","b","d","c"],["b","d","d","a","c","d","e","b","e","a","d"],[76,34,33,14,27,74,33,44,31,82,8]], Output=20873))

	def get_testcases(self):
		return self.testcases
