#!/usr/bin/env python

import os
from PIL import Image
import util
from geometry import Point, Rect

TILE_SIZE = 512

class SourceTile:

	def __init__(self, path):
		self.first_frame = Image.open(path + "/00001.jpg")
		
		self.width  = self.first_frame.size[0]
		self.height = self.first_frame.size[1]

		self.path = path

	def __str__(self):
		return str(self.pos) + ": " + self.path

	def calculate_frame_count(self):
		frame_filenames = filter(lambda f: f != ".DS_Store", os.listdir(self.path))
		frame_numbers = map(lambda f: int(f.split('.')[0]), frame_filenames)
		return max(frame_numbers)

	def bounds(self):
		return Rect(self.pos, self.pos + Point(self.width, self.height))

	def frame(self, f):
		path = self.path + "/" + str(f+1).zfill(5) + ".jpg"
		#print "Reading source tile: " + path
		return Image.open(path)


class RenderTile:

	def __init__(self, path, bounds):
		self.path = path
		self.bounds = bounds

	def __str__(self):
		return str(self.bounds) + ": " + self.path

	def first_frame(self):
		return Image.open(self.path + "/0.jpg")

	def frame(self, f):
		path = self.path + "/" + str(f).zfill(5) + ".jpg"
		#print "Reading render tile: " + path
		return Image.open(path)

class RenderTileSet:

	def __init__(self):
		self.tiles = []
		self.columns = 0
		self.rows = 0

	def __str__(self):
		return str([str(tile) for tile in self.tiles])

	def append(self, tile):
		self.tiles.append(tile)
		self.columns = max(self.columns, tile.bounds.bottom_right().x / TILE_SIZE)
		self.rows = max(self.rows, tile.bounds.bottom_right().y / TILE_SIZE)

	def TilesInBounds(self, bounds):
		return filter(lambda t: t.bounds.overlaps(bounds), self.tiles)


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

				source_tile.pos = Point(x, y)

				self.size = (max(self.size[0], x + source_tile.width), max(self.size[1], y + source_tile.height))
				
				self.source_tiles.append(source_tile)


		#print([str(tile) for tile in self.source_tiles])

	def calculate_frame_count(self):
		return min([tile.calculate_frame_count() for tile in self.source_tiles])

	def SourceTilesInBounds(self, bounds):
		return filter(lambda t: t.bounds().overlaps(bounds), self.source_tiles)

if __name__ == '__main__':
	canvas = Canvas()
	canvas.CreateSimpleSourceLayout("source_video_tiles_sequences", (3, 14))