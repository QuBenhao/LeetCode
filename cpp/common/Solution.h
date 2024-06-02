#pragma once
#include <string>
#include <vector>
#include <nlohmann/json.hpp>

using json = nlohmann::json;
using namespace std;

namespace leetcode {
    namespace qubh {
        json Solve(string input);
    }
}