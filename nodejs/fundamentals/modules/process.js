process.on('beforeExit', () => console.log('Ending process...'));

process.on('exit', () => console.log('Process ended'));

process.on('uncaughtException', (err, origin) => console.log(err, origin));

it_breaks();