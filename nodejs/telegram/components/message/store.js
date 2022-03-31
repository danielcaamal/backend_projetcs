const db = require('mongoose');
require('dotenv').config()

db.Promise = global.Promise;
uri = `mongodb://${process.env.DB_USER}:${process.env.DB_PASS}@${process.env.DB_HOST}:27017/${process.env.DB_NAME}`;
console.log(uri);
db.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => {
        console.log('[db] Connected to database: ' + process.env.DB_NAME);
    })
    .catch(err => {
        console.log('[db] Connection failed: ' + err);
    })

function addMessage(message){
    // list.push(message);
    const myMessage = new Model(message);
    myMessage.save();
}

function getMessages(){
    return list;
}

function deleteMessage(message){
    list.pop(message);
}

module.exports = {
    add: addMessage,
    list: getMessages,
    delete: deleteMessage,
}