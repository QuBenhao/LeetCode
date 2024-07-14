import solution
from typing import *
from collections import defaultdict

class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.accountsMerge(test_input)

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}
        email_to_id = {}
        id_to_email = {}
        id_to_name = {}
        id = 0

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = id
                    id_to_email[id] = email
                    id_to_name[id] = name
                    parent[id] = id
                    id += 1
                email_to_name[email] = name
                union(email_to_id[account[1]], email_to_id[email])

        ans = defaultdict(list)
        for email in email_to_id:
            ans[find(email_to_id[email])].append(email)

        return [[id_to_name[k]] + sorted(v) for k, v in ans.items()]
