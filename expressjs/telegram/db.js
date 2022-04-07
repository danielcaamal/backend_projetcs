const db = require('mongoose');

db.Promise = global.Promise;

async function connect(url) {
    await db.connect(url, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => {
        console.log('[db] Connected to database: ' + process.env.DB_NAME);
        console.log('[db] Mongo: ' + url);
        console.log('[db] Mongo Express: ' + 'http://' + process.env.DB_HOST +':8081');

    })
    .catch(err => {
        console.log('[db] Connection failed: ' + err);
    })
}

module.exports = connect;