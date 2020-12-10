CREATE TABLE exchange_currency_rates (
    id INT NOT NULL AUTO_INCREMENT,
    from_currency VARCHAR(30) NOT NULL,
    to_currency VARCHAR(30) NOT NULL,
    date VARCHAR(30) NOT NULL,
    rate FLOAT ,
    PRIMARY KEY (id)
);
