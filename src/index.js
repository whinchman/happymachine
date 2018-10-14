var sys = require('sys')
var exec = require('child_process').exec;
var fs = require('fs');
const raspi = require('raspi');
const gpio = require('raspi-gpio');

//function puts(error, stdout, stderr) { sys.puts(stdout) }
const sleep = (milliseconds) => {
	return new Promise(resolve => setTimeout(resolve, milliseconds))
}

function setLED(output, on) {

	if (on === true) {
		output.write(gpio.HIGH)	
	} else {
		output.write(gpio.LOW)
	}
	
}

function sendToPrinter(message) {
	//have to write to a temp file, since we're going to call out directly to LPS
	fs.writeFile("/tmp/test", "Hey there!\nIs this Printing?\nOMG!!!", function(err) {
		if(err) {
			return console.log(err);
		}
	
		console.log("The file was saved!");

		//call directly out to LPS, not the best solution, but this is a dang raspi we're talking about.
		dir = exec("lp -d ZJ-58 /tmp/test", function(err, stdout, stderr) {
			if (err) {
				console.log("OH NO")
				console.log(err)
			}
			console.log(stdout);
		  });
		  
		  dir.on('exit', function (code) {
			// exit code is code
			console.log("Should have printed to printer")
		  });
	}); 
}

raspi.init(() => {
	// const input = new gpio.DigitalInput({
	//   pin: 'P1-3',
	//   pullResistor: gpio.PULL_UP
	// });
   
	const output = new gpio.DigitalOutput('P1-11');
   
	output.write(gpio.LOW);
});

var ledOn = false

while (true) {
	sleep(500).then(() => {
		setLED(output, ledOn)
		ledOn = !ledOn
	});
}







 
