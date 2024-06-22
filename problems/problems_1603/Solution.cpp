//go:build ignore
#include "cpp/common/Solution.h"
class ParkingSystem {
public:
    ParkingSystem(int big, int medium, int small) {

    }
    
    bool addCar(int carType) {

    }
};


using namespace std;
using json = nlohmann::json;

class ParkingSystem {
public:
    ParkingSystem(int big, int medium, int small) {

    }
    
    bool addCar(int carType) {

    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */

json leetcode::qubh::Solve(string input) {
	vector<string> inputArray;
	size_t pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);



}
