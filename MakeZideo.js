var fs = require('fs'),
    path = require('path'),
    cp = require('child_process')

var sourceVideoTileDir = process.argv[2];
var sourceVideoTileImageSequenceDir = 'source_video_tiles_image_sequences';

fs.mkdir(sourceVideoTileImageSequenceDir, function(err) {
	console.log(err);

	fs.readdir(sourceVideoTileDir, function(err, files) {
		files.forEach(function(f, i) {
			var cmd = "ffmpeg -i " + sourceVideoTileDir + '/' + f + ' ' +
			          "-vframes 1 -f image2 " +
			          sourceVideoTileImageSequenceDir + '/' + f + '.jpeg';
			//console.log(cmd);

			cp.exec(cmd, function(result, stderr, stdout) { // correct callback args?
				console.log(result);
			});
		});
	});
});

//# TODO better video file detection
//find $1/*.MOV -exec sh "mkdir -p source_video_tiles_image_sequences/`basename {}`\; ffmpeg -i {}" \;