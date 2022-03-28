
function asyncFunction(cb){
    setTimeout(()=> {
        try {
            let a = 3 + 1;
            cb(null, a);
        } catch (e) {
            cb(e);
        }
    }, 1000)
}

asyncFunction((err, data) => {
    if (err) {
        console.error('Something went wrong: ' + err);
        return false;
    }
    console.log('The result: ' + data);
});