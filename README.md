# Overview
    This app to get exchange currency rate between two currencies at specific date
    from external endpoint and save the exchange rate at database for future use.

### Technologies:
- FastAPI Framework (python)
- MySQL Database
- Docker
- Docker Compose
### Requirements
  - **Docker** 
    if you don't know how to install Docker please go to **(https://docs.docker.com/engine/install/ubuntu/)**
  - **Docker Compose**
    *if you don't know how to install Docker Compose please go to **(https://docs.docker.com/compose/install/)**
  
### Starting services

- in directory that has a docker-compse.yml file Run the following command:
```
        sudo docker-compose up -d --build
```
```sh
if you face error like this: ** Error starting userland proxy: listen tcp 0.0.0.0:3306: bind: address already in use **
please run this command: $ sudo service mysql stop
Then run docker command again.
```
***Note: after you run the above command please wait for almost 1 min after this command finished 
        because establishing MySQL connection takes some time then you can call the api to get exchange rate.***

### Stoping services

- in directory that has a docker-compse.yml file Run the following command:
```
        sudo docker-compose down -v
```

### Show logs
- To show app logs run this command:
```sh
       sudo docker-compose logs
```
# Documentation
-------------------------------------------------------------------------------------------
This app has a one endpoint /rate ,and It takes three query parameters:
- from_currency
- to_currency
- date
and respond with exchange rate for those currencies at specific date. 

## Routes:
- **GET http://0.0.0.0:3000/rate**
### Example:
- **Request:** curl -X GET "http://0.0.0.0:3000/rate?from_currency=USD&to_currency=MXN&date=2020-02-04"
- **Response:** {"from_currency": "USD", "to_currency": "MXN", "date": "2020-02-04", "rate": 18.7111}

### Testing:
- **To check database after you call the endpoint, you can run the following commands:**
 1: sudo docker-compose exec db bash
2: mysql -u root -p
3: it required password : enter password 
4: use flextock
5: select * from exchange_currency_rates;
- **To check if the endpoint got the rate from the external api or from database you can run this command:**
```
    $ sudo docker-compose logs
    you will find printed statement that told you from which place the endpoint respond to you,
    like that:
    //////////////////////////////////////
    GET FROM API
    /////////////////////////////////////
    Or:
    //////////////////////////////////////
    GET FROM DATABASE
    /////////////////////////////////////
```
