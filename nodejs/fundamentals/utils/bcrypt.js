const bcrypt = require('bcrypt');

const pwd = '123456';

bcrypt.hash(pwd, 5, (err, hash) => {
    console.log(hash);
    bcrypt.compare(pwd, hash, (err, res) => console.log(res));
});
