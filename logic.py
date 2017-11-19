import os
import random
# 导入自己写的数据操作模块
import data

# 游戏模型为 tic-tac-toe ,即井字棋


# 创建一个拥有 9 个空格的新列表
def newGame():
    return list(" " * 9)

# 使用 data.py 中的 savegame() 函数保存当前游戏文件
def saveGame(game):
    data.saveGame(game)

# 恢复游戏
def restoreGame():
    try:
        # 调用 data.py 中的 restoreGame() 函数来恢复游戏
        game = data.restoreGame()
        # 确认已保存游戏的长度,如果长度等于9继续
        if len(game) == 9:
            return game
        # 否则,重新创建游戏
        else:
            return newGame()
    # 当无法找到游戏文件时,重新创建游戏
    except IOError:
        return newGame()

# 寻找当前游戏中没有被使用的格子,然后随机选择一个格子来防止计算机的移动,算法有待改进
def _generateMove(game):
    options = [i for i in range(len(game)) if game[i] == " "]
    # 是一种 pythonic 的写法,与以下等价,
    # options = []
    # for i in range(len(game)):
    #     if game[i] == " ":
    #         options.append(i)
    return random.choice(options)

# 判断游戏是否结束,这里采用一个非常简单且依赖于一个事实:只有8个可能的获胜路线
def _isWinningMove(game):
    wins = ((0, 1, 2),(3, 4, 5),(6, 7, 8),(0, 3, 6),(1, 4, 7),(2, 5, 8),(0, 4, 8),(2, 4, 6))
    # 这是判断游戏状态的一种方法
    for a, b, c in wins:
        # 注意是字符串相加
        chars = game[a] + game[b] + game[c]
        # 如果出现 XXX 或者 OOO 则游戏结束
        if chars == 'XXX' or chars == 'OOO':
            return True
    return False

# 玩家移动
def userMove(game, cell):
    # 出现空格字符则表示出现错误
    if game[cell] != ' ':
        raise ValueError('Invaild Cell')
    # 否则将此处变成X
    else:
        game[cell] = 'X'
    # 判断游戏是否结束
    if _isWinningMove(game):
        return 'X'
    else:
        return ''

# 电脑移动
def computerMove(game):
    cell = _generateMove(game)
    # 如果找不到地方下了,返回平局
    if cell == -1:
        return 'D'
    # 否则此处变成O
    game[cell] = 'O'
    # 判断游戏是否结束
    if _isWinningMove(game):
        return 'O'
    else:
        return ''

# 测试函数
def test():
    result = ''
    # 载入游戏
    game = newGame()
    # 当result为空的时候进入循环
    while not result:
        # 打印当前游戏地图
        print(game)
        try:
            # 此处玩家随机下
            result = userMove(game, _generateMove(game))
        # 抛出值异常
        except ValueError:
            print("Oops, errors happened")
        if not result:
            result = computerMove(game)

        if not result:
            continue
        # 平局
        elif result == 'D':
            print('Its a draw')
        else:
            print('Winner is: ', result)
        print(game)

if __name__ == '__main__':
    test()
