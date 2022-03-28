function anotherFunction() {
    itBreaks();
}

function itBreaks() {
    return 3 + z;
}

function itBreaksAsync(cb) {
    setTimeout(() => {
        try {
            itBreaks();
        } 
        catch (err) {
            cb(err);
        }
    }, 1000);
}

try {
    // anotherFunction();
    itBreaksAsync((err) => {
        console.error(err.message);
    });
}
catch(err) {
    console.error('Something went wrong: ' + err);
}