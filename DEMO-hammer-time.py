#!/usr/bin/env python3
"""
Turn the sword into a tinker's hammer.
Radius adjustable.
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

tool_radius = 2

# Loop forever
while(True):
  for hit in mc.events.pollBlockHits():
    hit_block_type = mc.getBlock(hit.pos.x, hit.pos.y, hit.pos.z)

    if hit.face == block_faces['top'] or hit.face == block_faces['bottom']:
      mc.setBlocks(hit.pos.x-tool_radius, hit.pos.y, hit.pos.z-tool_radius, \
                   hit.pos.x+tool_radius, hit.pos.y, hit.pos.z+tool_radius, \
                   block.AIR)

    if hit.face == block_faces['east'] or hit.face == block_faces['west']:
      mc.setBlocks(hit.pos.x, hit.pos.y-tool_radius, hit.pos.z-tool_radius, \
                   hit.pos.x, hit.pos.y+tool_radius, hit.pos.z+tool_radius, \
                   block.AIR)

    if hit.face == block_faces['north'] or hit.face == block_faces['south']:
      mc.setBlocks(hit.pos.x-tool_radius, hit.pos.y-tool_radius, hit.pos.z, \
                   hit.pos.x+tool_radius, hit.pos.y+tool_radius, hit.pos.z, \
                   block.AIR)

  time.sleep(0.1)
