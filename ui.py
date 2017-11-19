import logic

# 菜单
menu = ["Start new game", "Resume saved game", "Display help", "Quit"]

# 获取菜单选项
def getMenuChoice(aMenu):
    # 抛出异常
    if not aMenu:
        raise ValueError('No menu named ', aMenu)
    # 接受用户的选项
    while True:
        print("\n\n")
        # enumerate是枚举变量, start=1代表是从1开始
        for index, item in enumerate(aMenu, start=1):
            print(index, '\t', item)
        try:
            choice = int(input("\nChoose a menu option: "))
            if 1 <= choice <= len(aMenu):
                return choice
            else:
                print("Choose a number between 1 and ", len(aMenu))
        # 如果用户输入一个异常字符,抛出值异常,并提示重新输入选项
        except ValueError:
            print("Choose the number of a menu option:")

def startGame():
    return logic.newGame()

def resumeGame():
    return logic.restoreGame()

def displayHelp():
    print('''
    Start new game: start a new game
    resume saved game: restore the last saved game
    display help: show this page
    Quit: quits this application
    ''')

def quit():
    print("Good Bye...")
    raise SystemExit

# 根据不同的选项调用不同的函数,可以使用多个if/else实现,但是此处采用了一个分派表[列表]来实现
def executeChoice(choice):
    dispatch = [startGame, resumeGame, displayHelp, quit]
    game = dispatch[choice - 1]()
    if game:
        playGame(game)

# 打印当前棋盘
def printGame(game):
    display = '''
    1 | 2 | 3       {} | {} | {}
    ---------       ------------
    4 | 5 | 6       {} | {} | {}
    ---------       ------------
    7 | 8 | 9       {} | {} | {}
    '''
    print(display.format(*game))

def playGame(game):
    # 初始化result为一个字符串
    result = ""
    # 当游戏尚未结束时,循环监听游戏状态
    while not result:
        # 打印当前游戏状态的地图
        printGame(game)
        # 获取用户下的地方
        choice = input("Cell[1-9] or q to quit :")
        # 如果输入q代表退出
        if choice.lower()[0] == 'q':
            # 询问是否保存
            save_or = input("Save game before quitting?[y/n]")
            if save_or.lower()[0] == 'y':
                logic.saveGame(game)
            quit()
        else:
            try:
                cell = int(choice) - 1
                if not (0 <= cell <= 8):
                    raise ValueError
            except ValueError:
                print("Choose a number between 1 and 9 or 'q' to quit")
                continue

            try:
                result = logic.userMove(game, cell)
            except ValueError:
                print("Chosee an empty cell")
                continue
            if not result:
                result = logic.computerMove(game)
            if not result:
                continue
            # 平局
            elif result == 'D':
                printGame(game)
                print("It's a  draw")
            # 游戏结束
            else:
                printGame(game)
                print("Winner is ", result, "\n")

def main():
    # 测试异常能否正常显示
    # getMenuChoice([])
    choice = getMenuChoice(menu)
    executeChoice(choice)

if __name__ == '__main__':
    main()
