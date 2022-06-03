from algorithm.searchmodel import *
from common import *
import util
import argparse
import sys

# 本引擎的AI模型
AI = None


# 由AI模型做出最佳着法
def make_decision(ncn):
    data, cnt, total_cnt = util.parse_ncn(ncn)
    best_move = AI.search(data, cnt)
    move = [best_move.from_where, best_move.to_where]
    return util.move_to_ncn(move)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="An AI engine.")
    parser.add_argument('--role', dest='role', type=int, default=1, help="Role of AI.")
    parser.add_argument('--time', dest='time', type=int, default=60, help="Time limited.")
    parser = parser.parse_args()

    # 当前AI对应的角色，1为黑方，-1为红方
    player = parser.role
    # 下棋时间限制，默认为60秒
    time = parser.time
    # 建立相应的AI模型
    AI = SearchModel(player=player, time=time)

    print("ready")
    sys.stdout.flush()
    while True:
        cmd = input()
        if cmd == CMD_QUIT:
            break
        if cmd.startswith(CMD_INIT):
            continue
        decision = make_decision(cmd)
        print(decision)
        sys.stdout.flush()
