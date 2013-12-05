#!/usr/bin/env python

import os

class SourceTile:

	def __init__(self, image_sequence_path):
		print "Created SourceTile: " + image_sequence_path

class Canvas:

	def __init__(self):
		pass

	def CreateSimpleSourceLayout(self, source_tile_image_sequences_dir, size):
		
		source_tile_names = filter(lambda f: f != ".DS_Store", os.listdir(source_tile_image_sequences_dir))
		
		self.source_tiles = map(lambda n: SourceTile(os.path.join(source_tile_image_sequences_dir, n)), source_tile_names)

	def SourceTilesInBounds(self, bounds):
		pass

if __name__ == '__main__':
	canvas = Canvas()
	canvas.CreateSimpleSourceLayout("source_video_tiles_sequences", (3, 14))