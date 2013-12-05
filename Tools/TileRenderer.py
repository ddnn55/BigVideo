#!/usr/bin/env python

import util
from canvas import Canvas

TILE_SIZE = 512

class TileRenderer:

	def __init__(self, canvas):
		pass

	def RenderTiles(self, output_xyz_image_sequences_dir):
		print "Rendering tiles..."
		
		grid_size = (canvas.size[0] / TILE_SIZE, canvas.size[1] / TILE_SIZE)
		print canvas.size
		print grid_size

		max_zoom = 0
		while pow(2, max_zoom) < max(grid_size):
			max_zoom = max_zoom + 1

		print max_zoom

if __name__ == '__main__':
	canvas = Canvas()
	canvas.CreateSimpleSourceLayout("source_video_tiles_sequences", (3, 14))
	renderer = TileRenderer(canvas)

	renderer.RenderTiles("xyz_tiles_sequences")