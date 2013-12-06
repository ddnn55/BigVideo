import os

def ensure_dir(path):
	if not os.path.exists(path):
		os.makedirs(path)

def listdir(path):
	return filter(lambda f: f != ".DS_Store", os.listdir(path))