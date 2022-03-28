const http = require('http');

function router(req, res) {
    console.log('New request');
    console.log(req.url);
    res.writeHead(201, {'content_type' : 'text/plain'})
    switch (req.url) {
        case '/hello':
            res.write('Hello from Node JS');
            break;
        default:
            res.write('Error 404: Not Found')
            break;
    }
    res.end();
    
}

http.createServer(router).listen(3000);

console.log('Listening at port 3000');