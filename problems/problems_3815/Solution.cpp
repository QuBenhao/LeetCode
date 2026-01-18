//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class AuctionSystem {
public:
    AuctionSystem() {
        
    }
    
    void addBid(int userId, int itemId, int bidAmount) {
        
    }
    
    void updateBid(int userId, int itemId, int newAmount) {
        
    }
    
    void removeBid(int userId, int itemId) {
        
    }
    
    int getHighestBidder(int itemId) {
        
    }
};

/**
 * Your AuctionSystem object will be instantiated and called as such:
 * AuctionSystem* obj = new AuctionSystem();
 * obj->addBid(userId,itemId,bidAmount);
 * obj->updateBid(userId,itemId,newAmount);
 * obj->removeBid(userId,itemId);
 * int param_4 = obj->getHighestBidder(itemId);
 */

json leetcode::qubh::Solve(string input_json_values) {
	vector<string> inputArray;
	size_t pos = input_json_values.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input_json_values.substr(0, pos));
		input_json_values = input_json_values.substr(pos + 1);
		pos = input_json_values.find('\n');
	}
	inputArray.push_back(input_json_values);

	vector<string> operators = json::parse(inputArray[0]);
	vector<vector<json>> op_values = json::parse(inputArray[1]);
	auto obj0 = make_unique<AuctionSystem>();
	vector<json> ans = {nullptr};
	for (size_t i = 1; i < op_values.size(); ++i) {
		if (operators[i] == "addBid") {
			obj0->addBid(op_values[i][0], op_values[i][1], op_values[i][2]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "updateBid") {
			obj0->updateBid(op_values[i][0], op_values[i][1], op_values[i][2]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "removeBid") {
			obj0->removeBid(op_values[i][0], op_values[i][1]);
			ans.push_back(nullptr);
			continue;
		}
		if (operators[i] == "getHighestBidder") {
			ans.push_back(obj0->getHighestBidder(op_values[i][0]));
			continue;
		}
		ans.push_back(nullptr);
	}
	return ans;
}
