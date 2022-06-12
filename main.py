from game import RPC_Info, DogecoinGame, DogecoinGameMame
from config import rpcuser, rpcpassword, rpcport
from simple_term_menu import TerminalMenu
from pyfiglet import Figlet
import os

# RPC Info
rpc = RPC_Info(ip="127.0.0.1", port=rpcport, user=rpcuser, password=rpcpassword)

def main():
    """Main menu"""
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

    figlet = Figlet(font='slant')
    print(figlet.renderText("Dogecoin \n Bartop \n Arcade"))

    print("Choose a game!")
    options = ["Space Invaders (5 DOGE)", "Test Game (1 DOGE)"]
    terminal_menu = TerminalMenu(options)
    index = terminal_menu.show()

    if index == 0: space_invaders()
    if index == 1: print("Game not available")

def space_invaders(): 
    mameParams = ["-autoboot_script", "invaders.lua", "invaders.zip", "-skip_gameinfo"]  #"-window"
    invaders = DogecoinGameMame(name="Space Invaders", params=mameParams, rpc=rpc, cost=5)
    invaders.start()

    # When game ends, restart
    main()

if __name__ == '__main__':
    main()
