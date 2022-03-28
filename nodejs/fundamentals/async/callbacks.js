function hello(name, callback){
    setTimeout(function(){
        console.log('Hello ' + name);
        callback(name);
    }, 1000);
}

function goodbye(name, callback){
    setTimeout(function(){
        console.log('Goodbye ' + name);
        callback();
    }, 1000);
}

console.log('Starting Process...');
hello('Daniel', function(name){
    goodbye(name, function(){
        console.log('Ending Process (goodbye)');
    });
    console.log('Ending Process (hello)');
});

console.log('Ending Process...');

