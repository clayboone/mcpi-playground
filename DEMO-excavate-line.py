#!/usr/bin/env python3
"""
Play around :)
"""

import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.event as event
import time

# Main Minecraft connection object
mc = minecraft.Minecraft.create()

# Tell player which file is running and when it started running
mc.postToChat(__file__ + ' started: ' + \
  time.strftime('%H:%M:%S', time.gmtime()))

# Block event faces
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

# Tool length
tool_length = 10

def set_air_block(block_type_to_change, x, y, z):
  """
  Set block at x, y, z to be an air block.

  Don't replace spawner blocks
  Don't set any blocks below Y=4 (in-game)
  Only change blocks that are the same type as `block_type_to_change`
  """
  if mc.getBlock(x, y, z) == 52 or y < -60 or \
    mc.getBlock(x, y, z) != block_type_to_change:
    return
  else:
    mc.setBlock(x, y, z, 0)

# Loop forever
while(True):
  for hit in mc.events.pollBlockHits():
    hit_block_type = mc.getBlock(hit.pos.x, hit.pos.y, hit.pos.z)

    if hit.face == block_faces['north']:
      for i in range(hit.pos.z, hit.pos.z + tool_length, 1):
        set_air_block(hit_block_type, hit.pos.x, hit.pos.y, i)

    if hit.face == block_faces['south']:
      for i in range(hit.pos.z, hit.pos.z - tool_length, -1):
        set_air_block(hit_block_type, hit.pos.x, hit.pos.y, i)

    if hit.face == block_faces['east']:
      for i in range(hit.pos.x, hit.pos.x - tool_length, -1):
        set_air_block(hit_block_type, i, hit.pos.y, hit.pos.z)

    if hit.face == block_faces['west']:
      for i in range(hit.pos.x, hit.pos.x + tool_length, 1):
        set_air_block(hit_block_type, i, hit.pos.y, hit.pos.z)

    if hit.face == block_faces['top']:
      for i in range(hit.pos.y, hit.pos.y - tool_length, -1):
        set_air_block(hit_block_type, hit.pos.x, i, hit.pos.z)

    if hit.face == block_faces['bottom']:
      for i in range(hit.pos.y, hit.pos.y + tool_length, 1):
        set_air_block(hit_block_type, hit.pos.x, i, hit.pos.z)

  time.sleep(0.1)
