#!/usr/bin/env python3
"""
playground
"""

import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.event as event
import time
import math

# Main Minecraft connection object
mc = minecraft.Minecraft.create()

# Tell player which file is running and when it started running
mc.postToChat(__file__ + ' started: ' + \
  time.strftime('%H:%M:%S', time.gmtime()))

# Types of blocks we want to float over
water_list = [
  8, # WATER_FLOWING
  9, # WATER_STATIONARY
  79, # ICE
]

while(True):
  x, y, z = mc.player.getPos()
  block_under_player = mc.getBlock(x, y-1, z)

  if block_under_player in water_list:
    mc.setBlocks(x-1, y-1, z-1,
                 x+1, y-1, z+1,
                 block.ICE)
    mc.setBlock(x, y, z, block.SNOW)

  time.sleep(0.1)
