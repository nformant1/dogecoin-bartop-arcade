from rpc_connection import RPC_Connection
import time
import subprocess
import qrcode
from pyfiglet import Figlet
import os

class RPC_Info:
    """A class used to represent RPC info"""
    def __init__(self, ip: str, port: int, user: str, password: str):
        self.ip = ip 
        self.port = port 
        self.user = user
        self.password = password

class DogecoinGame:
    """
    A class used to represent a Dogecoin game

    Attributes
    ----------
    name : str
        name of game
    bin : str
        string to binary (ex. /usr/bin/mame)
    path : str
        path of binary (ex. /usr/bin)
    params : str
        params to use when launching bin
    rpc : RPC_Info
        rpc info
    cost : float
        cost of game in dogecoin

    Methods
    -------
    start()
        Display screen to start game
    """
    def __init__(self, name: str, bin: str, path: str, params: str, rpc: RPC_Info, cost: float):
        self.name = name
        self.bin = bin
        self.path = path
        self.params = params
        self.rpc = rpc
        self.cost = cost
        self.figlet = Figlet()

    def start(self):
        """Display screen to start game"""
        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # Set up RPC Connection
        rpc = RPC_Connection(self.rpc.user, self.rpc.password, self.rpc.ip, self.rpc.port)

        # Get new address
        newaddress = rpc.command("getnewaddress")

        # Creating an instance of qrcode
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
        qr.add_data(newaddress)
        qr.make(fit=True)

        print(self.figlet.renderText(f"Play {self.name}"))
        
        print (' >>>>>>>>>>>> ' +newaddress+ ' <<<<<<<<<<< ')
        qr.print_ascii()
        
        print(self.figlet.renderText(f"Send {str(self.cost)} DOGE"))
        print(self.figlet.renderText("For 1 Game"))

        balance = 0
        while(balance < self.cost):
            print(f" >>>>>>>>>>>> {balance}/{self.cost} DOGE sent <<<<<<<<<<< ", end='\r')
            rbf = False
            listunspent = rpc.command("listunspent", params=[0, 99999, [newaddress]])  # RBF sec. issue
            if listunspent:
                balance = 0    
                for tx in listunspent:
                    rawtx = rpc.command("getrawtransaction", params=[tx['txid']])  # RBF sec. issue
                    decodedtx = rpc.command("decoderawtransaction", params=[rawtx])
                    for _input in decodedtx["vin"]:
                        if _input["sequence"] < 4294967294: # regtest returns 4294967294, not 4294967295 (0xFFFFFFFF)
                            rbf = True
                    balance += tx["amount"]
                if rbf: 
                    raise RuntimeError("RBF is not supported.")
                os.environ["MAME_COINS"] = str(hex(int(balance / 5)))

            time.sleep(5)

        sp = subprocess.Popen([self.bin, *self.params],
                            cwd = self.path,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True,
                            bufsize=0)

        sp.communicate()

class DogecoinGameMame(DogecoinGame):
    """A class used to represent a Dogecoin game using MAME"""
    def __init__(self, name, params, rpc, cost):
        path = os.getenv("MAME_PATH", None)
        if not path and os.name == 'nt':
            raise RuntimeError("You need to set MAME_PATH (path to mame binary)")
        else:
            path = '/usr/bin' # UNIX-based

        binary = os.path.join(path, "mame")
        
        super().__init__(name, binary, path, params, rpc, cost)
