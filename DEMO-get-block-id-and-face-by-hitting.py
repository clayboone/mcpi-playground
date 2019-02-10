#!/usr/bin/env python3
"""
Turns out that there's only 2 different ID's of wood.. \\.:)./
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

# Loop forever
while(True):
  for hit in mc.events.pollBlockHits():
    mc.postToChat('You {} an ID-{} block on the {} side'.format( \
      'hit' if hit.type is event.BlockEvent.HIT else 'something\'d',
      mc.getBlock(hit.pos.x, hit.pos.y, hit.pos.z),
      block_faces[hit.face]
    ))


  time.sleep(0.1)
