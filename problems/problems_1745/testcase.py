from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input="abcbdd", Output=True))
        self.testcases.append(case(Input="bcbddxy", Output=False))
        self.testcases.append(case(Input="yoldbrnfqvglfbxztwwivkymyamkpqqvcmqgsqfvvnnjhmmojxbbcybpdraxkrxvusfpumqymfximqihsrzeaubfukcbxdmqwjxfkxfvxiuvzylfxbuuszyjnmsrqioroariezxsztamlwqmprpndmwozwfnzpseuhubnryucpwokhtoujujraevvvdnmnjghsmgrgqhzxbyxpftgljkkknhunjrkaudfwhbmpjzpqoyxdhxhdatvnffommwuwvtcmtxdmocqbbewnuulhvqnfivonslpkwzvqviczcpxlnoazloehioimoiwvoqtkoijfjusecfwftouybiydtxdxclkjhlbcnppjgjhxryvbsantbdouproytalcmsgxzpcsxydkyznqqsrhvkjkegccxfrubpzbgucdcspbncqluabxdxeundxlqnzhmjgeeslykjghqneduxfhnsjztihpmmbhyenqcogkeahlezbspfdjxwcorltybcttbicjyokozqwajggpxksgnqahvqxoblbmihmxcjhugwguqvzxoxxtzvjhiyrainydjydmokklvrmhyjezwikaraayvhcxdlpxsckewxynipvfecsxnmyiklwshjfvgbyesflgifekgrbfnulrittoyxuqsgwfaudrdtmliyfzgphvwxhpicwtbumdpmgadxcvhxmrbcav", Output=False))

    def get_testcases(self):
        return self.testcases
