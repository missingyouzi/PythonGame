import os.path
game_file = '.game.dat'

# 使用os模块试图得到用户的主目录,如果失败就使用当前目录,前下划线代表不希望被调用者使用,在java中累死 private 修饰符
def _getpath():
    try:
        # os.environ['HOMEPATH'] => windows下的用户主目录
        # os.environ['HOME'] => 非windows下的用户主目录
        game_path = os.environ['HOMEPATH'] or os.environ['HOME']
        # 如果主目录不存在, 就使用当前文件目录
        if not os.path.exists(game_path):
            game_path = os.getcwd()
    # 抛出异常
    except (KeyError, TypeErro):
        game_path = os.getcwd()
    return game_path

# 创建一个包含表示游戏的字符串的新文件
def saveGame(game):
    path = os.path.join(_getpath(), game_file)
    with open(path, 'w') as gf:
        gamestr = ''.join(game)
        gf.write(gamestr)

# 使用 _getpath() 定位到被保存的文件并打开它,读取保存的游戏数据
def restoreGame():
    path = os.path.join(_getpath(), game_file)
    with open(path, 'r') as gf:
        gamestr = gf.read()
        return list(gamestr)

# 单元测试
def test():
    print("path = ", _getpath())
    saveGame(list("XO XO OX"))
    print(restoreGame())

if __name__ == '__main__':
    test()
