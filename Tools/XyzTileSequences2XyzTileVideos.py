#!/usr/bin/env python

import util
import os
import subprocess

source_dir = "xyz_tiles_sequences"
destination_dir = "xyz_tiles_video"

zooms = util.listdir(source_dir)

for z in zooms:
	z_path = os.path.join(source_dir, z)
	cols = util.listdir(z_path)

	for c in cols:
		c_path = os.path.join(z_path, c)
		rows = util.listdir(c_path)

		for r in rows:
			sequence_path = os.path.join(c_path, r)
			video_destination_dir = os.path.join(destination_dir, z, c)
			util.ensure_dir(video_destination_dir)
			destination_path = os.path.join(video_destination_dir, r + ".mp4")
			cmd = '/usr/bin/env ffmpeg -f image2 -i "' + sequence_path + '/%5d.jpg"  -vcodec libx264 -b 300k "' + destination_path + '"'
			print cmd
			subprocess.call(cmd, shell=True)