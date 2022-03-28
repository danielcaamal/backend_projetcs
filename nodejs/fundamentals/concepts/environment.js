console.log('Starting module...');

// Environment Variables
let _name = process.env.NAME || 'Nonamed';

console.log(_name);

console.info(_name)
// nodemon for development
// pm2 for production