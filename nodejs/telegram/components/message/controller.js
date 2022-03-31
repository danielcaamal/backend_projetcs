const store = require('./store');

function addMessage(user, message){
    return new Promise((resolve, reject) => {
        if (!user || !message){
            console.error('[messageController] Error: user or message not provided');
            return reject('Invalid data');
        }

        const fullMessage = {
            user: user,
            message: message,
            date: new Date(),
        }
        
        store.add(fullMessage);

        console.log(fullMessage);
        return resolve(fullMessage);
    });
}

function getMessages(){
    return new Promise((resolve, reject) => {
        resolve(store.list());
    });
}

module.exports = {
    addMessage,
    getMessages
}