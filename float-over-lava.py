#!/usr/bin/env python3
"""
Unfortunately, relative positions aren't possible in mcpi, we can use another
one of these Python mods (picraft) to set vectors and set only y that way, but
not with mcpi alone.

https://picraft.readthedocs.io/en/release-0.6/conversion.html#minecraft-player-gettilepos
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
float_over_ids = [
  10, # LAVA_FLOWING
  11, # LAVA_STATIONARY
]

while(True):
  x, y, z = mc.player.getPos()
  block_under_player = mc.getBlock(x, y-1, z)

  if block_under_player in float_over_ids:
    mc.player.setPos(x, y, z)

  time.sleep(0.1)
