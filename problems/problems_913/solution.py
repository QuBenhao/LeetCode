import solution
from typing import *
from collections import deque

HOLE, MOUSE_START, CAT_START = 0, 1, 2
MOUSE_TURN, CAT_TURN = 0, 1
UNKNOWN, MOUSE_WIN, CAT_WIN = 0, 1, 2


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.catMouseGame(test_input)

    def catMouseGame(self, graph: List[List[int]]) -> int:
        self.__n = len(graph)
        self.__graph = graph
        self.__degrees = [[[0, 0] for _ in range(self.__n)] for _ in range(self.__n)]
        self.__results = [[[0, 0] for _ in range(self.__n)] for _ in range(self.__n)]
        for i in range(self.__n):
            for j in range(1, self.__n):
                self.__degrees[i][j][MOUSE_TURN] = len(graph[i])
                self.__degrees[i][j][CAT_TURN] = len(graph[j])
        for i in range(self.__n):
            for j in graph[HOLE]:
                self.__degrees[i][j][CAT_TURN] -= 1
        q = deque()
        for i in range(1, self.__n):
            self.__results[i][i][MOUSE_TURN] = CAT_WIN
            self.__results[i][i][CAT_TURN] = CAT_WIN
            q.append((i, i, MOUSE_TURN))
            q.append((i, i, CAT_TURN))
        for j in range(1, self.__n):
            self.__results[HOLE][j][MOUSE_TURN] = MOUSE_WIN
            self.__results[HOLE][j][CAT_TURN] = MOUSE_WIN
            q.append((HOLE, j, MOUSE_TURN))
            q.append((HOLE, j, CAT_TURN))
        while q:
            state = q.popleft()
            mouse, cat, turn = state
            result = self.__results[mouse][cat][turn]
            prevStates = self.__getPrevStates(mouse, cat, turn)
            for prevState in prevStates:
                prevMouse, prevCat, prevTurn = prevState
                if self.__results[prevMouse][prevCat][prevTurn] == UNKNOWN:
                    winState = (result == MOUSE_WIN and prevTurn == MOUSE_TURN) or (
                                result == CAT_WIN and prevTurn == CAT_TURN)
                    if winState:
                        self.__results[prevMouse][prevCat][prevTurn] = result
                        q.append((prevMouse, prevCat, prevTurn))
                    else:
                        self.__degrees[prevMouse][prevCat][prevTurn] -= 1
                        if self.__degrees[prevMouse][prevCat][prevTurn] == 0:
                            self.__results[prevMouse][prevCat][prevTurn] = result
                            q.append((prevMouse, prevCat, prevTurn))
        return self.__results[MOUSE_START][CAT_START][MOUSE_TURN]

    def __getPrevStates(self, mouse, cat, turn) -> List[tuple]:
        prevStates = []
        prevTurn = CAT_TURN if turn == MOUSE_TURN else MOUSE_TURN
        if prevTurn == CAT_TURN:
            for prevCat in self.__graph[cat]:
                if prevCat != HOLE:
                    prevStates.append((mouse, prevCat, prevTurn))
        else:
            for prevMouse in self.__graph[mouse]:
                prevStates.append((prevMouse, cat, prevTurn))
        return prevStates
