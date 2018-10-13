var sys = require('sys')
var exec = require('child_process').exec;
var fs = require('fs');

function puts(error, stdout, stderr) { sys.puts(stdout) }


fs.writeFile("/tmp/test", "Hey there!\nIs this Printing?\nOMG!!!", function(err) {
    if(err) {
        return console.log(err);
    }

	console.log("The file was saved!");
	dir = exec("lp -d ZJ-58 ./tmp/test", function(err, stdout, stderr) {
		if (err) {
		  // should have err.code here?  
		}
		console.log(stdout);
	  });
	  
	  dir.on('exit', function (code) {
		// exit code is code
	  });
	  
}); 






