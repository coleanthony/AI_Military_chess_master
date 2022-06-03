"""
 * The timer.
"""
import time
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A timer.")
    parser.add_argument('--time', dest='tm', type=int, default=60, help="Time limited.")
    parser = parser.parse_args()
    # 从命令行中获取计时数
    tm = int(parser.tm)
    # 通过子进程进程睡眠完成计时
    time.sleep(tm)
