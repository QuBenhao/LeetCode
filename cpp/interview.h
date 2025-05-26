//
// Created by BenHao on 2025/5/26.
//

#ifndef PRACTICE_INTERVIEW_H
#define PRACTICE_INTERVIEW_H

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <cmath>
#include <climits>
#include <limits>
#include <functional>

// 常用数据结构定义
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
    ~ListNode() {
        delete next; // 注意：递归删除可能导致栈溢出，实际使用中应谨慎
    }
};

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    ~TreeNode() {
        delete left;
        delete right;
    }
};

namespace InterviewUtils {

// 基础输入处理
template<typename T>
std::vector<T> read_vector() {
    std::cout << "Enter elements (space-separated): ";
    std::vector<T> res;
    std::string line;
    std::getline(std::cin, line);
    std::istringstream iss(line);
    T val;
    while (iss >> val) {
        res.push_back(val);
    }
    return res;
}

template<typename T>
std::vector<std::vector<T>> read_matrix() {
    std::cout << "Enter matrix rows (end with an empty line):\n";
    std::vector<std::vector<T>> matrix;
    std::string line;
    while (std::getline(std::cin, line)) {
        if (line.empty()) break;
        std::istringstream iss(line);
        matrix.emplace_back(std::istream_iterator<T>{iss},
                          std::istream_iterator<T>{});
    }
    return matrix;
}

// 链表构建与输出
ListNode* build_linked_list(const std::vector<int>& nums) {
    ListNode dummy(0);
    ListNode* curr = &dummy;
    for (int num : nums) {
        curr->next = new ListNode(num);
        curr = curr->next;
    }
    return dummy.next;
}

void print_linked_list(ListNode* head) {
    while (head) {
        std::cout << head->val;
        if (head->next) std::cout << "->";
        head = head->next;
    }
    std::cout << "\n";
}

// 二叉树构建（层序输入）
TreeNode* build_tree(const std::vector<std::string>& nodes) {
    if (nodes.empty() || nodes[0] == "null") return nullptr;

    std::queue<TreeNode*> q;
    TreeNode* root = new TreeNode(std::stoi(nodes[0]));
    q.push(root);

    for (size_t i = 1; i < nodes.size();) {
        TreeNode* curr = q.front();
        q.pop();

        // 左子节点
        if (i < nodes.size() && nodes[i] != "null") {
            curr->left = new TreeNode(std::stoi(nodes[i]));
            q.push(curr->left);
        }
        i++;

        // 右子节点
        if (i < nodes.size() && nodes[i] != "null") {
            curr->right = new TreeNode(std::stoi(nodes[i]));
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

void print_tree(TreeNode* root, int level = 0) {
    if (!root) return;
    print_tree(root->right, level + 1);
    std::cout << std::string(level * 4, ' ') << root->val << "\n";
    print_tree(root->left, level + 1);
}

// 调试输出工具
template<typename T>
void print_container(const T& container) {
    for (const auto& item : container) {
        std::cout << item << " ";
    }
    std::cout << "\n";
}

template<typename T>
void print_matrix(const std::vector<std::vector<T>>& matrix) {
    for (const auto& row : matrix) {
        print_container(row);
    }
}

} // namespace InterviewUtils

#endif // PRACTICE_INTERVIEW_H