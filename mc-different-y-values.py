#!/usr/bin/env python3
"""
This program shows that MCPiAPI's idea of Y:0 is different than Minecraft's
idea of Y:0.

This program thinks that "zero" is sea-level plus 1. Real, in-game Y value is
64.

So, according to mcpi, "sea level" is Y:-1, and in-game Y:0 is y == -64 here.
"""

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# Main Minecraft connection object
mc = minecraft.Minecraft.create()
mc.postToChat('started: ' + time.strftime('%H:%M:%S', time.gmtime()))

lasty = 99999

# Get player position
while(True):
  x, y, z = mc.player.getPos()
  if lasty != y:
    mc.postToChat(y)
  lasty = y
  time.sleep(0.1)
