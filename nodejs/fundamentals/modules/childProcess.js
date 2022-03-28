const { exec, spawn } = require('child_process');

exec('ls -la', (err, stdout, stderr) => {
    if (err) {
        console.log(err.message);
        return false
    }
    console.log(stdout);
    console.log(stderr);
});


exec('node fundamentals/modules/console.js', (err, stdout, stderr) => {
    if (err) {
        console.log(err.message);
        return false
    }
    console.log(stdout);
    console.log(stderr);
});

let process = spawn('ls', ['-la'])
console.log(process.pid)