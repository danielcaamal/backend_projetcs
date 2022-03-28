const fs = require('fs');

function read_file(route, cb) {
    fs.readFile(route, (err, data) => {
        console.log(data.toString());
    });
}

function write_file(route, content, cb) {
    fs.writeFile(route, content, (err) => {
        if (err){
            console.error('Something wrong happens')
        }else {
            console.log('File Wrote Successfully')
        }
        
    });
}

function delete_file(route, cb) {
    fs.unlink(route, (err) => {
        if (err){
            console.error('Something wrong happens')
        }else {
            console.log('File Deleted Successfully')
        }
    });
}

read_file(__dirname + '/file.txt')
write_file(__dirname + '/file_2.txt', 'I am a new file')
read_file(__dirname + '/file_2.txt')
delete_file(__dirname + '/file_2.txt')
