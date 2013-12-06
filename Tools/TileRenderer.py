#!/usr/bin/env python

import util
from canvas import Canvas

TILE_SIZE = 512

class TileRenderer:

	def __init__(self, canvas):
		pass

	def RenderTiles(self, output_xyz_image_sequences_dir):
		print "Rendering tiles..."
		
		self.grid_size = (canvas.size[0] / TILE_SIZE, canvas.size[1] / TILE_SIZE)
		print canvas.size
		print self.grid_size

		self.max_zoom = 0
		while pow(2, self.max_zoom) < max(self.grid_size):
			self.max_zoom = self.max_zoom + 1
		
		self.RenderBaseTiles()

	def RenderBaseTiles(self):
		print "Rendering base tiles with max zoom: " + str(self.max_zoom)
		for c in range(0, self.grid_size[0]):
			for r in range(0, self.grid_size[1]):
				
				left = c * TILE_SIZE
				right = left + TILE_SIZE
				top = r * TILE_SIZE
				bottom = top + TILE_SIZE
				pixel_bounds = (left, right, top, bottom)

				print "Rendering base tile " + str((c, r))
				print "Bounds: " + str(pixel_bounds)
				
				source_tiles = canvas.SourceTilesInBounds(pixel_bounds)

				print source_tiles

				print





if __name__ == '__main__':
	canvas = Canvas()
	canvas.CreateSimpleSourceLayout("source_video_tiles_sequences", (3, 14))
	renderer = TileRenderer(canvas)

	renderer.RenderTiles("xyz_tiles_sequences")