const os = require('os')

// Architecture
console.group('Architecture');
console.log(os.arch());
console.groupEnd('Architecture');

// Platform
console.group('Platform');
console.log(os.platform());
console.groupEnd('Platform');

// CPUs
console.group('CPUs');
console.log(os.cpus());
console.groupEnd('CPUs');

// Errors
console.group('Errors');
console.log(os.constants);
console.groupEnd('Errors');

// Free memory
console.group('Free/total memory');
console.log(os.freemem() + '/' + os.totalmem());
console.groupEnd('Free/total memory');

// Root Directory
console.group('Root Directory');
console.log(os.homedir());
console.groupEnd('Root Directory');

// Tmp Directory
console.group('Tmp Directory');
console.log(os.tmpdir());
console.groupEnd('Tmp Directory');

// Hostname
console.group('Hostname');
console.log(os.hostname());
console.groupEnd('Hostname');

// Active Network interfaces
console.group('Network Interfaces');
console.log(os.networkInterfaces())
console.groupEnd('Network Interfaces');