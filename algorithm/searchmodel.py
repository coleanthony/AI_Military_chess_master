"""
 * Alpha beta search.
"""
from algorithm.evalmodel import *
from algorithm.alphabetanode import *
from GameEngine.LBChess import *
import numpy as np
import subprocess


class SearchModel:
    def __init__(self, player, time):
        self.player = player
        self.board = None
        # 设定搜索的时间限制
        self.time = time
        # 初始搜索深度为2
        self.DEPTH = 2
        # 定义最大连续不吃子的半回合数
        self.MAX_SEMI_ROUND = 14
        # 将self.player的值与红黑方对应，便于调用eval()时使用
        self.dict = {1: 'b', -1: 'r'}
        # 计时子进程
        self.process = None

    def search(self, data, cnt):
        """
        使用 alphabetanode.py
        :param data: 当前棋盘的数据
        :param cnt: 记录当前连续未吃子的半回合数
        :return: 当前最优走法，以 AlphaBetaNode 的类型返回
        """
        self.board = LBChess(data)
        # 统计当前棋盘上的棋子数
        piece_num = np.count_nonzero(data)
        # 根据棋子数动态确定搜索深度
        if piece_num < 25:
            self.DEPTH = 3
        if piece_num < 18:
            self.DEPTH = 4
        if piece_num < 14:
            self.DEPTH = 5
        if piece_num < 10:
            self.DEPTH = 6

        # 记录当前搜索到的最优着法，AlphaBetaNode节点
        best_with_eat = best = None
        moves = self.generatemovesforall(self.player)

        # 创建计时子进程，用于控制搜索时间
        self.process = subprocess.Popen("python clock.py --time " + str(self.time - 2),
                                        stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        # 对当前走棋方所有可能的走法进行搜索
        for m in moves:
            # 行棋
            end_piece = self.board.data[m.to_where[0], m.to_where[1]]
            m_result = self.board.move(m.from_where, m.to_where)

            # 搜索
            m.value = -self.alphabeta(self.DEPTH, -float("inf"), float("inf"), -self.player)
            if best is None or m.value > best.value:
                best = m
            if (best_with_eat is None or m.value > best_with_eat.value) and m_result is not None:
                best_with_eat = m

            # 恢复棋盘
            self.board.data[m.from_where[0], m.from_where[1]] = m.piece
            self.board.data[m.to_where[0], m.to_where[1]] = end_piece

            # 如果时间到就停止搜索，直接返回当前最优着法
            if self.process.poll() == 0:
                return best if best_with_eat is None or cnt <= self.MAX_SEMI_ROUND else best_with_eat

        # 如果时间未到就完成搜索，则停止计时子进程，返回最优着法
        self.process.terminate()
        return best if best_with_eat is None or cnt <= self.MAX_SEMI_ROUND else best_with_eat

    def alphabeta(self, depth, alpha, beta, isMax):
        """
        :param depth: 搜索深度
        :param alpha: 当前搜索到的最优值
        :param beta: 当前对于对手来说的最坏值
        :param isMax: 当前行动方，1为黑，-1为红
        :Return evaluation if reaching leaf node or any side won.
        """
        # 若到达当前搜索深度的叶节点或游戏结束，则终止递归搜索，返回当前isMax角度的局势评估值
        if depth <= 0 or end(self.board.data) is not None:
            return evalmodel().eval(self.board.data, self.dict[isMax])

        # AlphaBeta剪枝算法
        moves = self.generatemovesforall(isMax)
        for m in moves:
            # 行棋
            end_piece = self.board.data[m.to_where[0], m.to_where[1]]
            self.board.move(m.from_where, m.to_where)

            # 采用了Negamax风格
            val = -self.alphabeta(depth - 1, -beta, -alpha, -isMax)

            # 恢复棋盘
            self.board.data[m.from_where[0], m.from_where[1]] = m.piece
            self.board.data[m.to_where[0], m.to_where[1]] = end_piece

            # 剪枝
            if val >= beta:
                return beta
            # 保留最大值
            if val > alpha:
                alpha = val
        return alpha

    def generatemovesforall(self, isMax):
        """
        :param isMax: 指示当前行动方 1为执黑，-1为执红
        :return: 返回当前行动方所有可能动作
        """
        data = self.board.data
        moves = []

        # 当前是黑方，故从黑方前线开始搜索
        if isMax == 1:
            for i in range(6, -1, -1):
                for j in range(5):
                    if data[i, j]*isMax <= 0:    # 考虑该点为对方棋子或者是空格则跳过
                        continue
                    for to_where in self.board.get([i, j]):
                        node = AlphaBetaNode(data[i, j], [i, j], to_where)
                        moves.append(node)
            for i in range(7, 13):
                for j in range(5):
                    if data[i, j]*isMax <= 0:
                        continue
                    for to_where in self.board.get([i, j]):
                        node = AlphaBetaNode(data[i, j], [i, j], to_where)
                        moves.append(node)

        # 当前是红方，故从红方前线开始搜索
        else:
            for i in range(6, 13):
                for j in range(5):
                    if data[i, j]*isMax <= 0:
                        continue
                    for to_where in self.board.get([i, j]):
                        node = AlphaBetaNode(data[i, j], [i, j], to_where)
                        moves.append(node)
            for i in range(5, -1, -1):
                for j in range(5):
                    if data[i, j]*isMax <= 0:
                        continue
                    for to_where in self.board.get([i, j]):
                        node = AlphaBetaNode(data[i, j], [i, j], to_where)
                        moves.append(node)
        return moves
