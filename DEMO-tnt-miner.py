#!/usr/bin/env python3
"""
Create a pillar of TNT blocks from bedrock to the player's feet, as long as
he's not jumping or flying.
"""

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# Main Minecraft connection object
mc = minecraft.Minecraft.create()
mc.postToChat('started: ' + time.strftime('%H:%M:%S', time.gmtime()))

# Set sentinel values for last_player_*
last_player_x = False
last_player_y = False
last_player_z = False

while(True):
  # Get player position and the ID of the block under the player
  exact_player_x, exact_player_y, exact_player_z = mc.player.getPos()

  # Round to the nearest whole number (except y)
  player_x = int(round(exact_player_x))
  player_y = int(round(exact_player_y))
  player_z = int(round(exact_player_z))

  # Only run if we're in a new block (this takes a while to run)
  if False or \
    not player_x == last_player_x or \
    not player_y == last_player_y or \
    not player_z == last_player_z:

    blockUnderPlayer = mc.getBlock(player_x, player_y - 1, player_z)

    # Don't do anything if we're flying/jumping
    if blockUnderPlayer > 0:

      # Loop through the blocks under the player, starting at the block under the
      # player's feet and going towards negative y (downward)
      for y in range(int(player_y) - 1, int(player_y) - 25, -1):
        # Stop at bedrock
        if y < -60:
          continue

        #Skip air blocks
        if mc.getBlock(player_x, y, player_z) <= 0:
          continue

        # Since we haven't continued yet, set the block to TNT
        mc.setBlock(player_x, y, player_z, block.TNT)

      # Save rounded player position for next iteration (optimization)
      last_player_x = player_x
      last_player_y = player_y
      last_player_z = player_z

  else:
    time.sleep(0.1)
