#!/usr/bin/env python

# find $1 -name "*.MOV" -exec sh -c 'ffmpeg -y -i {} -vf "scale=910:512" -vf "crop=512:512:199:0" -c:v libx264 -preset medium -b:v 1000k -an -f mp4 delivery_video_test/`basename {}`.mp4' \;

import util
import os
import subprocess

source_dir = "source_video_tiles"
destination_dir = "source_video_tiles_sequences"

source_filenames = filter(lambda f: f != ".DS_Store", os.listdir(source_dir))

for source_filename in source_filenames:
	basename = os.path.splitext(source_filename)[0]
	source_path = source_dir + "/" + source_filename
	tile_destination_dir = destination_dir + "/" + basename + "/"
	util.ensure_dir(tile_destination_dir)
	destination_path = tile_destination_dir + "%05d.jpg"
	cmd = '/usr/bin/env ffmpeg -i "' + source_path + '" -an -f image2 "' + destination_path + '"'
	print cmd
	subprocess.call(cmd, shell=True)