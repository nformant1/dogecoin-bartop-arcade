from rpc_connection import RPC_Connection
import time
import subprocess
import qrcode
import os

# we need math for the fee calculation
# we need time to sleep (wait for next block)
# rpc_connection wraps our calls nicely

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    # I assume the node runs local (127.0.0.1)
    # This should match your dogecoin.conf
    testnet = 1  # optional if "dogecoin-qt.texe -testnet" is used
    server = 1
    rpcuser = "YOUR_RPC_USER"
    rpcpassword = "YOUR_RPC_PASSWORD"
    rpcport = 44555

    # port standard values if not defined
    # use them or dont assign those variables at all
    # rpcport = 44555
    # port = 44556
    # my non standard ports for merged mining (uncomment to use them)
    # End of dogecoin.conf

    # set MAME_PATH=C:\Users\nformant\Downloads\mame\
    path = os.getenv("MAME_PATH", None)
    if not path:
        raise RuntimeError("You need to set MAME_PATH (path to mame binary)")

    # binaryPath = os.path.join(path, "mame")
    mameParams = ["-autoboot_script", "invaders.lua", "invaders.zip", "-skip_gameinfo"]  #"-window"

    rpc = RPC_Connection(rpcuser, rpcpassword, "127.0.0.1", rpcport)
    # Get List of UTXOs
    #data = {}
    newaddress = rpc.command("getnewaddress")
    #print (newaddress)
    getbalance = 0
    # Creating an instance of qrcode
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(newaddress)
    qr.make(fit=True)
    #img = qr.make_image(fill='black', back_color='white')

    #f = io.StringIO()
    #qr.print_ascii(out=f)

    print (' ______ _               _____                                                  ')
    print (' | ___ \ |             /  ___|                                                 ')
    print (' | |_/ / | __ _ _   _  \ `--. _ __   __ _  ___ ___         ____                ')
    print (' |  __/| |/ _` | | | |  `--. \ \'_ \ / _` |/ __/ _ \       /___/\_              ')
    print (' | |   | | (_| | |_| | /\__/ / |_) | (_| | (_|  __/      _\   \/_/\__          ')
    print (' \_|   |_|\__,_|\__, | \____/| .__/ \__,_|\___\___|    __\       \/_/\         ')
    print ('                 __/ |       | |                       \   __    __ \ \        ')
    print ('  _____         |___/      _ |_|                      __\  \_\   \_\ \ \  __  ')
    print (' |_   _|                  | |                        /_/\\   __   __  \ \_/_/\ ')
    print ('   | | _ ____   ____ _  __| | ___ _ __ ___           \_\/_\__\/\__\/\__\/_\_\/ ')
    print ('   | || \'_ \ \ / / _` |/ _` |/ _ \ \'__/ __|             \_\/_/\       /_\_\/   ')
    print ('  _| || | | \ V / (_| | (_| |  __/ |  \__ \                \_\/       \_\/     ')
    print ('  \___/_| |_|\_/ \__,_|\__,_|\___|_|  |___/                                    ')
    print ('                                                                               ')
    print ('                                                                               ')
    print ('                                                                               ')
    
    print (' >>>>>>>>>>>> ' +newaddress+ ' <<<<<<<<<<< ')
    qr.print_ascii()
    
    print ('                                                                               ')
    print ('                                                                               ')
    print (' _______                 __   ______   _____                            ')
    print ('|     __|.-----.-----.--|  | |    __| |     \.-----.-----.-----.-----.  ')
    print ('|__     ||  -__|     |  _  | |__    | |  --  |  _  |  _  |  -__|__ --|  ')
    print ('|_______||_____|__|__|_____| |______| |_____/|_____|___  |_____|_____|  ')
    print ('                                                   |_____|              ')
    print ('  ___               ____     _______                                    ')
    print ('.\'  _|.-----.----. |_   |   |     __|.---.-.--------.-----.             ')
    print ('|   _||  _  |   _|  _|  |_  |    |  ||  _  |        |  -__|             ')
    print ('|__|  |_____|__|   |______| |_______||___._|__|__|__|_____|             ')
    print ('                                                                        ')

    balance = 0
    while(balance < 5):
        rbf = False
        listunspent = rpc.command("listunspent", params=[0, 99999, [newaddress]])  # RBF sec. issue
        if listunspent:
            balance = 0    
            for tx in listunspent:
                rawtx = rpc.command("getrawtransaction", params=[tx['txid']])  # RBF sec. issue
                decodedtx = rpc.command("decoderawtransaction", params=[rawtx])
                for _input in decodedtx["vin"]:
                    if _input["sequence"] != 4294967295:
                        rbf = True
                balance += tx["amount"]
            if rbf: 
                break
            os.environ["MAME_COINS"] = str(hex(int(balance / 5)))


        time.sleep(5)
    sp = subprocess.Popen([os.path.join(path,"mame"), *mameParams],
                         cwd = path,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         universal_newlines=True,
                         bufsize=0)

    sp.communicate()


if __name__ == '__main__':
    while (True):
        main()








