#!/usr/bin/env python

import util
from canvas import Canvas, RenderTileSet, RenderTile
from geometry import Rect, Point
from PIL import Image
import math

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
		
		base_tiles = self.RenderBaseTiles()
		self.RenderTilesForAllZoomLevelsUpTo(self.max_zoom - 1, base_tiles)


	def RenderTilesForAllZoomLevelsUpTo(self, z, z_plus_1_tiles):
		print "Rendering tiles for zoom level " + str(z)
		base_dir = self.output_dir + "/" + str(z)
		columns = math.ceil(float(z_plus_1_tiles.columns) / 2.0)
		rows = math.ceil(float(z_plus_1_tiles.rows) / 2.0)
		for c in range(0, columns):
			for r in range(0, rows):
				print "Rendering tile " + str((z, c, r))
				source_pos = Point(c * TILE_SIZE * 2, r * TILE_SIZE * 2)
				source_bounds = Rect(source_pos, source_pos + Point(2 * TILE_SIZE, 2 * TILE_SIZE))
				source_tiles = z_plus_1_tiles.TilesInBounds(source_bounds)

				tile_image = Image.new("RGBA", (TILE_SIZE * 2, TILE_SIZE * 2))

				for source_tile in source_tiles:
					source_tile_render_pos = source_tile.pos - source_pos
					tile_image.paste(source_tile.first_frame, source_tile_render_pos.as_tuple())

				tile_image.resize((TILE_SIZE, TILE_SIZE), filter=Image.ANTIALIAS)

				tile_dir = base_dir + "/" + str(c) + "/" + str(r)
				util.ensure_dir(tile_dir)
				path = tile_dir + "/0.jpg"
				base_tile_image.save(path)

		if z > 0:
			self.RenderTilesForAllZoomLevelsUpTo(z - 1, tile_set)


	def RenderBaseTiles(self):
		print "Rendering base tiles with max zoom: " + str(self.max_zoom)
		
		tile_set = RenderTileSet()
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

				tile_set.append(RenderTile(path, pixel_bounds))

				print

		print "Base render made tile set: " + str(tile_set)
		return tile_set




if __name__ == '__main__':
	canvas = Canvas()
	canvas.CreateSimpleSourceLayout("source_video_tiles_sequences", (3, 14))
	renderer = TileRenderer(canvas)

	renderer.RenderTiles("xyz_tiles_sequences")