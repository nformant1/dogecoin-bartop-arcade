# :space_invader: Dogecoin Bartop Arcade
Collection of scripts to run a Dogecoin Bartop Arcade

## Configurations
you need to change this in main.py

```python
rpcuser = "YOUR_RPC_USER"
rpcpassword = "YOUR_RPC_PASSWORD"
```

and you need to setup the credentials in dogecoin.conf
```
rpcuser=YOUR_RPC_USER
rpcpassword=YOUR_RPC_PASSWORD
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
