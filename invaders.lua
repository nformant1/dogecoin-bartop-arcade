--mame.exe -autoboot_script invaders.lua -window invaders.zip


local last_tick_time = -10
--local current_coins = 1

local cpu = manager.machine.devices[":maincpu"]
local mem = cpu.spaces["program"]
--print(mem:read_i8(0x20EB))
--mem:read_i8(0x20EB)
local current_coins = os.getenv("MAME_COINS")
local delay = 1
local count = 0

function tick()
	-- check if first run / tick
	if last_tick_time == -10 then
		--mem:write_i8(0x20EB, 0x0001);
		-- write $MAME_COINS env variable to credits memory address 
		mem:write_i8(0x20EB, tonumber(current_coins));
	end
	
	if emu.time() < last_tick_time + delay then
		return
	end
	last_tick_time = emu.time()
	
	
	local playing =	mem:read_u8(0x2011)
	print (playing)
	if playing == 128 then
		--print ("playing")
		--print (playing)
		local coins = mem:read_i8(0x20EB)
		if coins ~= current_coins then
			if coins == 0 then
				--print ("coins")
				--print (coins)
				count = count + 1
				
			end
			
		end 
	end
	if playing == 0 then
		delay = 5
	end
	
	if count >= 10 then
		manager.machine:exit()
	end
	
	current_coins = coins
end
	
emu.register_frame(tick)
