CREATE USER daniel WITH PASSWORD 'caamal';
CREATE DATABASE fastapi_twitter;
GRANT ALL PRIVILEGES ON DATABASE fastapi_twitter TO daniel;
ALTER DATABASE fastapi_twitter OWNER TO daniel;

\connect

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(30) NOT NULL,
    password VARCHAR(30) NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    birth_date DATE
);

CREATE TABLE IF NOT EXISTS tweets (
    id SERIAL PRIMARY KEY,
    content VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP,
    user_id int,
    CONSTRAINT fk_user 
        FOREIGN KEY(user_id) 
	    REFERENCES users(id)
);

INSERT INTO users (email, password, first_name, last_name, birth_date) 
    VALUES ('danielcaamal@email.com', '12345', 'daniel', 'caamal', '01-01-2000');

INSERT INTO tweets (content, created_at, updated_at, user_id) 
    VALUES ('First tweet made it', '01-01-2000 01:01:00', '01-01-2000 01:01:00', 1);