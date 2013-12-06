def ensure_dir(path):
	if not os.path.exists(path):
		os.makedirs(path)

def intersects(bounds1, bounds2):
	