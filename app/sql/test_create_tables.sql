CREATE TABLE IF NOT EXISTS test_admin
(
    id        integer PRIMARY KEY auto_increment,
    username  varchar(255) NOT NULL,
    password  text         NOT NULL,
    full_name text         NOT NULL,
    avatar    BLOB,
    CONSTRAINT UNIQUE (username)
);

CREATE TABLE IF NOT EXISTS test_hospital
(
    id    integer PRIMARY KEY auto_increment,
    name  varchar(255) NOT NULL,
    to_do text         NOT NULL,
    CONSTRAINT UNIQUE (name)

);

CREATE TABLE IF NOT EXISTS test_employee
(
    id            integer PRIMARY KEY auto_increment,
    name          varchar(255) NOT NULL,
    date_of_birth date         NOT NULL,
    salary        integer      NOT NULL,
    hospital_id   integer      NOT NULL,
    CONSTRAINT FOREIGN KEY (hospital_id) REFERENCES test_hospital (id)
        ON UPDATE CASCADE
);