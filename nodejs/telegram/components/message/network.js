const express = require('express');
const router = express.Router();
const response = require('../../network/response');
const controller = require('./controller');

router.get('/', (req, res) => {
    controller.getMessages()
        .then((messageList) => {
            response.success(req, res, messageList, 200);
        })
        .catch(e => {
            response.error(req, res, 'Error getting messages', 500, e);
        });
});

router.post('/', (req, res) => {
    controller.addMessage(req.body.user, req.body.message)
        .then((fullMessage) => {
            response.success(req, res, fullMessage, 200)
        })
        .catch(e => {
            response.error(req, res, 'Error adding message', 400, e);
        });
});

router.delete('/', (req, res) => {
    response.success(req, res, 'Message deleted', 200)
});

module.exports = router;