console.time('main');

let sum = 0;
console.time('loop');
for (let i = 0; i < 1000000000; i++){
    sum += 1 ;
}
console.timeEnd('loop');

function fAsync(){
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log('Ending async process');
            resolve();
        })
    })
}

console.time('async');
fAsync().then(()=> {
    console.timeEnd('async');
});


console.timeEnd('main');
