

console.log('Something');
console.info('Something');
console.warn('Something');
console.error('Something');


var table = [
    {
        a: 1, b: 'z'
    }, 
    {
        a: 2, b: 'a', c: 'b'
    },
    {
        a: 3, b: 'd', c: 'h'
    }
]
console.table(table);

console.group('Greetings')
console.log('Hello');
console.log('...');
console.log('Bye');
console.groupEnd()

console.log('Another logs');

console.count('counter');
console.count('counter');
console.count('counter');
console.count('counter');
console.countReset('counter');
console.count('counter');





