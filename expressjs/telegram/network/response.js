exports.success = function(req, res, body, status, error) {
    res.status(status || 200).send({
        'body': body || '',
        'error': error || ''
    });
}

exports.error = function(req, res, body, status, error){
    console.error(error);
    res.status(status || 500).send({
        'body': body || '',
        'error': error || ''
    });
}