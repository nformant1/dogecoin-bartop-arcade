# :space_invader: Dogecoin Bartop Arcade
Collection of scripts to run a Dogecoin Bartop Arcade

## Dependencies
Run
```bash
pip install -r requirements.txt 
```

## Configurations
You need to change this in config.py:

```python
rpcuser = "YOUR_RPC_USER"
rpcpassword = "YOUR_RPC_PASSWORD"
rpcport = XXXX
```

and you need to setup the credentials in dogecoin.conf
```
server=1
rpcuser=YOUR_RPC_USER
rpcpassword=YOUR_RPC_PASSWORD
rpcport=XXXX
```

## Set enviroment variable

UNIX
```
export MAME_PATH=/path/to/mame/
```

Windows
```
set MAME_PATH=C:\path\to\mame\
```

## LUA Credit
LUA script credits to https://github.com/Centurix/mamestate/blob/master/states/invaders.lua

## ROM
You will need the game "invaders.zip"  in your `roms/` dir
