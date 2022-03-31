const db = require('mongoose');

//mongodb://<dbuser>:<dbpassword>@ds127989.mlab.com:27989/telegrome
db.connect('mongodb://daniel:caamal@192.168.100.32:27017/telegrome', { useNewUrlParser: true });


function addMessage(message){
    list.push(message);
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