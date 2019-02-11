#!/usr/bin/env python3
"""
Walking near water should turn it to lava
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

# Larger radius increases delay before any output.
player_radius = 10

last_x = False
last_y = False
last_z = False

water_block_list = []

def find_water_around_block(x, y, z):
  """Recursively search for water around block"""
  passed_block = mc.getBlock(x, y, z)

  if passed_block == 8 or passed_block == 9:
    water_block_list.append((x, y, z))
    mc.postToChat('len water_block_list = {}'.format(len(water_block_list)))

    for xi in range(x-1, x+1):
      for yi in range(y-1, y+1):
        for zi in range(z-1, z+1):
          if xi == x or yi == y or zi == z:
            continue
          find_water_around_block(xi, yi, zi)

  else:
    # This block is not water, stop searching.
    pass

# Loop forever
while(True):
  exact_x, exact_y, exact_z = mc.player.getPos()
  x, y, z = math.floor(exact_x), math.floor(exact_y), math.floor(exact_z)
  block_under_player = mc.getBlock(x, y-1, z)

  if x != last_x or y != last_y or z != last_z:
    for xi in range(x-player_radius, x+player_radius+1):
      for zi in range(z-player_radius, z+player_radius+1):
        find_water_around_block(xi, y-1, zi)

    # Set all found water blocks to air before changing to lava (prevents
    # obsidian generation)
    for block_x, block_y, block_z in water_block_list:
      mc.setBlock(block_x, block_y, block_z, 0)

    # Wait for water to go away (probably increase this OR set it based on len
    # of water_block_list)
    time.sleep(4)

    # Then set the old air blocks to lava
    while len(water_block_list) > 0:
      block_x, block_y, block_z = water_block_list.pop(0)
      mc.setBlock(block_x, block_y, block_z, block.LAVA)


    last_x = x
    last_y = y
    last_z = z

  time.sleep(0.1)
