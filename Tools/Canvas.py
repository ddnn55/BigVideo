#!/usr/bin/env python

import os
from PIL import Image
import util


class SourceTile:

	def __init__(self, path):
		first_frame_image = Image.open(path + "/00001.jpg")
		
		self.width  = first_frame_image.size[0]
		self.height = first_frame_image.size[1]

		self.path = path

	def __str__(self):
		return str(self.pos) + ": " + self.path

class Canvas:

	def __init__(self):
		pass

	def CreateSimpleSourceLayout(self, source_tile_image_sequences_dir, size):
		
		source_tile_names = filter(lambda f: f != ".DS_Store", os.listdir(source_tile_image_sequences_dir))
		
		self.size = (0, 0)

		self.source_tiles = []
		for c in range(0, size[0]):
			for r in range(0, size[1]):
				tile_name = source_tile_names.pop(0)
				source_tile_path = os.path.join(source_tile_image_sequences_dir, tile_name)
				
				source_tile = SourceTile(source_tile_path)

				x = c * source_tile.width
				y = r * source_tile.height

				source_tile.pos = (x, y)

				self.size = (max(self.size[0], x + source_tile.width), max(self.size[1], y + source_tile.height))
				
				self.source_tiles.append(source_tile)


		#print([str(tile) for tile in self.source_tiles])

	def SourceTilesInBounds(self, bounds):
		return filter(lambda t: intersects(t.bounds(), bounds), self.source_tiles)

if __name__ == '__main__':
	canvas = Canvas()
	canvas.CreateSimpleSourceLayout("source_video_tiles_sequences", (3, 14))