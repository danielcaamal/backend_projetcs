db.createUser({
    user: "admin1",
    pwd: "admin1",
    roles: [
        {
            role: "readWrite",
            db: "chatdb"
        }
    ]
})