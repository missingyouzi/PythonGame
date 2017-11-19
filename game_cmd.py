import cmd
from ui import *
import data
import logic
import argparse as ap

class Game_cmd(cmd.Cmd):
    intro = "Enter a command: new , resume, quit. Type 'Help' or '?' for help "
    game = ""
    prompt = "(oxo)"

    def do_new(self, arg):
        self.game = logic.newGame()
        ui.playGame(self.game)

    def do_restore(self, arg):
        self.game = logic.restoreGame()
        ui.playGame(self.game)

    def do_quit(self, arg):
        print("Good Bye...")
        raise SystemExit

def main():
    p = ap.ArgumentParser(description="Play a game of Tic-Tac-Toe")
    grp = p.add_mutually_exclusive_group()
    grp.add_argument("-n", "--new", action='store_true', help="start new game")
    grp.add_argument("-r", "--res", "--restore", action="store_true", help="restore old game")
    args = p.parse_args()
    if args.new:
        executeChoice(1)
    elif args.res:
        executeChoice(2)
    else:
        while True:
            choice = getMenuChoice(menu)
            executeChoice(choice)

if __name__ == '__main__':
    main()
