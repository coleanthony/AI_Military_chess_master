## 军棋AI对战、人机对战、人人对战
### 1. 说明

军棋AI

### 2. 环境

经测试在Windows10下的Python3.7环境可用，使用`pip install -r requirement.txt`安装所需Python环境。

### 3. 快速上手

进入代码目录，在终端下运行 `python run.py -r "demo.exe --role -1" -b "demo.exe"`

参数说明：
* `run.py`
    * `-b`：黑方的AI引擎的启动指令设置（不使用该参数来手动进行控制，下同）
    * `-r`：红方的AI引擎的启动指令设置
    * `-i`：初始化棋盘，使用NCN方式表示
    * `-l`：使用更大的界面
    * `-c`：从某一回合开始

* `demo.exe`
    * `-role`：算法的角色，默认为`1`，为黑方;`-1`为红方


