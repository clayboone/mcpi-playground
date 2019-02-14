#!/usr/bin/env python3
"""
Play around :)
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

block_faces = {
  'bottom': 0,
  'top': 1,
  'north': 2,
  'south': 3,
  'west': 4,
  'east': 5,
  0: 'bottom',
  1: 'top',
  2: 'north',
  3: 'south',
  4: 'west',
  5: 'east'
}

tool_width = 3
tool_height = 10
tool_depth = 10

replacement_block = block.LAVA
# replacement_block = block.GLASS

wood_ids = [17, 162]

def find_wood_in(x, y, z, x2, y2, z2):
  """Find wood blocks touching a cuboid"""
  found_wood_blocks = []

  start_x = x if x < x2 else x2
  end_x = x2+1 if x < x2 else x+1

  start_y = y if y < y2 else y2
  end_y = y2+1 if y < y2 else y+1

  start_z = z if z < z2 else z2
  end_z = z2+1 if z < z2 else z+1


  for xi in range(start_x, end_x):
    for yi in range(start_y, end_y):
      for zi in range(start_z, end_z):
        if mc.getBlock(xi, yi, zi) in wood_ids:
          found_wood_blocks.append((xi, yi, zi))

  return found_wood_blocks

# Loop forever
while(True):
  for hit in mc.events.pollBlockHits():
    block_id = mc.getBlock(hit.pos.x, hit.pos.y, hit.pos.z)
    if block_id in wood_ids:
      if hit.face == block_faces['east']:
        mc.postToChat('Searching eastward...')
        wood_blocks = find_wood_in(hit.pos.x,
                                   hit.pos.y,
                                   hit.pos.z-tool_width,

                                   hit.pos.x-tool_depth,
                                   hit.pos.y+tool_height,
                                   hit.pos.z+tool_width)
      elif hit.face == block_faces['west']:
        mc.postToChat('Searching westward...')
        wood_blocks = find_wood_in(hit.pos.x,
                                   hit.pos.y,
                                   hit.pos.z-tool_width,

                                   hit.pos.x+tool_depth,
                                   hit.pos.y+tool_height,
                                   hit.pos.z+tool_width)
      elif hit.face == block_faces['south']:
        mc.postToChat('Searching southward...')
        wood_blocks = find_wood_in(hit.pos.x-tool_width,
                                   hit.pos.y,
                                   hit.pos.z,

                                   hit.pos.x+tool_width,
                                   hit.pos.y+tool_height,
                                   hit.pos.z-tool_depth)
      elif hit.face == block_faces['north']:
        mc.postToChat('Searching northward...')
        wood_blocks = find_wood_in(hit.pos.x-tool_width,
                                   hit.pos.y,
                                   hit.pos.z,

                                   hit.pos.x+tool_width,
                                   hit.pos.y+tool_height,
                                   hit.pos.z+tool_depth)
      else:
        mc.postToChat('Hit on the side to start searching!')
        break

      if len(wood_blocks) > 0:
        mc.postToChat('Removing {} wood blocks.'.format(len(wood_blocks)))

      while len(wood_blocks) > 0:
        bx, by, bz = wood_blocks.pop(0)
        mc.setBlock(bx, by, bz, replacement_block)



  time.sleep(0.1)
