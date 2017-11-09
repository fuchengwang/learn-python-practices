from pprint import pformat
from itertools import permutations

class NQueen:

    def __init__(self, size):
        self.queens = []

        self.chess = [[0] * size for i in range(size)]
        self.width = self.height = size

    def get_queen_range(self, x, y):
        range_set = set()

        diff = x - y
        sum = x + y

        for i in range(self.width):
            for j in range(self.height):
                if i - j == diff or i + j == sum: #  斜方向
                    range_set.add((i, j))
                elif i == x or j == y:  # 横竖方向
                    range_set.add((i, j))
        return range_set

    def add(self, x, y):
        "添加一个皇后, 添加成功返回True"
        if self.chess[x][y] > 0:
            return False

        self.queens.append((x, y))
        points = self.get_queen_range(x, y)
        for p in points:
            self.chess[p[0]][p[1]] += 1
        return True

    def rm(self, x, y):
        "拿走一个皇后"
        if (x, y) not in self.queens:
            return False

        points = self.get_queen_range(x, y)
        for p in points:
            self.chess[p[0]][p[1]] -= 1
        self.queens.remove((x, y))
        return True

    def max(self):
        seq = permutations(range(self.height))
        max = 0
        for t in seq:
            for i in t:
                self.add(i, t[i])
            if len(self.queens) > max:
                max = len(self.queens)
            self.clear()
        return max

    def clear(self):
        self.queens = []
        self.chess = [[0] * self.width for i in range(self.height)]

    def __str__(self):
        return pformat(self.chess)

    def __repr__(self):
        return pformat(self.chess) + "\nqueens: " + str(self.queens)


import cProfile

bag  =[]
def queen(A,cur=0):
    if cur == len(A): bag.append(A) ;return
    for col in range(len(A)):
        A[cur],flag = col,True
        for row in range(cur):
            if A[row] == col or abs(col-A[row])==cur - row:flag=False;break
        if flag:queen(A,cur+1)



pr = cProfile.Profile()
pr.enable()

queen([None]*8)
print(len(bag))
pr.disable()
pr.print_stats()
