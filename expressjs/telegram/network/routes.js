const express = require('express');

const routes = function(server){
    server.use('/message', require('../components/message/network'));
    server.use('/user', require('../components/user/network'));
    server.use('/chat', require('../components/chat/network'));
};

module.exports = routes;