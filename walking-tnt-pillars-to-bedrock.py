#!/usr/bin/env python3
"""
Create a pillar of TNT blocks from bedrock to the player's feet, as long as
he's not jumping or flying.
"""

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

blocks = {
  # "slimeBlock": 165 # slime blocks don't exist in 1.7.10.. only 1.8
}

# Main Minecraft connection object
mc = minecraft.Minecraft.create()
mc.postToChat('started: ' + time.strftime('%H:%M:%S', time.gmtime()))

# Get player position
while(True):
  x, y, z = mc.player.getPos()
  blockUnderPlayer = mc.getBlock(x, y - 1, z)
  if (blockUnderPlayer > 0):
    for current_y in range(-60, int(y)):
      mc.setBlock(x, current_y, z, block.TNT)
  time.sleep(0.25)
