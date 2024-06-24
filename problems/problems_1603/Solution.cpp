//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class ParkingSystem {
public:
    ParkingSystem(int big, int medium, int small) {
        this->park = vector<int>{big, medium, small};
    }

    bool addCar(int carType) {
        if (this->park[--carType] > 0) {
            this->park[carType]--;
            return true;
        }
        return false;
    }

private:
    vector<int> park;
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

    vector<string> operators = json::parse(inputArray[0]);
    vector<vector<json>> values = json::parse(inputArray[1]);
    auto obj = make_shared<ParkingSystem>(values[0][0], values[0][1], values[0][2]);
    vector<json> ans = {nullptr};
    for (size_t i = 1; i < values.size(); i++) {
        if (operators[i] == "addCar") {
            ans.push_back(obj->addCar(values[i][0]));
        } else {
            ans.push_back(nullptr);
        }
    }
    return ans;
}
