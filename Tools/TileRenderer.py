#!/usr/bin/env python

import util
from canvas import Canvas
from geometry import Rect, Point
from PIL import Image

TILE_SIZE = 512

class TileRenderer:

	def __init__(self, canvas):
		pass

	def RenderTiles(self, output_xyz_image_sequences_dir):
		print "Rendering tiles..."
		
		self.output_dir = output_xyz_image_sequences_dir

		self.grid_size = (canvas.size[0] / TILE_SIZE, canvas.size[1] / TILE_SIZE)
		print canvas.size
		print self.grid_size

		self.max_zoom = 0
		while pow(2, self.max_zoom) < max(self.grid_size):
			self.max_zoom = self.max_zoom + 1
		
		self.RenderBaseTiles()
		z = self.max_zoom - 1
		while z >= 0:

			self.RenderTilesForZoomLevel(z)

			z = z - 1

	def RenderTilesForZoomLevel(self, z):
		print "Rendering tiles for zoom level " + str(z)

	def RenderBaseTiles(self):
		print "Rendering base tiles with max zoom: " + str(self.max_zoom)
		
		base_dir = self.output_dir + "/" + str(self.max_zoom)

		for c in range(0, self.grid_size[0]):
			for r in range(0, self.grid_size[1]):
				
				left = c * TILE_SIZE
				right = left + TILE_SIZE
				top = r * TILE_SIZE
				bottom = top + TILE_SIZE
				pixel_bounds = Rect(Point(left, top), Point(right, bottom))

				print "Rendering base tile " + str((c, r))
				print "Bounds: " + str(pixel_bounds)
				
				source_tiles = canvas.SourceTilesInBounds(pixel_bounds)

				print source_tiles


				base_tile_image = Image.new("RGBA", (TILE_SIZE, TILE_SIZE))
				
				for source_tile in source_tiles:
					source_pos_in_target_space = source_tile.pos - Point(left, top)
					print source_pos_in_target_space
					base_tile_image.paste(source_tile.first_frame, source_pos_in_target_space.as_tuple())

				tile_dir = base_dir + "/" + str(c) + "/" + str(r)
				util.ensure_dir(tile_dir)
				path = tile_dir + "/0.jpg"
				base_tile_image.save(path)
				print




if __name__ == '__main__':
	canvas = Canvas()
	canvas.CreateSimpleSourceLayout("source_video_tiles_sequences", (3, 14))
	renderer = TileRenderer(canvas)

	renderer.RenderTiles("xyz_tiles_sequences")