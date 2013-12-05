#!/usr/bin/env python

# find $1 -name "*.MOV" -exec sh -c 'ffmpeg -y -i {} -vf "scale=910:512" -vf "crop=512:512:199:0" -c:v libx264 -preset medium -b:v 1000k -an -f mp4 delivery_video_test/`basename {}`.mp4' \;

import os

source_filenames = filter(lambda f: f != ".DS_Store", os.listdir("source_video_tiles"))

print source_filenames