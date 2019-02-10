#!/usr/bin/env python3
"""
summoning stuff is really wrong.. the math is way off..
summoning lightning doesn't work until 1.8 anyways :(
can't set spawners until 1.8...
can't issue command block commands from mcpi...
this is pretty limited...
"""

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# Main Minecraft connection object
mc = minecraft.Minecraft.create()
mc.postToChat('started: ' + time.strftime('%H:%M:%S', time.gmtime()))

# Get player position
while(True):
  x, y, z = mc.player.getPos()
  mc.postToChat('summon Zombie ~ ~ ~')
  time.sleep(1)
