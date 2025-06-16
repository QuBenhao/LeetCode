//go:build ignore
#include <queue>

#include "cpp/common/Solution.h"
#include "cpp/models/NodeNeighbors.h"

using namespace std;
using json = nlohmann::json;

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
  Node *cloneGraph(Node *node) {
    if (node == nullptr) {
      return node;
    }

    unordered_map<Node *, Node *> visited;

    // 将题目给定的节点添加到队列
    queue<Node *> Q;
    Q.push(node);
    // 克隆第一个节点并存储到哈希表中
    visited[node] = new Node(node->val);

    // 广度优先搜索
    while (!Q.empty()) {
      // 取出队列的头节点
      auto n = Q.front();
      Q.pop();
      // 遍历该节点的邻居
      for (auto &neighbor : n->neighbors) {
        if (visited.find(neighbor) == visited.end()) {
          // 如果没有被访问过，就克隆并存储在哈希表中
          visited[neighbor] = new Node(neighbor->val);
          // 将邻居节点加入队列中
          Q.push(neighbor);
        }
        // 更新当前节点的邻居列表
        visited[n]->neighbors.emplace_back(visited[neighbor]);
      }
    }

    return visited[node];
  }
};

json leetcode::qubh::Solve(string input_json_values) {
  vector<string> inputArray;
  size_t pos = input_json_values.find('\n');
  while (pos != string::npos) {
    inputArray.push_back(input_json_values.substr(0, pos));
    input_json_values = input_json_values.substr(pos + 1);
    pos = input_json_values.find('\n');
  }
  inputArray.push_back(input_json_values);

  Solution solution;
  vector<vector<int>> node_arrays = json::parse(inputArray.at(0));
  Node *node = JsonArrayToNodeNeighbors(node_arrays);
  Node *res_ptr = solution.cloneGraph(node);
  json final_ans = NodeNeighborsToJsonArray(res_ptr);
  DeleteGraph(node);    // Delete the graph to prevent memory leak
  DeleteGraph(res_ptr); // Delete the graph to prevent memory leak
  return final_ans;
}