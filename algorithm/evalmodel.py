'''
Eval model
'''
from common import *
import numpy as np

class evalmodel:
    def __init__(self):
        '''
        only PieceValue and PiecePosition are implemented, so the array size is set to 3. */
        '''
        self.values=[[0]*3 for i in range(2)]

    def eval(self,board,player):
        '''
        board:13*5 array type
        player: string   'r' or 'b'
        :return:type int
        总的评估函数
        '''
        #循环整个棋盘
        for i in range(len(board)):
            for j in range(len(board[0])):
                #军旗
                temp=abs(board[i][j])
                #返回棋盘棋子代号的绝对值，方便计算得分

                #如果是地雷
                if temp==FLAG:
                    #如果是红方
                    if board[i][j]==-FLAG:
                        #value加上该棋子的价值评估与位置评估
                        self.values[0][0]+=self.evalpiecevalue(FLAG)
                        self.values[0][2]+=self.evalattack([12-i,4-j])
                    #如果是黑方
                    elif board[i][j]==FLAG:
                        # value加上该棋子的价值评估与位置评估
                        self.values[1][0]+=self.evalpiecevalue(FLAG)
                        self.values[1][2]+self.evalattack([i,j])

                #地雷
                elif temp==DI:
                    # 如果是红方
                    if board[i][j]==-DI:
                        # value加上该棋子的价值评估与位置评估
                        self.values[0][0]+=self.evalpiecevalue(DI)
                        self.values[0][2] += self.evalattack([12 - i, 4 - j])
                    # 如果是黑方
                    elif board[i][j]==DI:
                        # value加上该棋子的价值评估与位置评估
                        self.values[1][0]+=self.evalpiecevalue(DI)
                        self.values[1][2] + self.evalattack([i, j])


                 #炸弹
                elif temp==ZHA:
                    # 如果是红方
                    if board[i][j]==-ZHA:
                        # value加上该棋子的价值评估与位置评估
                        self.values[0][0]+=self.evalpiecevalue(ZHA)
                        position=[12-i,4-j]
                        self.values[0][1]+=self.evalpieceposition(ZHA,position)
                        self.values[0][2] += self.evalattack([12 - i, 4 - j])
                    # 如果是黑方
                    elif board[i][j]==ZHA:
                        # value加上该棋子的价值评估与位置评估
                        self.values[1][0]+=self.evalpiecevalue(ZHA)
                        position = [i, j]
                        self.values[1][1] += self.evalpieceposition(ZHA,position)
                        self.values[1][2] + self.evalattack([i, j])


                #工兵
                elif temp==GONG:
                    #如果是红方
                    if board[i][j]==-GONG:
                        # value加上该棋子的价值评估与位置评估
                        self.values[0][0]+=self.evalpiecevalue(GONG)
                        position = [12 -i, 4 -j]
                        self.values[0][1] += self.evalpieceposition(GONG, position)
                        self.values[0][2] += self.evalattack([12 - i, 4 - j])
                    # 如果是黑方
                    elif board[i][j]==GONG:
                        # value加上该棋子的价值评估与位置评估
                        self.values[1][0]+=self.evalpiecevalue(GONG)
                        position = [i, j]
                        self.values[1][1] += self.evalpieceposition(GONG, position)
                        self.values[1][2] + self.evalattack([i, j])


                #排长
                elif temp==PAI:
                    # 如果是红方
                    if board[i][j]==-PAI:
                        # value加上该棋子的价值评估与位置评估
                        self.values[0][0]+=self.evalpiecevalue(PAI)
                        position = [12 -i, 4 -j]
                        self.values[0][1] += self.evalpieceposition(PAI, position)
                        self.values[0][2] += self.evalattack([12 - i, 4 - j])

                    # 如果是黑方
                    elif board[i][j]==PAI:
                        # value加上该棋子的价值评估与位置评估
                        self.values[1][0]+=self.evalpiecevalue(PAI)
                        position = [i, j]
                        self.values[1][1] += self.evalpieceposition(PAI, position)
                        self.values[1][2] + self.evalattack([i, j])


                #连长
                elif temp==LIAN:
                    # 如果是红方
                    if board[i][j]==-LIAN:
                        # value加上该棋子的价值评估与位置评估
                        self.values[0][0]+=self.evalpiecevalue(LIAN)
                        position = [12 -i, 4 -j]
                        self.values[0][1] += self.evalpieceposition(LIAN, position)
                        self.values[0][2] += self.evalattack([12 - i, 4 - j])

                    # 如果是黑方
                    elif board[i][j]==LIAN:
                        # value加上该棋子的价值评估与位置评估
                        self.values[1][0]+=self.evalpiecevalue(LIAN)
                        position = [i, j]
                        self.values[1][1] += self.evalpieceposition(LIAN, position)
                        self.values[1][2] + self.evalattack([i, j])


                #营长
                elif temp==YING :
                    # 如果是红方
                    if board[i][j]==-YING:
                        # value加上该棋子的价值评估与位置评估
                        self.values[0][0]+=self.evalpiecevalue(YING)
                        position = [12 -i, 4 -j]
                        self.values[0][1] += self.evalpieceposition(YING, position)
                        self.values[0][2] += self.evalattack([12 - i, 4 - j])

                    # 如果是黑方
                    elif board[i][j] == YING:
                        # value加上该棋子的价值评估与位置评估
                        self.values[1][0]+=self.evalpiecevalue(YING)
                        position = [i, j]
                        self.values[1][1] += self.evalpieceposition(YING, position)
                        self.values[1][2] + self.evalattack([i, j])


                #团长
                elif temp==TUAN:
                    # 如果是红方
                    if board[i][j]==-TUAN:
                        # value加上该棋子的价值评估与位置评估
                        self.values[0][0]+=self.evalpiecevalue(TUAN)
                        position = [12 -i, 4 -j]
                        self.values[0][1] += self.evalpieceposition(TUAN, position)
                        self.values[0][2] += self.evalattack([12 - i, 4 - j])

                    # 如果是黑方
                    elif board[i][j] == TUAN:
                        # value加上该棋子的价值评估与位置评估
                        self.values[1][0]+=self.evalpiecevalue(TUAN)
                        position = [i, j]
                        self.values[1][1] += self.evalpieceposition(TUAN, position)
                        self.values[1][2] + self.evalattack([i, j])

                #旅长
                elif temp==LV:
                    # 如果是红方
                    if board[i][j]==-LV:
                        # value加上该棋子的价值评估与位置评估
                        self.values[0][0]+=self.evalpiecevalue(LV)
                        position = [12 -i, 4 -j]
                        self.values[0][1] += self.evalpieceposition(LV, position)
                        self.values[0][2] += self.evalattack([12 - i, 4 - j])

                    # 如果是黑方
                    elif board[i][j] == LV:
                        # value加上该棋子的价值评估与位置评估
                        self.values[1][0]+=self.evalpiecevalue(LV)
                        position = [i, j]
                        self.values[1][1] += self.evalpieceposition(LV, position)
                        self.values[1][2] + self.evalattack([i, j])

                #师长
                elif temp==SHI:
                    # 如果是红方
                    if board[i][j]==-SHI:
                        # value加上该棋子的价值评估与位置评估
                        self.values[0][0]+=self.evalpiecevalue(SHI)
                        position = [12 -i, 4 -j]
                        self.values[0][1] += self.evalpieceposition(SHI, position)
                        self.values[0][2] += self.evalattack([12 - i, 4 - j])
                    # 如果是黑方
                    elif board[i][j] == SHI:
                        # value加上该棋子的价值评估与位置评估
                        self.values[1][0]+=self.evalpiecevalue(SHI)
                        position = [i, j]
                        self.values[1][1] += self.evalpieceposition(SHI, position)
                        self.values[1][2] + self.evalattack([i, j])

                #军长
                elif temp==JUN:
                    # 如果是红方
                    if board[i][j] == -JUN:
                        # value加上该棋子的价值评估与位置评估
                        self.values[0][0]+=self.evalpiecevalue(JUN)
                        position = [12 -i, 4 -j]
                        self.values[0][1] += self.evalpieceposition(JUN, position)
                        self.values[0][2] += self.evalattack([12 - i, 4 - j])

                    # 如果是黑方
                    elif board[i][j] == JUN:
                        # value加上该棋子的价值评估与位置评估
                        self.values[1][0]+=self.evalpiecevalue(JUN)
                        position = [i, j]
                        self.values[1][1] += self.evalpieceposition(JUN, position)
                        self.values[1][2] + self.evalattack([i, j])


                # 司令
                elif temp == SI:
                    # 如果是红方
                    if board[i][j]==-SI:
                        # value加上该棋子的价值评估与位置评估
                        self.values[0][0] += self.evalpiecevalue(SI)
                        position = [12 -i, 4 -j]
                        self.values[0][1] += self.evalpieceposition(SI, position)
                        self.values[0][2] += self.evalattack([12 - i, 4 - j])

                    # 如果是黑方
                    elif board[i][j] == SI:
                        # value加上该棋子的价值评估与位置评估
                        self.values[1][0] += self.evalpiecevalue(SI)
                        position = [i, j]
                        self.values[1][1] += self.evalpieceposition(SI, position)
                        self.values[1][2] + self.evalattack([i, j])

        #分别计算红方与黑方的评估得分
        sumred=self.values[0][0]+self.values[0][1]/10+self.values[0][2]*6
        sumblack=self.values[1][0]+self.values[1][1]/10+self.values[1][2]*6

        ##print('sumred',sumred)
        #print('summblack',sumblack)

        #返回红方与黑方的得分差
        if player=='r':
            return sumred-sumblack
        elif player=='b':
            return sumblack-sumred


    def evalpiecevalue(self,piece):
        '''

        :param piece: int
        :return: piecevalue[piece]
        '''
        '''
        FLAG = 1  # 军旗/
        DI = 2  # 地雷
        ZHA = 3  # 炸弹
        GONG = 4  # 工兵
        PAI = 5  # 排长
        LIAN = 6  # 连长
        YING = 7  # 营长
        TUAN = 8  # 团长
        LV = 9  # 旅长
        SHI = 10  # 师长
        JUN = 11  # 军长
        SI = 12  # 司令
        按这个顺序给出各个piecevalue
        '''

        self.piecevalue=[10000000,400,1000,400,50,100,200,400,600,900,1400,2000]
        return  self.piecevalue[piece-1]


    def evalpieceposition(self,piece,pos):
        '''
        :param piece:
        :param pos:
        :return:
        '''
        #其效果一般，先暂时不用改方法评估
        '''
        self.positionlist=[]

        ZHA_position = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, self.piecevalue[ZHA - 1] + 300, 0, self.piecevalue[ZHA - 1] + 300, 0],
            [0, 0, self.piecevalue[ZHA - 1] + 100, 0, 0],
            [0, self.piecevalue[ZHA - 1] + 200, 0, self.piecevalue[ZHA - 1] + 200, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, self.piecevalue[ZHA - 1], 0, self.piecevalue[ZHA - 1], 0],
            [0, 0, self.piecevalue[ZHA - 1] - 200, 0, 0],
            [0, self.piecevalue[ZHA - 1], 0, self.piecevalue[ZHA - 1], 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.positionlist.append(ZHA_position)

        GONG_position = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, self.piecevalue[GONG - 1] + 300, 0, self.piecevalue[GONG - 1] + 300, 0],
            [0, 0, self.piecevalue[GONG - 1] + 100, 0, 0],
            [0, self.piecevalue[GONG - 1] + 200, 0, self.piecevalue[GONG - 1] + 200, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, self.piecevalue[GONG - 1], 0, self.piecevalue[GONG - 1], 0],
            [0, 0, self.piecevalue[GONG - 1] - 200, 0, 0],
            [0, self.piecevalue[GONG - 1], 0, self.piecevalue[GONG - 1], 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.positionlist.append(GONG_position)

        PAI_position = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, self.piecevalue[PAI - 1] + 300, 0, self.piecevalue[PAI - 1] + 300, 0],
            [0, 0, self.piecevalue[PAI - 1] + 100, 0, 0],
            [0, self.piecevalue[PAI - 1] + 200, 0, self.piecevalue[PAI - 1] + 200, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, self.piecevalue[PAI - 1], 0, self.piecevalue[PAI - 1], 0],
            [0, 0, self.piecevalue[PAI - 1] - 200, 0, 0],
            [0, self.piecevalue[PAI - 1], 0, self.piecevalue[PAI - 1], 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.positionlist.append(PAI_position)

        LIAN_position = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, self.piecevalue[LIAN - 1] + 300, 0, self.piecevalue[LIAN - 1] + 300, 0],
            [0, 0, self.piecevalue[LIAN - 1] + 100, 0, 0],
            [0, self.piecevalue[LIAN - 1] + 200, 0, self.piecevalue[LIAN - 1] + 200, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, self.piecevalue[LIAN - 1], 0, self.piecevalue[LIAN - 1], 0],
            [0, 0, self.piecevalue[LIAN - 1] - 200, 0, 0],
            [0, self.piecevalue[LIAN - 1], 0, self.piecevalue[LIAN - 1], 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.positionlist.append(LIAN_position)

        YING_position = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, self.piecevalue[YING-1] + 300, 0, self.piecevalue[YING-1] + 300, 0],
            [0, 0, self.piecevalue[YING-1] + 100, 0, 0],
            [0, self.piecevalue[YING-1] + 200, 0, self.piecevalue[YING-1] + 200, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, self.piecevalue[YING-1], 0, self.piecevalue[YING-1], 0],
            [0, 0, self.piecevalue[YING-1] - 200, 0, 0],
            [0, self.piecevalue[YING-1], 0, self.piecevalue[YING-1], 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.positionlist.append(YING_position)

        TUAN_position = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, self.piecevalue[TUAN - 1] + 300, 0, self.piecevalue[TUAN - 1] + 300, 0],
            [0, 0, self.piecevalue[TUAN - 1] + 100, 0, 0],
            [0, self.piecevalue[TUAN - 1] + 200, 0, self.piecevalue[TUAN - 1] + 200, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, self.piecevalue[TUAN - 1], 0, self.piecevalue[TUAN - 1], 0],
            [0, 0, self.piecevalue[TUAN - 1] - 200, 0, 0],
            [0, self.piecevalue[TUAN - 1], 0, self.piecevalue[TUAN - 1], 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.positionlist.append(TUAN_position)

        LV_position = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, self.piecevalue[LV - 1] + 300, 0, self.piecevalue[LV - 1] + 300, 0],
            [0, 0, self.piecevalue[LV - 1] + 100, 0, 0],
            [0, self.piecevalue[LV - 1] + 200, 0, self.piecevalue[LV - 1] + 200, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, self.piecevalue[LV - 1], 0, self.piecevalue[LV - 1], 0],
            [0, 0, self.piecevalue[LV - 1] - 200, 0, 0],
            [0, self.piecevalue[LV - 1], 0, self.piecevalue[LV - 1], 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.positionlist.append(LV_position)

        SHI_position = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, self.piecevalue[SHI - 1] + 300, 0, self.piecevalue[SHI - 1] + 300, 0],
            [0, 0, self.piecevalue[SHI - 1] + 100, 0, 0],
            [0, self.piecevalue[SHI - 1] + 200, 0, self.piecevalue[SHI - 1] + 200, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, self.piecevalue[SHI - 1], 0, self.piecevalue[SHI - 1], 0],
            [0, 0, self.piecevalue[SHI - 1] - 200, 0, 0],
            [0, self.piecevalue[SHI - 1], 0, self.piecevalue[SHI - 1], 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.positionlist.append(SHI_position)

        JUN_position = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, self.piecevalue[JUN - 1] + 300, 0, self.piecevalue[JUN - 1] + 300, 0],
            [0, 0, self.piecevalue[JUN - 1] + 100, 0, 0],
            [0, self.piecevalue[JUN - 1] + 200, 0, self.piecevalue[JUN - 1] + 200, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, self.piecevalue[JUN - 1], 0, self.piecevalue[JUN - 1], 0],
            [0, 0, self.piecevalue[JUN - 1] - 200, 0, 0],
            [0, self.piecevalue[JUN - 1], 0, self.piecevalue[JUN - 1], 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.positionlist.append(JUN_position)

        SI_position = np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, self.piecevalue[SI - 1] + 300, 0, self.piecevalue[SI - 1] + 300, 0],
            [0, 0, self.piecevalue[SI - 1] + 100, 0, 0],
            [0, self.piecevalue[SI - 1] + 200, 0, self.piecevalue[SI - 1] + 200, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, self.piecevalue[SI - 1], 0, self.piecevalue[SI - 1], 0],
            [0, 0, self.piecevalue[SI - 1] - 200, 0, 0],
            [0, self.piecevalue[SI - 1], 0, self.piecevalue[SI - 1], 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.positionlist.append(SI_position)

        array=self.positionlist[piece-3]

        #return array[pos[0]][pos[1]]
        '''

        return 0

    def evalattack(self,pos):
        #进攻矩阵，其可以引导棋子夺取敌方军旗
        attack=np.array([
            [70, 100, 70, 100, 70],
            [40, 70, 40, 70, 40],
            [20, 20, 15, 20, 20],
            [15, 15, 10, 15, 15],
            [10, 10, 10, 10, 10],
            [5, 5, 5, 5, 5],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])

        #攻击评估函数
        return attack[pos[0]][pos[1]]
